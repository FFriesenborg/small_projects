# basic le chat request
import requests
from dotenv import load_dotenv
import os
from mistralai import Mistral
from analyse_ATS_CV import read_cv
from datetime import datetime

cv_information=read_cv(r'C:\Users\fabic\Documents\GitHub\small_projects\Automating-Cover-Letters\20250314_CV_Fabian_Fischer_ATS.pdf')


with open(r'C:\Users\fabic\Documents\GitHub\small_projects\Automating-Cover-Letters\job_description.txt', 'r') as file:
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
            "content": "Please write the salutation and body of a cover letter in German (ca. 200 words) with the information from my CV: " + cv_information + " \n and the job description: " + job_description
        }
    ]
)

#print(chat_response.choices[0].message.content)

today_date = datetime.today().strftime('%Y-%m-%d' + '_')

with open(today_date + 'cover-letter.txt', 'w') as file:
    file.write(chat_response.choices[0].message.content)

