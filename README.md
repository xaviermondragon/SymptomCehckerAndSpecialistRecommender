# Symptom Checker and Specialist Recommender

GenAI-powered healthcare Assistant

## Description
This project is a [streamlit](https://streamlit.io/) app which
leverages Google's Gemimi large language models to interpret 
natural language health descriptions and accordingly:

- Interprets and summarizes the reported symptoms
- Indentifies likely medical conditions
- Recommends actions to be taken to lessen symptoms
- Recommends the best specialist(s) suited for the patient

## Getting Started
- In order to run this app, you need a Gemini API key, which you 
can generate [here](https://ai.google.dev/gemini-api/docs/api-key).
Once you have you API key, you can export it as an environment
variable by running
````commandline
export GEMINI_API_KEY="YOUR_API_KEY"
````
on Linux-like systems or
````commandline
GEMINI_API_KEY > "YOUR_API_KEY"
````
on Windows.
Alternatively, you can create a file named `.env` at the 
root directory with the following content
`GEMINI_API_KEY = "YOUR_API_KEY"`

### Dependencies
It is recommended to create a [Python virtual environment](https://docs.python.org/3/library/venv.html), 
[activate it](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) 
and install the dependencies there using the following command:
````commandline
pip install -r requirements.txt
````


### Running the app
Navigate to the root directory of this project, activate the 
virtual environment where the dependencies are installed and 
run the app with the following command:
````commandline
python main.py
````

### Architecture
- The web interface, where the user can write his symptoms, and where the response of
the model is shown is contained in the file 
`app.py`.
- The GenAI model is defined in the class `symptom_checker.py`
- The model is prompted to generate a response with predefined fields which are defined 
as a [pydantic](https://docs.pydantic.dev/latest/) model defined in the 
`HealthCareAdvice` class.