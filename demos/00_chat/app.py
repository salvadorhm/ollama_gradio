import ollama
import gradio as gr

def chat(message, history):
    response = ollama.chat(
        model='qwen3.5:2b', 
        messages=[{'role': 'user','content': message}],
        stream=False,
    )
    return response['message']['content']

gr.ChatInterface(fn=chat).launch()
