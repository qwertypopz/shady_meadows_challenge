# Tommy Nguyen's QA Project Challenge
The files and code within are designed to test the functionality of 
[Sauce Labs Retreat](https://automationintesting.online/ "Sauce Labs Retreat") through Firefox.

**Special Note**

The website changed on 2019.10.04 without warning. Reservation options were initially Single, Double, Family, and Suite.
They were changed to one Twin room and three Single rooms. Additionally, the rooms had unique characteristics such as
costs and amenities but are now all the same price offer similar amenities. In summary, the options became less refined
during the testing process so the scope of the project had to be adjusted accordingly. There has been no documentation
concerning reverting the website back to the state it was in before 2019.10.04. Documentation did state that the site
resets every ten minutes, however the reservation selections have not changed.
## Features
* QA Code is currently capable of the following:
    * Navigate and validate the Welcome Splash Page
    * Reserve a room for any amount of time within the 35-day window displayed by the website's calendar
        * Given a start date, the program will navigate to the specified calendar month to make the reservation
    * Contact the business with pre-determined information
* Python files have been organized by functions of the page and a common functions file, all of which will be expanded 
upon:
    * splash.py - Validation of the welcome splash page
    * reservation.py - Reservation functionality of the page including validation through the admin panel
    * contact.py - Contact the business owner including validation through the admin panel
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
```bash
pip install -U selenium
```
### Webdriverwrapper
Within the Windows Command Prompt, enter the following command:
```bash
pip install webdriverwrapper
```
### Firefox
Download and install the [Firefox web browser](https://www.mozilla.org/en-US/firefox/new/)
### Geckodriver
Download and unzip [geckodriver](https://github.com/mozilla/geckodriver/releases) into the same directory as the Python 
project if it does not already exist
## Functions
Commonly used functions have been compiled into each of the aforementioned python files, generally organized by their
use case. If the functionality applies to general use of the site, they will be organized into the common_functions.py 
file. These functions were created with the intent of saving time and energy when adding new functionality to the smoke 
test. Listed below are the functions that would be helpful when creating a new test. To use these functions, the 
developer must import the respective python file to their test.

**splash.validate(log)**
* Location
    * splash.py
* Parameters
    * log: Utilizes logging functionality for testing and diagnostic purposes
* Summary
    * Validates each page of the welcome splash page before closing the browser
    
**reservation.action(args, log)**
* Location
    * reservation.py
* Parameters
    * args: This is a dictionary variable with the following key value pairs:
        * room: String variable denoting type of reservation ('Single', 'Double', 'Family', 'Suite')
        * start_date: datetime variable stating reservation start date Can be defined by datetime.datetime(YYYY, MM, DD)
        * duration: integer variable stating duration of reservation in days
    * log: Utilizes logging functionality for testing and diagnostic purposes
* Summary
    * The main user-side function of the website. Developers are able to emulate user behavior in making a reservation
    by passing in the required parameters. The function itself enters dummy personal information to complete the
    reservation form before submission.

**contact.action(log)**
* Location
    * contact.py
* Parameters
    * log: Utilizes logging functionality for testing and diagnostic purposes.
* Summary
    * Fills out contact form with pre-determined information and then validates through the admin panel

**common_functions.admin_login(driver, log)**
* Location
    * common_functions.py
* Parameters
    * driver: Allows the program to utilize the browser in the same manner a user would.
    * log: Utilizes logging functionality for testing and diagnostic purposes.
* Summary
    * Logs into the back end of the website for tasks specific to website administrators such as records, business
    queries, and reservations.

**common_functions.navigate_calendar(start_date, driver, log)**
* Location
    * common_functions.py
* Parameters
    * start_date: datetime variable marking the starting date of the reservation
    * driver: Allows the program to utilize the browser in the same manner a user would.
    * log: Utilizes logging functionality for testing and diagnostic purposes
* Summary
    * The website opens up on the current month's calendar. If the test case requires a starting date further in the 
    future or past, then this function will navigate through the calendar until the proper calendar month is displayed.

**common_functions.navigate_to_main(driver, log)**
* Location
    * common_functions.py
* Parameters
    * driver: Allows the program to utilize the browser in the same manner a user would
    * log: Utilizes logging functionality for testing and diagnostic purposes
* Summary
    * Navigates to the main page

**common_functions.setup_driver(log)**
* Location
    * common_functions.py
* Parameters
    * log: Utilizes logging functionality for testing and diagnostic purposes
* Summary
    * This is a necessary function if the test requires any action to be done through a web browser.

**common_functions.setup_log()**
* Location
    * common_functions.py
* Summary
    * Required to incorporate logging functionality in code.

**common_functions.skip_splash(driver, log)**
* Location
    * common_functions.py
* Parameters
    * driver: Allows the program to utilize the browser in the same manner a user would
    * log: Utilizes logging functionality for testing and diagnostic purposes
* Summary
    * When first navigating to the main page, the user would typically encounter a welcome splash page, this function
    would quickly navigate through the panels and close the splash page to continue onto the main page.
