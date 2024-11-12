import ollama
import gradio as gr

def chat(message, history):
    response = ollama.chat(
        model='qwen2.5:0.5b', 
        messages=[{'role': 'user','content': message["text"]}],
        stream=False,
    )
    num_files = len(message["files"])
    print(f"You uploaded {num_files} files")
    return response['message']['content']


ui = gr.ChatInterface(
    fn=chat,
    type="messages",
    examples=[{"text": "Hello", "files": []}],
    title="S.A.M.M.",
    multimodal=True)

ui.launch()
