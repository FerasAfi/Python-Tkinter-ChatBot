import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()


genai.configure(api_key=os.getenv("API_KEY"))

generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  generation_config=generation_config,
)


history=[]
seed_message = os.getenv("SEED_MESSAGE")

def send(message, history):

  while 1:
    chat_session = model.start_chat(history=[
    {"role": "user", "parts": ["Hello"]},
    {"role": "model", "parts": ["understood, how can i help you"]},])
    response = chat_session.send_message(seed_message+message)

    return(response.text.strip())



if __name__=="__main__":
  send(message='', history=[])



