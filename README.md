# Sales Assistant Prototype

The Sales Assistant Prototype is a web application designed to provide sales representatives with key insights about products, competitors, and market strategy using advanced AI models. This project leverages the Groq AI model for natural language processing to generate structured reports based on the input data provided by the users.

## Features

- Generate insights about company strategy based on public data.
- Analyze competitors and market positioning.
- Provide summarized data from financial reports and press releases.
- User-friendly web interface for easy interaction and data presentation.

## Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python, Groq API
- **Deployment**: This application is designed to be deployed on platforms like Heroku, AWS, or similar PaaS providers.

## Project Structure

```
salesagent/
|-- __init__.py
|-- app.py         # Main application file for Streamlit interface
|-- model.py       # Handles API interactions with the Groq model
|-- utils.py       # Contains utility functions like prompt generation
|-- config.py      # Configuration details like API keys
|-- requirements.txt # Dependencies for the project
|-- Procfile       # For Heroku deployment
|-- setup.sh       # Setup script for Streamlit on Heroku
|-- README.md      # This file
```

## Setup Instructions

1. **Clone the Repository:**

   ```
   git clone https://github.com/yourusername/salesagent.git
   cd salesagent
   ```

2. **Install Dependencies:**

   ```
   pip install -r requirements.txt
   ```

3. **Environment Variables:**

   Set the necessary environment variables for your deployment:

   ```
   export GROQ_API_KEY='your_api_key_here'
   ```

   For Groq API key, Refer to this documentation: https://console.groq.com/docs/overview

4. **Run the Application:**

   ```
   streamlit run app.py
   ```


## Documentation

Further documentation on system architecture, use cases, and a detailed guide for contributors can be found in the project documentation.