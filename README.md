# Tommy Nguyen's QA Project Challenge
The files and code within are designed to test the functionality of 
[Sauce Labs Retreat](https://automationintesting.online/ "Sauce Labs Retreat") through Firefox.
## Features
* QA Code is currently capable of the following:
    * Navigate and validate the Welcome Splash Page
    * Reserve a room for any amount of time within the 35-day window displayed by the website's calendar
        * Given a start date, the program will navigate to the specified calendar month to make the reservation
    * Contact the business with pre-determined information
* Python files have been organized by functions of the page and a common functions file which will be expanded upon:
    * splash.py - Welcome Splash Page
    * reservation_single.py - Reservation for the single room
    * reservation_double.py - Reservation for the double room
    * reservation_family.py - Reservation for the family room
    * reservation_suite.py - Reservation for the suite room
    * contact.py - Contact Business
    * common_functions.py - Common Functions
* Useful blocks of code have been compiled in the common_functions.py file to be used as needed during testing.
* Verbose documentation within code to assist the developer better understand the functionality and better utilize the 
existing code.
## Assumptions
This documentation assumes that the user is familiar with Python and is using a Windows machine with an IDE configured 
for Python projects
## Requirements
### Selenium
Within the Windows Command Prompt, enter the following command:
>pip install -U selenium
### Webdriverwrapper
Within the Windows Command Prompt, enter the following command:
>pip install webdriverwrapper
### Firefox
Download and install the [Firefox web browser](https://www.mozilla.org/en-US/firefox/new/)
### Geckodriver
Download and unzip [geckodriver](https://github.com/mozilla/geckodriver/releases) into the same directory as the Python 
project if it does not already exist
## Common Functions
