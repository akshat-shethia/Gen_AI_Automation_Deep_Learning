import yagmail

sender = "EMAIL1"
receiver = "EMAIL2"

subject = "This is a test mail"

contents = """
These are the contents of the mail
hi there!
"""

# Replace "your_app_specific_password" with the generated app-specific password
yag = yagmail.SMTP(user=EMAIL1, password="")

yag.send(to=EMAIL2, subject=subject, contents=contents)
print("Email sent!")
