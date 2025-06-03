
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20240123150734/Python-AI--(1).webp" alt="Python Logo" >

# AI-ChatBot-with-DialoGPT

This repository hosts a **state-of-the-art AI ChatBot** leveraging the pre-trained DialoGPT-large model by Microsoft. The bot generates natural and contextually relevant responses to user inputs, making it ideal for conversational AI applications.

---


## Features

- **Large-scale Pretrained Model**: Built using Microsoft's DialoGPT-large, trained on vast conversational datasets.
- **Interactive Interface**: Seamless integration with Gradio for an intuitive user experience.
- **Real-time Conversations**: The bot provides context-aware responses based on conversation history.
- **Customizable Theme**: Styled with the `boxy_violet` theme for a visually appealing interface.

---
## 🚀 [Live Demo](https://huggingface.co/spaces/throneAyush/AI-Chatbot)  
*(Click the link to try out the chatbot!)*  
## Requirements

Ensure you have the following installed:

- Python 3.8 or later
- Required Python packages (install via `pip`):
  - `transformers`
  - `gradio`
  - `torch`

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AyushGorlawar/AI-ChatBot-with-DialoGPT/
   cd ai-chatbot
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *Note: If the `requirements.txt` file isn't provided, manually install the packages listed in the [Requirements](#requirements) section.*

3. **Run the ChatBot**:
   ```bash
   python chatbot.py
   ```

---

## Usage

Once the chatbot is running, you can interact with it via the Gradio interface:

1. Open the link generated in your terminal.
2. Enter your message in the text box.
3. Receive real-time, context-aware responses from the AI.

### Example Interaction

- **User Input**: "How are you?"
- **Bot Response**: "I'm just a program, but I'm doing great! How can I assist you today?"

---

## Code Overview

### Key Components

1. **Model Initialization**:
   - The chatbot uses `AutoModelForCausalLM` and `AutoTokenizer` from the Hugging Face `transformers` library to load the DialoGPT-large model.

2. **Prediction Function**:
   - The `predict` function processes user inputs, appends conversation history, and generates a response using the model.

3. **Interface Setup**:
   - A Gradio interface binds the prediction function to an interactive web UI, featuring inputs for user text and conversation state.

### Main Libraries

- **Transformers**: For model loading and tokenization.
- **Gradio**: For creating an interactive web interface.
- **Torch**: For tensor operations and model inference.

---

## Customization

- **Theme**: Modify the Gradio theme by replacing `boxy_violet` with other available themes.
- **Model**: Experiment with different models from Hugging Face by replacing `microsoft/DialoGPT-large` with your desired model.

---

## Future Improvements

- Add multi-language support.
- Integrate a database to save conversation history.
- Enhance UI/UX for better accessibility.

---

 

## Acknowledgments

- **Hugging Face**: For providing the `transformers` library and pre-trained models.
- **Gradio**: For the intuitive interface framework.

---
 
