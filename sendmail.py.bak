# -*- coding: utf-8 -*-
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE,formatdate
from email import encoders
import smtplib 
import os


server ={'name':'mail.funshion.com','user':'qa-fireflies','passwd':'nihao123!'}
fro = 'qa-fireflies@funshion.com'
to =['xiongsp@funshion.com']
cc =['liuyang1@funshion.com']
subject = 'Linda_0.2.6Web_ATDD TestResult'
file_result =open('/var/www/Linda026/result.txt','r').read()
text = file_result  
files=[]
msg=MIMEMultipart() 

def send_mail(): 
    assert type(server) == dict 
    assert type(to) == list 
    assert type(files) == list 
    assert type(cc) == list 
    
    msg = MIMEMultipart() 
    msg['From'] = fro 
    msg['Subject'] = subject 
    msg['To'] = COMMASPACE.join(to) 
    msg['Cc'] = COMMASPACE.join(cc)    
    msg['Date'] = formatdate(localtime=True) 
    msg.attach(MIMEText(text)) 
 
    for perfile in files: 
        part = MIMEBase('application', 'octet-stream') #'octet-stream': binary data 
        try:
            part.set_payload(open(perfile,'rb').read()) 
            encoders.encode_base64(part) 
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(perfile)) 
            msg.attach(part) 
        except IOError:
            print "The files path is not aviable!"       

    smtp = smtplib.SMTP(server['name']) 
    smtp.login(server['user'], server['passwd']) 
    smtp.sendmail(fro, to, msg.as_string())
    for cmail in cc:
        if cmail in to:
            continue
        smtp.sendmail(fro, cmail, msg.as_string())  
    smtp.close()


if __name__ == "__main__":
    send_mail()
