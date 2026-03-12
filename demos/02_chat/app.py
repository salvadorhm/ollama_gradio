import ollama
import gradio as gr

def chat(message, history):
    # Solicitamos la respuesta a Ollama activando el modo stream
    stream = ollama.chat(
        model='gemma3:1b', 
        messages=[{'role': 'user', 'content': message}],
        stream=True,
    )
    
    # Variable para acumular el texto de la respuesta
    partial_message = ""
    
    # Iteramos sobre cada fragmento (chunk) que nos devuelve Ollama
    for chunk in stream:
        # Sumamos el nuevo fragmento de texto al mensaje parcial
        partial_message += chunk['message']['content']
        # 'yield' envía el progreso a Gradio para que lo muestre en la interfaz
        yield partial_message

ui = gr.ChatInterface(
    fn=chat,
    title="S.A.M.M."
)

ui.launch(share=False)
