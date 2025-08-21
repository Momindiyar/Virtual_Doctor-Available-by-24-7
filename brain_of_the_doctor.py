# if you dont use pipenv uncomment the following:
from dotenv import load_dotenv
load_dotenv()

#Step1: Setup GROQ API key
import os

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

#Step2: Convert image to required format
import base64


#image_path="acne.jpg"

def encode_image(image_path):   
    image_file=open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8')

#Step3: Setup Multimodal LLM & Also bea Open Source LLM
# from groq import Groq

# query="Is there something wrong with my face?"
# #model = "meta-llama/llama-4-maverick-17b-128e-instruct"
# model="meta-llama/llama-4-scout-17b-16e-instruct"
# #model = "meta-llama/llama-4-scout-17b-16e-instruct"
# #model="llama-3.2-90b-vision-preview" #Deprecated

# We have used the OpenAi Model which are Paid
from openai import OpenAI
query = "is there something wrong with my face?"
model = "gpt-4o"

def analyze_image_with_query(query, model, encoded_image):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]
    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content




# # ===================== TEST BLOCK TO CHECK IF IT WORKS =====================
# if __name__ == "__main__":
#     # ❗ change the image path below to *your* image
#     image_path = "acne.jpg"  # <-- e.g. "acne.jpg" or "image.jpg"
    
#     # ❗ change the query below if you want to ask something else
#     test_query = "Is there any issue with my skin?"

#     # Encode the image
#     encoded_img = encode_image(image_path)

#     # Call the function
#     response = analyze_image_with_query(
#         query=test_query,
#         model=model,
#         encoded_image=encoded_img
#     )

#     print("===== MODEL RESPONSE =====")
#     print(response)