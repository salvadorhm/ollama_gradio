import ollama
import gradio as gr

def chat(message, history):
    response = ollama.chat(
        model='gemma3:270m', 
        messages=[{'role': 'user','content': message}],
        stream=False,
    )
    return response['message']['content']

ui = gr.ChatInterface(
    fn=chat,
    title="S.A.M.M.")

ui.launch(share=False)
