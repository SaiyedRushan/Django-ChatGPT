# Django-GPT & DALL-E clone

Django-ChatGPT is a web application that integrates the power of GPT-3.5 language model from OpenAI into a Django-based chatbot. This project aims to demonstrate how advanced language models can be used to create interactive and intelligent chatbots for various applications.

## Features

- **Interactive Chat Interface**: Users can engage in conversations with the chatbot using a user-friendly interface.
- **Dall E Image generation**: Users can generate images using openai's dall-e api with the chatbot using a user-friendly interface.
- **GPT-3.5 Language Model**: The application leverages the GPT-3.5 language model from OpenAI to generate human-like responses.
- **Customizable**: The chatbot's behavior and responses can be fine-tuned and customized as needed.
- **User Management**: Users can register, login, and manage their chat history.
- **Admin Dashboard**: Administrators have access to an admin dashboard to view user interactions and manage the application.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/SaiyedRushan/Django-ChatGPT.git
cd Django-ChatGPT
```

2. Create a virtual environment and activate it:

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Set up the database:

```bash
python manage.py migrate
```

5. Create a superuser for the admin dashboard:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

7. Visit `http://127.0.0.1:8000/` in your web browser to access the application.

## Configuration

To use the GPT-3.5 language model, you need to set up an API key from OpenAI. Once you have the API key, open `chat/views.py` and replace `YOUR_API_KEY` with your actual API key.

## Contributing

Contributions are welcome! If you find any bugs or want to add new features, please create an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://github.com/SaiyedRushan/Django-ChatGPT/blob/main/LICENSE).

## Acknowledgments

- The project uses the [Django](https://www.djangoproject.com/) web framework.
- Special thanks to the [OpenAI](https://openai.com/) team for providing the GPT-3.5 language model.

## Disclaimer

This project is intended for educational and demonstration purposes only. The use of the GPT-3.5 language model may be subject to specific terms and conditions by OpenAI. Please refer to the [OpenAI website](https://platform.openai.com/) for more information.

---
*Please note that the above README.md is a template and may require adjustments based on the actual project features, developments, and requirements.*

