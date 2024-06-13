import gradio as gr
import os

# あいさつの関数
def greet(name):
    return str(os.getenv('TEST_VALUE'))

# Interfaceの作成
demo = gr.Interface(
    fn=greet, 
    inputs="text", 
    outputs="text"
)

# 起動
demo.launch(server_name="0.0.0.0")