# Basic webscraper template

The two important components of this repo are _**[BaseSpyder.py](https://github.com/aziznal/WebScrapingEssentials/blob/master/BaseSpyder.py)**_ and _**[EmailSender.py](https://github.com/aziznal/WebScrapingEssentials/blob/master/EmailSender.py)**_

## Details about files

---

## geckodriver.exe

Keep this file in local directory when using scraper on windows. If you're using a linux system, make sure to include geckodriver in PATH variable. Downloaded from [here](https://github.com/mozilla/geckodriver/releases)

Note: This driver is for **_Mozilla Firefox_**

## [BaseSpyder.py](https://github.com/aziznal/WebScrapingEssentials/blob/master/BaseSpyder.py)

Use this as the superclass for your own project's spyder

This Spyder can do basic things like goto a url, scroll down the page in different ways, refresh the page, etc..

It acts as an interface to _**selenium.webdriver**_ to make setting up a project easier

**_NOTE: parent dir must include email_settings.json. Alternatively pass settings as a parameter when instantiating a new object._**

## [EmailSender.py](https://github.com/aziznal/WebScrapingEssentials/blob/master/EmailSender.py)

Sends an email with an attachment. the email's body can be html or just plain text. Uses **_email.mime_**

**_NOTE: parent dir must include email_settings.json. Alternatively pass settings as a parameter when instantiating a new object._**
