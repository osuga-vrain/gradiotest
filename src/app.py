import gradio as gr

# あいさつの関数
def greet(name):
    return "Hello " + name + "!"

# Interfaceの作成
demo = gr.Interface(
    fn=greet, 
    inputs="text", 
    outputs="text"
)

# 起動
demo.launch(server_name="0.0.0.0")