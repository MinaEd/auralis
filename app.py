import gradio as gr
from auralis_agent import auralis, AuralisState

def run_auralis(input_type, text, image):
    if input_type == "Text":
        result = auralis.invoke(AuralisState(input_type='text', content=text))
    else:
        result = auralis.invoke(AuralisState(input_type='image', content=image))
    return result["content"]

iface = gr.Interface(
    fn=run_auralis,
    inputs=[
        gr.Radio(["Text", "Image"], label="Input Type", value="Text"),
        gr.Textbox(label="Text Input"),
        gr.Image(label="Upload Image", type="filepath")
    ],
    outputs=gr.Textbox(
        label="Auralis Insight Output",
        lines=15,          # number of visible lines (increase for bigger box)
        max_lines=25,      # maximum height before scroll
        placeholder="Your summary or insight will appear here..."
    ),
    title="Auralis - AI Document & Image Insight Agent",
)

if __name__ == "__main__":
    iface.launch()
