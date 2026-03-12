import ollama
import gradio as gr
import os

def chat(message, history):
    # En modo multimodal, 'message' ya no es un string, sino un diccionario.
    # Contiene el texto escrito y una lista con las rutas de los archivos subidos.
    user_text = message.get("text", "")
    files = message.get("files", [])
    
    file_context = ""
    
    # Si hay archivos adjuntos, extraemos su contenido
    if files:
        for file_path in files:
            # Extraemos el nombre y la extensión del archivo
            filename = os.path.basename(file_path)
            ext = os.path.splitext(filename)[1].lower()
            
            # Verificamos que sea un tipo de archivo permitido (por seguridad extra)
            if ext in ['.txt', '.csv', '.md']:
                try:
                    # Leemos el contenido del archivo
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Formateamos el texto para que el modelo sepa qué es
                        file_context += f"\n\n--- Inicio del documento: {filename} ---\n"
                        file_context += content
                        file_context += f"\n--- Fin del documento: {filename} ---\n"
                except Exception as e:
                    file_context += f"\n[Error al intentar leer {filename}: {str(e)}]\n"
            else:
                file_context += f"\n[Aviso: Se ignoró el archivo {filename} porque no es .txt, .csv o .md]\n"

    # Construimos el prompt final
    # Si subieron archivos, le pasamos el contexto primero y luego la instrucción del usuario
    if file_context:
        final_prompt = f"A continuación se proporciona información de contexto:\n{file_context}\n\nInstrucción del usuario: {user_text}"
    else:
        final_prompt = user_text

    # Llamamos a Ollama (mantenemos el modo stream del paso anterior)
    stream = ollama.chat(
        model='gemma3:1b', 
        messages=[{'role': 'user', 'content': final_prompt}],
        stream=True,
    )
    
    partial_message = ""
    for chunk in stream:
        partial_message += chunk['message']['content']
        yield partial_message

# Configuramos la interfaz para que acepte archivos
ui = gr.ChatInterface(
    fn=chat,
    title="S.A.M.M. con Análisis de Documentos",
    multimodal=True, # ¡Esto activa el botón de subir archivos!
    textbox=gr.MultimodalTextbox(
        file_types=[".txt", ".csv", ".md"], # Restringe los archivos permitidos en el selector
        placeholder="Escribe un mensaje o arrastra archivos de texto aquí..."
    )
)

ui.launch(share=False)
