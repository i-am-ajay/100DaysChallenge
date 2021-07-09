import imaplib
import base64
import os
import email


class EmailExtractor:
    email_id = "ajay.chandel@sgrh.com"
    email_password = "!3August@1986"

    mail = imaplib.IMAP4_SSL("http://webmail.sgrh.com", 143)
    mail.login(email_id, email_password)
    #mail.close()
