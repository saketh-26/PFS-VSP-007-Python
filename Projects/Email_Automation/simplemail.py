'''
Email Automation using Python -->Set up Gmail App Password (2-Step Verfctn ON)
-->We create a project specific Password

We will be using SMTP Library (Simple Mail Transfer Protocol)
'''
import smtplib
#Now we need to connect to the server ->Gmail
server = smtplib.SMTP("smtp.gmail.com",587)
print(server)
#Start the connection
server.starttls()
#give your login credentials
server.login("saketh@codegnan.com","tqiq frji awpd sbbd")
print("Success")
#give your desired message
message = "This is the First mail sent using Python"
server.sendmail("saketh@codegnan.com",
                "vinaysambana1@gmail.com",message)
server.close()
print("Mail Sent")











