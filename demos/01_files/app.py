import ollama
import gradio as gr

def chat(message, history):
    print("received message:", message)
    text = message.get("text", "") or ""
    files = message.get("files", []) or []
    # Gradio sometimes returns FileData objects, other times simple file-path
    # strings. Accept both by checking for the attribute.
    image_paths = []
    for f in files:
        if hasattr(f, "path"):
            image_paths.append(f.path)
        elif isinstance(f, str):
            image_paths.append(f)
        else:
            # unknown format, just log it
            print("warning: unexpected file object", repr(f))
    if image_paths:
        print(f"attaching {len(image_paths)} image(s) to model request: {image_paths}")

    payload = {'role': 'user', 'content': text}
    if image_paths:
        payload['images'] = image_paths

    response = ollama.chat(
        model='qwen3-vl:2b',
        messages=[payload],
        stream=False,
    )

    return response['message']['content']

ui = gr.ChatInterface(
    fn=chat, 
    title="S.A.M.M.",
    multimodal=True,
    textbox=gr.MultimodalTextbox(file_count="multiple", file_types=["image"], sources=["upload"])
)
ui.launch(share=False)
