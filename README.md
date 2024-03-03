<h1 align="center">Child Name Generator: Fusion Name Creator 🚀</h1>

## Overview 📖
The Child Name Generator is a Generative AI based unique project aimed at assisting parents in choosing meaningful names for their children by fusing parts of both parents' names. Unlike traditional naming methods that might randomly mix letters, this application uses advanced Language Models (LLMs) and a custom fine-tuned model to generate names that are not only unique but also carry meaningful connections and cultural significance, particularly with references to Sanskrit.

## Key Features 🔑
- Meaningful Name Generation: Suggests names by intelligently fusing the parents' names, ensuring the output is meaningful and significant.
- Cultural and Linguistic Depth: Each suggested name is accompanied by its meaning and context, with a special focus on Sanskrit, enriching the cultural value of the name.
- Deployed Application: Easily accessible online platform for generating names without the need for local setup or installation at https://child-name-generator.streamlit.app/
- Custom Fine-Tuned Model: Utilizes a specialized model fine-tuned on a diverse dataset, ensuring high-quality and relevant name suggestions.

## Technologies Used 💻
- LangChain: For integrating language models seamlessly into applications.
- OpenAI: Leveraging the power of cutting-edge LLMs for name generation.
- Python: The core programming language used for developing the application.
- Kaggle Dataset: Utilizes a comprehensive dataset for training the custom model, enhancing the quality and relevance of name suggestions.
- Streamlit: Used for creating and deploying the web application, making it interactive and user-friendly.

## Getting Started🌟

### Prerequisites 🛠️

Ensure you have Python installed on your system.

You will need to get OpenAI API key from https://platform.openai.com/api-keys to authenticate.

### Installation📦

Clone the Repository: Start by cloning the repo to your local machine.
```bash
git clone https://github.com/jforjay1/child-name-generator.git
```
Install Requirements: Install all the necessary dependencies listed in the requirements.txt file.
```bash
pip install -r requirements.txt
```

### Setup🦾

Modify the secretkey.py file with your API keys and other sensitive information.

Modify app.py to uncomment 3rd line and replace ```st.secrets["api_key"]``` with ```api_key```

### Run⚙️

Finally, launch the application using Streamlit.
```bash
streamlit run app.py
```
Now, the application should be up and running, ready to generate meaningful names for your future children!

## Other Features: Creating Training Data 📊

This part is not spoon-fed, if you are using it then you will have to make some adjustments. ```Names.csv, training_data.csv, training_data.jsonl``` is just for reference.

### Steps:

- Gather data in 2 columns ```name1``` and ```name2``` and save it as Names.csv.
- Run each block of code from ```generate_answer.ipynb``` which will also help you understand how training data is prepared. This will help you generate training data for fine-tuning model.
- Run ```fine_tuning.ipynb``` to fine-tune gpt-3.5 model to meet your specific needs.
- Use fine-tuned model in ```app.py``` to achieve desired output.

## Purpose of the App 🎯
The Child Name Generator fills a niche but significant need for parents looking for meaningful, culturally rich names for their children. By leveraging advanced AI models and the rich linguistic heritage of Sanskrit, this application provides a modern solution to the age-old desire to name one's child with intention and significance. Whether you're looking for a name that carries a particular meaning or one that creatively combines aspects of both parents' names, this generator offers a thoughtful and innovative approach to a deeply personal decision.

### Contributors 🌍
This project thrives on collaboration and contributions from the community. We are grateful to the following contributors for their invaluable input and dedication:

<a href="https://github.com/jforjay1/child-name-generator/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=jforjay1/child-name-generator&anon=0" />
</a>

For contributions, suggestions, or any queries, feel free to open an issue or submit a pull request. Let's collaborate to enrich the Child Name Generator with more features and linguistic depth! 🌟👶📚
