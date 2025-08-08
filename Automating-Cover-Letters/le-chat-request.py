# basic le chat request
import requests
from dotenv import load_dotenv
import os
from mistralai import Mistral
from analyse_ATS_CV import read_cv
from datetime import datetime

language = 'German'

cv_information=read_cv(r'Automating-Cover-Letters\2024-04-01_CV_Fabian_Fischer_ATS.pdf')

with open(r'Automating-Cover-Letters\example_cover_letter.txt', 'r') as file:
    example_coverletter = file.read()

with open(r'Automating-Cover-Letters\job_description.txt', 'r') as file:
    job_description = file.read()


#API key is in an .env folder, excluded from the git repo
load_dotenv()
api_key = os.getenv("API_KEY")

model = "mistral-large-latest"

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": "Please write only the body of a (fairly factual) cover letter in " + language + "(max 300 words!) with the information from my CV: "
            + cv_information +
        " \n , two former cover letters: " + example_coverletter +
        " \n and use the language and try to tailor it to the job description: " + job_description 
        }
    ]
)

#print(chat_response.choices[0].message.content)

today_date = datetime.today().strftime('%Y-%m-%d' + '_')

with open("Automating-Cover-Letters/cover-letters/" + today_date + 'cover-letter.txt', 'w') as file:
    file.write(chat_response.choices[0].message.content)
    
with open("Automating-Cover-Letters/cover-letter.txt", 'w') as file:
    file.write(chat_response.choices[0].message.content)

