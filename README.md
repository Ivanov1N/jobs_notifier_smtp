# Jobs Notificator

Web scraping script for jobs.bg, combined with SMTP and AWS for automation.

## Description

This is a script that performs web scraping on a job site based on predefined conditions (Python internship listings) and sends me notifications via SMTP when a new job is added.
To automate the script, I deployed it on AWS EC2 instance and scheduled it with Cron to run at the end of each workday.

## Dependencies

* Python 3, requests, BeautifulSoup4, smtplib

## Executing/testing the program

* Change lines 45, 47 and 51 by adding your own mail and password information
* Optional - Set up AWS instance and crontab to schedule it's execution
