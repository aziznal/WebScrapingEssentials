# Basic webscraper template

The highlight of this repo is _**[BaseSpider.py](https://github.com/aziznal/WebScrapingEssentials/blob/master/BaseSpider.py)**_

## Details about files

---

## geckodriver.exe | geckodriver

Keep this file in local directory when using scraper on windows. If you're using a linux system, make sure to include geckodriver in PATH variable. Downloaded from [here](https://github.com/mozilla/geckodriver/releases)

Note: geckodriver.exe is for windows, and geckodriver (no extension) is for Linux

## [BaseSpider.py](https://github.com/aziznal/WebScrapingEssentials/blob/master/BaseSpider.py)

Use this as the superclass for your own project's spider

This Spider can do basic things like goto a url, scroll down the page in different ways, refresh the page, etc..

It acts as an interface to _**selenium.webdriver**_ to make setting up a project easier

