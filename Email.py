import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = '<<username>>'
password = '<<password>>'

def send_mail(text="This email was sent using Python", subject="Email Testing", from_email='Anshul <anshuljawale04@gmail.com>',to_email=['anshuljawale04@gmail.com']):
    #Message Formatting
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ', '.join(to_email)
    msg['Subject'] = subject
    text_part = MIMEText(text, 'plain')
    msg.attach(text_part)    
    msg_str = msg.as_string()
    
    #login
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)  #instance of SMTP
    server.ehlo()    #run server on default
    server.starttls()          #secure connection
    server.login(user=username, password=password)
    server.sendmail(from_email, to_email, msg_str)
    server.quit()

try:
    send_mail()
    sent = True   
except:
    sent = False    

if sent:
    print("The email was sent successfully.")
else:
    print("The email was not sent. Try again.")
    
