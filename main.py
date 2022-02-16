import requests

from bs4 import BeautifulSoup

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime
now = datetime.datetime.now()

content = ''

def extract_news(url):
    print('Extracting HAcker News Stories...')
    cnt = ''
    cnt += ('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class':'title','valign':''})):
        cnt += ((str(i+1)+' :: '+tag.text+'\n'+'<br>') if tag.text!='More' else '')
        #print(ta,prettify)
    return(cnt)

cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>--------<br>')
content += ('<br><br>End of Message')

#Sending the email
print('Composing Email...')

SERVER = 'smtp.gmail.com'
PORT = 587
FROM = ''
TO = ''
PASS = ''

#fp = open(file_name, 'rb')
#Create a text/plain message
#msg = MIMEText('')
msg = MIMEMultipart()

#msg.add_header('Content-Disposition', 'attachment', filename='empty.txt')
msg['SUbject'] = 'Top News Stories HN [Automated EMail]' + ' ' + str(now.day) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))
#fp.close

print('Initiating Server...')
server = smtplib.SMTP(SERVER, PORT)
#server = smtplib.SMTP SSL('smtp.gmail.com', 465)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
#server.ehlo
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent...')

server.quit()
