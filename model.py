from groq import Groq
from config import API_KEY, MODEL_ID
from utils import generate_prompt
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def call_groq_model(product_name, company_url, product_category, competitors, value_proposition, target_customer):
    client = Groq(api_key=API_KEY)
    prompt = generate_prompt(product_name, company_url, product_category, competitors, value_proposition, target_customer)
    
    try: 
        completion = client.chat.completions.create(
            model=MODEL_ID,
            messages=[{"role": "system", "content": prompt}],
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )

        if completion.choices and completion.choices[0].message:
            return completion.choices[0].message.content
        else:
            return "No insights were generated or completion is malformed."
    except Exception as e:
        logging.error(f"An error occurred while calling the Groq model: {str(e)}")
        return "Error processing your request due to an internal error."