from fastapi import FastAPI, Request, Query
from fastapi.middleware.cors import CORSMiddleware
from hellosign_sdk import HSClient


import joblib
import json
import pickle
from fpdf import FPDF
import time
import os
from datetime import date


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
    infoDict = await info.json()

    pdf = FPDF()
    pdf.add_page()


    pdf.set_font("Times", size = 15)
    pdf.cell(200, 10, txt = "Hello Doc",
    ln = 1 , align='C')
    pdf.cell(200, 10, txt = infoDict['DoctorName'],
    ln = 1)
    pdf.cell(200, 10, txt = infoDict['DoctorInfo'],
    ln = 2)
    pdf.cell(200, 10, txt = infoDict['DoctorNo'],
    ln = 2)
    pdf.cell(200, 10, txt = infoDict['DoctorEmail'],
    ln = 2)
  
  

    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    today = date.today()

    pdf.cell(200, 10, txt = str(today),
    ln = 2, align='R')

    pdf.cell(200, 10, txt = str(curr_clock),
    ln = 2, align='R')
  
  

    for i in range(len(infoDict['Medication'])):
        pdf.cell(200, 10, txt = " - ".join(infoDict['Medication'][i]), ln = 2)

    pdf.cell(200, 10, txt = "\n\n\n", ln = 2)
    pdf.cell(200, 10, txt = "Note: " + infoDict["AdditionalInfo"], ln = 2)

    pdf.cell(200, 10, txt = "To,", ln = 2)
    pdf.cell(200, 10, txt = "Patient Name: " + infoDict['PatientName'], ln = 2)
    pdf.cell(200, 10, txt = "Patient Email: " + infoDict["PatientEmail"] , ln = 2)

    file_path = infoDict['PatientName'] + ".pdf"
    pdf.output(file_path)

    client.send_signature_request(
            test_mode=True,
            title="prescription - %s"%(infoDict['DoctorName']),
            subject="Test Subject",
            message="Please sign this to give the prescription!!",
            signers=[
                {'email_address': infoDict["DoctorEmail"], 'name': infoDict['DoctorName'] },
                ],
            cc_email_addresses = [infoDict["PatientEmail"]],
            files=[file_path]
    )

   
    if os.path.exists(file_path):
        os.remove(file_path)


    

    return {"Status" : "True"}
