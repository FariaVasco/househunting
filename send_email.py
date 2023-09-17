from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import pandas as pd


def send_email(listings, email):

    df = pd.DataFrame(listings)

    html = """\
    <html>
      <head></head>
      <body>
        {0}
      </body>
    </html>
    """.format(df.to_html())

    msg = MIMEMultipart()
    password = 'ldaswfxgjifsbukl'
    msg['Subject'] = "New listings found"
    msg['From'] = 'house.hunting.scraping@gmail.com'
    msg['To'] = email

    body = MIMEText(html, 'html')
    msg.attach(body)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
