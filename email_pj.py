from email_proj.credentials import get_credentials
import smtplib
import json


def send_mail(
        mail_to,
        mail_from,
        subject,
        mail_body,
        path_to_credentials = "credentials.json",
        path_to_output_json = "out.json",
        host = 'smtp.gmail.com',
        port = 587
):
    credentials = get_credentials(path_to_credentials)
    un = credentials['username']
    ps = credentials['password']

    out = {}
    # set up the SMTP server
    try:
        s = smtplib.SMTP(host=host, port=port)
        s.starttls()
        s.login(un, ps)

        s.sendmail(mail_from,mail_to,"Subject:"+subject +'\n\n'+ mail_body)
        s.quit()
    except:
        out['status'] = 'failed'
    else:
        out['status'] = 'success'

    with open(path_to_output_json, "w+") as outf:
        jsn = json.dump(out,outf)