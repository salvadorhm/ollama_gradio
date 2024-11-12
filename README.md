# Ollama y Gradio

Demo de Ollama y Gradio implementar una UI de Chat

## 1. Instalar ollama

Descargar e instalar [ollama](https://ollama.com/download/linux)

````shell
curl -fsSL https://ollama.com/install.sh | sh
````

## 2. Inicializar el servidor

````shell
ollama serve
````

## 3. Descargar un modelo

Descargar un [modelo](https://ollama.com/library/qwen2.5:0.5b) 

````shell
ollama pull qwen2.5:0.5b
````

## 4. Crear un Ambiente virtual

````shell
python3 -m venv .venv
````

## 5. Activar el ambiente virtual

````shell
source .venv/bin/activate
````

## 6. Actualizar PIP

````shell
pip install --upgrade pip
````

## 7. Instalar las librerias de ollama y gradio

````shell
pip install -r requirements.txt
````

## 8. Ejecutar los demos

````shell
python3 app.py
````
