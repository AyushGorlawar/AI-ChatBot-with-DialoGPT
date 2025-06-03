from transformers import AutoModelForCausalLM, AutoTokenizer
import gradio as gr
import torch


title = "AI ChatBot"
description = "A State-of-the-Art Large-scale Pretrained Response generation model (DialoGPT)"
examples = [["How are you? buddy"]]
article = """
### Authors and Credits
- **Model**: Based on Microsoft's [DialoGPT-large](https://huggingface.co/microsoft/DialoGPT-large).
- **Developed by**: Ayush Gorlawar.
- **Libraries Used**: Hugging Face Transformers, PyTorch, Gradio.
- **Credits**: Special thanks to Microsoft for providing the pretrained model.
"""

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")


def predict(input, history=[]):

    new_user_input_ids = tokenizer.encode(
        input + tokenizer.eos_token, return_tensors="pt"
    )

    bot_input_ids = torch.cat([torch.LongTensor(history), new_user_input_ids], dim=-1)

    history = model.generate(
        bot_input_ids, max_length=4000, pad_token_id=tokenizer.eos_token_id
    ).tolist()

    response = tokenizer.decode(history[0]).split("<|endoftext|>")
    response = [
        (response[i], response[i + 1]) for i in range(0, len(response) - 1, 2)
    ]
    return response, history


gr.Interface(
    fn=predict,
    title=title,
    description=description,
    examples=examples,
    inputs=["text", "state"],
    outputs=["chatbot", "state"],
    theme="finlaymacklon/boxy_violet",
).launch()
