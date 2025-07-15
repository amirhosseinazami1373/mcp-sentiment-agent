import gradio as gr
from textblob import TextBlob
import nltk; nltk.download("punkt")

def sentiment(text: str) -> str:
    return str(TextBlob(text).sentiment)

demo = gr.Interface(fn=sentiment, inputs=gr.Textbox(), outputs=gr.Textbox())
demo.queue().launch(mcp_server=True)