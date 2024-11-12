import ollama
import gradio as gr

def chat(message, history):
    response = ollama.chat(
        model='qwen2.5:0.5b', 
        messages=[{'role': 'user','content': message}],
        stream=False,
    )
    return response['message']['content']

gr.ChatInterface(chat, type="messages").launch()
