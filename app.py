# Project: get contacts from json file and log in into smtp seesion and then send an email_proj
# then print out into a json file the sending status ex: status : success
from email_proj.email_pj import send_mail
from datetime import datetime

mail_to = "ur.mail@yahoo.com"
mail_from ="me@gmail.com"
subject = "subj"

now = datetime.now()
mail_body = "You're amazing!\n Sent on "+ now.strftime("%Y-%m-%d %H:%M:%S")

#optional
path_to_credentials = "credentials.json"
path_to_output_json = "out.json"
host = 'smtp.gmail.com'
port = 587

send_mail(
    mail_to,
    mail_from,
    subject,
    mail_body,
    path_to_credentials,
    path_to_output_json,
    host,
    port)