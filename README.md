# Jobs Notificator

Web scraping script for jobs.bg, combined with SMTP and AWS for automation.

## Description

This is a script that scrapes a job site by predefined conditions (Python internsip listings) and notifies me (via SMTP) when a new job is added. 
For the automation of the script I deployed it on AWS EC2 instance and scheduled it with Cron to run it at the end of every work day.

## Dependencies

* Python 3, requests, pandas, BeautifulSoup4

## Executing/testing the program

* Change lines 45, 47 and 51 by adding your own mail and password information
* Optional - Set up AWS instance and crontab to schedule the script execution
