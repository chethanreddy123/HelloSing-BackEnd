from fpdf import FPDF
from datetime import date
import time

infoDict = {
    "PatientName" : "Jack",
    "PatientEmail" : "chethan.tekie@gmail.com",
    "DoctorName" : "Dr. Rajesh",
    "DoctorInfo" : "M.B.B.S M.D, M.S | RegNO: 2000234",
    "DoctorNo" : "9924352433",
    "DoctorEmail" : "chethan.campk12@gmail.com",
    "Medication" : [
        ["Anti-inflammatory Tablets" , "1" , "Morning"] , 
        ["Nepafenac eye drops" , "2 Drops" , "Night"] , 
        ["Dexketoprofen for pain" , "1.5 Tablet" , "Afternoon"]
        ],
    "AdditionalInfo" : "Make sure that tablets are placed in order."
}

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


print("Today date is: ", today)
  
print(curr_clock)

pdf.cell(200, 10, txt = str(today),
    ln = 2, align='R')

pdf.cell(200, 10, txt = str(curr_clock),
    ln = 2, align='R')
  
  

for i in range(len(infoDict['Medication'])):
    pdf.cell(200, 10, txt = " - ".join(infoDict['Medication'][i]), ln = 2)
    print("-".join(infoDict['Medication'][i]))

pdf.cell(200, 10, txt = "\n\n\n", ln = 2)



pdf.cell(200, 10, txt = "Note: " + infoDict["AdditionalInfo"], ln = 2)

pdf.cell(200, 10, txt = "To,", ln = 2)
pdf.cell(200, 10, txt = "Patient Name: " + infoDict['PatientName'], ln = 2)
pdf.cell(200, 10, txt = "Patient Email: " + infoDict["PatientEmail"] , ln = 2)









pdf.output("GFG.pdf")

