import ollama
import gradio as gr

def chat(message, history):
    # Extracción de texto y resolución de rutas de imágenes en una sola línea
    text = message.get("text", "") or ""
    images = [getattr(f, "path", f) for f in message.get("files", []) if hasattr(f, "path") or isinstance(f, str)]

    # Construcción dinámica del payload
    payload = {'role': 'user', 'content': text}
    if images: 
        payload['images'] = images

    # Llamada síncrona a Ollama
    response = ollama.chat(model='qwen3-vl:2b', messages=[payload])
    
    return response['message']['content']

# Configuración y lanzamiento de la interfaz encadenados
ui = gr.ChatInterface(
    fn=chat, 
    title="S.A.M.M.",
    multimodal=True,
    textbox=gr.MultimodalTextbox(
        file_count="multiple", 
        file_types=["image"], 
        sources=["upload"]
        )
)

ui.launch()
