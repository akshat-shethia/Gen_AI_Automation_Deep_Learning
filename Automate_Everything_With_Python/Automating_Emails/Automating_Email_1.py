import yagmail

sender = "akshatshethia1@gmail.com"
receiver = "afpzgoaee@10mail.org"

subject = "This is a test mail"

contents = """
These are the contents of the mail
hi there!
"""

# Replace "your_app_specific_password" with the generated app-specific password
yag = yagmail.SMTP(user=sender, password="Aeroplane12")

yag.send(to=receiver, subject=subject, contents=contents)
print("Email sent!")
