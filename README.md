# Basic webscraper template


## Details about files

---

## geckodriver.exe | geckodriver

Keep this file in local directory when using scraper on windows. If you're using a linux system, make sure to include geckodriver in PATH variable. Downloaded from [here](https://github.com/mozilla/geckodriver/releases)

Note: geckodriver.exe is for windows, and geckodriver (no extension) is for Linux

## [BasicSpider.py](https://github.com/aziznal/basic-web-scraper/blob/master/BasicSpider.py)

Use this as the superclass for your own project's spider

This Spider can do basic things like goto a url, scroll down the page in different ways, refresh the page, etc..

It acts as an interface to _**selenium.webdriver**_ to make setting up a project easier

## custom_exceptions.py

Copy alongside BasicSpider.py, add any custom exceptions to this file.

## package.json | package-lock.json
used to install dependencies related to testing and its related workflows. not needed for the spider to function.

## start_local_server.py
used for testing. optional.

## tests.py
this is where all the tests for the scraper are done. optional.

## mock_webpage
used for testing. optional. can be used as a simple demo.
