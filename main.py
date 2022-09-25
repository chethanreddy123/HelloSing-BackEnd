from fastapi import FastAPI, Request, Query
from fastapi.middleware.cors import CORSMiddleware
from hellosign_sdk import HSClient


import joblib
import json
import pickle
from fpdf import FPDF
import time
import os

client = HSClient(api_key='a65d631bc7a875990682b67ac1cc37ca0aef34ab537b52d57bddb4f633afb7a2')


app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/sendform")
async def getInformation(info : Request):
    print(await info.body())
    req_info = await info.json()

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size = 15)
 

    pdf.cell(200, 10, txt = "GeeksforGeeks",
         ln = 1)

    pdf.cell(200, 10, txt = "A Computer Science portal for geeks.",
         ln = 2, align = 'C')

    pdf.output("GFG.pdf")

    client.send_signature_request(
            test_mode=True,
            title="title=Test Title.",
            subject="Test Subject",
            message="Please sign this.",
            signers=[{ 'email_address': 'chethan.tekie@gmail.com', 'name': 'Alice Smith' }],
            files=['GFG.pdf']
    )


    file_path = "GFG.pdf"
   
    if os.path.exists(file_path):
        os.remove(file_path)


    

    return {"Status" : "True"}
