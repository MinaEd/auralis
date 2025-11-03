import gradio as gr
from auralis_agent import auralis, AuralisState
import base64

def run_auralis(input_type, text, image):
    if input_type == "Text":
        result = auralis.invoke(AuralisState(input_type='text', content=text))
    else:
        result = auralis.invoke(AuralisState(input_type='image', content=image))
    return result["content"]

# Read and encode the logo as base64
def get_logo_base64():
    try:
        with open(r"C:\auralis\auralis_logo.png", "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        print("Logo file not found, using placeholder")
        return None

logo_base64 = get_logo_base64()

# Custom CSS with Auralis branding colors
custom_css = """
/* Main container styling */
.gradio-container {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%) !important;
}

/* Header with logo */
.title-container {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1.5rem;
    padding: 2rem 1rem;
    background: rgba(44, 95, 127, 0.1);
    border-radius: 15px;
    margin-bottom: 1.5rem;
}

.logo-img {
    width: 80px;
    height: 80px;
    object-fit: contain;
}

h1 {
    color: white !important;
    font-size: 3rem !important;
    font-weight: 800 !important;
    letter-spacing: 3px !important;
    margin: 0 !important;
}

/* Label styling */
label {
    color: white !important;
    font-weight: 600 !important;
    font-size: 16px !important;
}

/* Radio buttons styling */
.gr-radio {
    background: rgba(255, 255, 255, 0.95) !important;
    border-radius: 10px !important;
    padding: 1rem !important;
}

.gr-radio label {
    background: #2c5f7f !important;
    color: white !important;
    border-radius: 8px !important;
    padding: 0.6rem 1.2rem !important;
    font-weight: 600 !important;
    margin: 0.3rem !important;
    transition: all 0.3s ease !important;
}

.gr-radio input:checked + label {
    background: #1a3a4f !important;
    box-shadow: 0 4px 15px rgba(44, 95, 127, 0.4) !important;
    transform: scale(1.05) !important;
}

/* Textbox and textarea styling - FIXED TEXT COLOR */
textarea, .gr-textbox textarea {
    border: 2px solid #2c5f7f !important;
    border-radius: 10px !important;
    font-size: 15px !important;
    background: white !important;
    color: #1a3a4f !important;
}

textarea::placeholder {
    color: #6b7280 !important;
}

textarea:focus, .gr-textbox textarea:focus {
    border-color: #1a3a4f !important;
    box-shadow: 0 0 0 3px rgba(44, 95, 127, 0.2) !important;
    color: #1a3a4f !important;
}

/* Image upload area */
.gr-image {
    border: 2px dashed #2c5f7f !important;
    border-radius: 10px !important;
    background: rgba(255, 255, 255, 0.95) !important;
}

/* Submit button */
.gr-button-primary {
    background: linear-gradient(135deg, #2c5f7f 0%, #1a3a4f 100%) !important;
    color: white !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    padding: 0.8rem 2rem !important;
    border-radius: 10px !important;
    border: none !important;
    box-shadow: 0 6px 20px rgba(44, 95, 127, 0.4) !important;
    transition: all 0.3s ease !important;
}

.gr-button-primary:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(44, 95, 127, 0.6) !important;
}

/* Clear button */
.gr-button-secondary {
    background: rgba(255, 255, 255, 0.1) !important;
    color: white !important;
    border: 2px solid rgba(255, 255, 255, 0.3) !important;
    transition: all 0.3s ease !important;
}

.gr-button-secondary:hover {
    background: rgba(255, 255, 255, 0.2) !important;
    border-color: rgba(255, 255, 255, 0.5) !important;
}

/* Output box - FIXED TEXT COLOR */
.output .gr-textbox textarea {
    background: white !important;
    border: 2px solid #2c5f7f !important;
    font-family: 'Segoe UI', system-ui, sans-serif !important;
    line-height: 1.8 !important;
    color: #1a3a4f !important;
    font-size: 15px !important;
}

/* Form container */
.gr-form {
    background: rgba(255, 255, 255, 0.05) !important;
    border-radius: 15px !important;
    padding: 1.5rem !important;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
}

/* Info text color fix */
.gr-info {
    color: rgba(255, 255, 255, 0.8) !important;
}
"""

# HTML for header with logo - Using base64 embedded image
if logo_base64:
    header_html = f"""
<div class="title-container">
    <img src="data:image/png;base64,{logo_base64}" class="logo-img" alt="Auralis Logo"/>
    <h1>AURALIS</h1>
</div>
"""
else:
    # Fallback to SVG if image not found
    header_html = """
<div class="title-container">
    <svg class="logo-img" width="80" height="80" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
        <circle cx="100" cy="140" r="20" fill="#2c5f7f"/>
        <circle cx="100" cy="140" r="35" fill="none" stroke="#2c5f7f" stroke-width="12"/>
        <path d="M 50 140 A 50 50 0 0 1 150 140" fill="none" stroke="#2c5f7f" stroke-width="12" stroke-linecap="round"/>
        <path d="M 35 110 A 80 80 0 0 1 165 110" fill="none" stroke="#2c5f7f" stroke-width="12" stroke-linecap="round"/>
        <path d="M 20 80 A 110 110 0 0 1 180 80" fill="none" stroke="#2c5f7f" stroke-width="12" stroke-linecap="round"/>
    </svg>
    <h1>AURALIS</h1>
</div>
"""

# Function to toggle visibility
def toggle_inputs(input_type):
    if input_type == "Text":
        return gr.update(visible=True), gr.update(visible=False)
    else:
        return gr.update(visible=False), gr.update(visible=True)

# Create interface using Blocks for side-by-side layout
with gr.Blocks(css=custom_css, theme=gr.themes.Soft(primary_hue="blue", secondary_hue="slate")) as iface:
    gr.HTML(header_html)
    
    with gr.Row():
        # Left column - Input
        with gr.Column(scale=1):
            input_type = gr.Radio(
                ["Text", "Image"], 
                label="📌 Input Type", 
                value="Text",
                info="Choose whether to analyze text or an image"
            )
            
            text_input = gr.Textbox(
                label="📝 Text Input",
                placeholder="Paste your text here for analysis...",
                lines=10,
                visible=True
            )
            
            image_input = gr.Image(
                label="🖼️ Upload Image", 
                type="filepath",
                sources=["upload", "clipboard"],
                visible=False
            )
            
            with gr.Row():
                submit_btn = gr.Button("✨ Generate Insights", variant="primary")
                clear_btn = gr.Button("🔄 Clear", variant="secondary")
        
        # Right column - Output
        with gr.Column(scale=1):
            output = gr.Textbox(
                label="💡 Auralis Insight Output",
                lines=15,
                max_lines=25,
                placeholder="Your insights will appear here...\n\n✨ Upload content and click Submit to begin analysis.",
                show_copy_button=True,
                elem_classes="output"
            )
    
    # Toggle visibility when radio button changes
    input_type.change(
        fn=toggle_inputs,
        inputs=[input_type],
        outputs=[text_input, image_input]
    )
    
    # Submit button click
    submit_btn.click(
        fn=run_auralis,
        inputs=[input_type, text_input, image_input],
        outputs=[output]
    )
    
    # Clear button click
    clear_btn.click(
        fn=lambda: ("Text", "", None, ""),
        outputs=[input_type, text_input, image_input, output]
    )

if __name__ == "__main__":
    iface.launch()