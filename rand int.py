
#how to send real time mail:
import smtplib
import random
def read_data_send_mail():
    try :  
           f=open("student_mail.txt","r")
           student_mail=f.read()

           student_mail=student_mail.split(",")
           print(student_mail)
    except:
         print("file not available") 

    sender_email="harshavardhan6281240878@gmail.com"          
 
    for i in student_mail:
        otp_number=random.randint(0000,9999)
        s=smtplib.SMTP("smtp.gmail.com",587)
        s.starttls()
        s.login(sender_email," lgui nywp zlmp tqiq") 
        message=f"hi your otp is:{otp_number}"
        try:
            s.sendmail(sender_email,i,message)
            print("mail sent successfully")
            s.quit()
        except:
             print("mail not sent")  

read_data_send_mail()               


