import smtplib
import email.message

# Put the emails you want to send to this list
emails = ['email1@gmail.com', 'email2@outlook.com', 'fernandacrs0104@yahoo.com']

def enviar_email(to):  
    body_email = """
    <h1>Message of email</h1>
    """

    msg = email.message.Message()
    # Subject of email
    msg['Subject'] = "Subject of email"
    # Your email
    msg['From'] = 'youremail@gmail.com'
    msg['To'] = to
    # Password of your email
    password = 'Password of your email' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print(f'Email sent to {to} successfully!')

for i in range(len(emails)):
    enviar_email(emails[i])