import requests
from bs4 import BeautifulSoup
from datetime import date
import smtplib


# Setting up BeautifulSoup
def jobs_bg():
    url = 'https://www.jobs.bg/front_job_search.php?subm=1&categories%5B%5D=56&techs%5B%5D=Python&job_type%5B%5D=4'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    return soup

new_jobs = []

# Scraping jobs.bg
def check_for_new_jobs(s):
    jobs_listings = s.find_all('div', class_='mdc-layout-grid__inner')
    for i in jobs_listings:
        job_date = i.find('div', class_='card-date').text.split()[0]
        if job_date == 'днес':
            job_name = i.find('a')['title']
            web_page = i.find('a')['href']
            company_name = i.find('div', class_='right').a['title']
            real_date = date.today().strftime('%d.%m.%y')
            job = {
                'Job Name': job_name,
                'Company Name': company_name,
                'Date Added': real_date,
                'Link': web_page
                   }
            new_jobs.append(job)

# Text for the mail
def mail_text():
    b = ''
    for j in new_jobs:
        t = f'Има нова позиция от днес като {j["Job Name"]} в {j["Company Name"]} - {j["Link"]}'
        b = b + t +'\n'
    return b

# Setting up and use SMTP to send myself a mail with the newest jobs
# Replace the login/sendmail information with your email
def send_me_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login('myemail@mail.com', 'password')
    subject = 'Нови позиции от jobs.bg'
    body = mail_text()
    message = f'Subject: {subject}\n\n{body}'
    server.sendmail('myemail@mail.com', 'myemail@mail.com', msg=message.encode('utf-8'))

check_for_new_jobs(jobs_bg())

if len(new_jobs) > 0:
    send_me_mail()



