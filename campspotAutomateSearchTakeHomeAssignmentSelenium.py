"""
how to install selenium webdriver on macOS to use with Python:
pip3 install selenium
1st note: this project requires Python3 to be installed on your OS
2nd note: due to defects that I have logged, the automation script I have written will not work against the "developmentURL" variable until a developer fixes the issues with the inputs "Location", "Dates", and "Guests". For the purpose of this automation demo, the production variable "productionUrl" is used.
"""

import time
from selenium import webdriver


# creates a variable for time to print out when the script finishes
startTime = time.time()
# create variables for which environment you'd like to test in for the webdriver
developmentUrl = "https://development-9-prototype.campspot.com/"
productionUrl = "https://campspot.com/"

browser = webdriver.Chrome()
# change the variable within "browser.get()" to specify the dev or prod endpoint you'd like to test
browser.get(productionUrl)
# verify the correct Homepage is being loaded by checking the title in the Browser. Raises an exception if the title doesn't match the title string
try:
    get_title = browser.title
    assert "Campspot - Campgrounds, RV resorts, glamping, and more." in browser.title == get_title
    print("Title in Browser is Correct. Automation Script will Continue.")
except Exception as e:
    print("Title in Browser is Incorrect and URL needs to be checked. Ending automation script.", format(e))
    browser.close()
    browser.quit()
    

# added sleep method to allow the Homepage to fully load before the script beings to interact with elements on the page
time.sleep(5)

# using the xpath, this locates the Location field and types the searchable location "Lodi, California"
locationElement = browser.find_element("xpath", "/html/body/app-root/div/main/search/main/section[1]/div/div/div[2]/label/location-search/div/input").send_keys("Lodi, California")
time.sleep(5)

# after "Lodi, California" is entered into the text field, this clicks on the "Lodi, California" search result
lodiCaliforniaLocationElement = browser.find_element("xpath", "/html/body/app-root/div/main/search/main/section[1]/div/div/div[2]/label/location-search/div/ul/li/button").click()
time.sleep(2)

# using xpath create a clickable element for the "Check In" button to open the calendar view
checkInButton = browser.find_element("xpath", "/html/body/app-root/div/main/search/main/section[1]/div/div/div[2]/div[1]/aggredator/div/div/div[1]/button").click()
time.sleep(3)

# using xpath create a clickable element for the previous month button to validate a previous month can be viewed
datePastMonthButton = browser.find_element("xpath", "/html/body/app-root/div/main/search/main/section[1]/div/div/div[2]/div[1]/aggredator/div/div[2]/section[1]/button[1]").click()
time.sleep(1)

# using xpath create a clickable element for the future month button and return to the current month
dateFutureMonthButton = browser.find_element("xpath", "/html/body/app-root/div/main/search/main/section[1]/div/div/div[2]/div[1]/aggredator/div/div[2]/section[1]/button[2]").click()
time.sleep(1)

# using xpath go forward a month to validate a future month can be viewed
dateFutureMonthButton = browser.find_element("xpath", "/html/body/app-root/div/main/search/main/section[1]/div/div/div[2]/div[1]/aggredator/div/div[2]/section[1]/button[2]").click()
time.sleep(1)

# one last time return back to the current month to prepare for the date range to be selected by the customer
datePastMonthButton = browser.find_element("xpath", "/html/body/app-root/div/main/search/main/section[1]/div/div/div[2]/div[1]/aggredator/div/div[2]/section[1]/button[1]").click()
time.sleep(1)

# clicks on the first date for the reservation which is December 31st 2023
reservationStartingDateButton = browser.find_element("xpath", "/html/body/app-root/div/main/search/main/section[1]/div/div/div[2]/div[1]/aggredator/div/div[2]/section[2]/div[2]/table/tr[6]/td/button").click()
time.sleep(3)

# clicks on the end date for the reservation which is January 2nd 2024
reservationEndDateButton = browser.find_element("xpath", "/html/body/app-root/div/main/search/main/section[1]/div/div/div[2]/div[1]/aggredator/div/div[2]/section[2]/div[3]/table/tr[1]/td[3]/button").click()
time.sleep(1)

# opens the "Guests" input to validate the user could add/remove adults, children, and pets
guestsCheckOptionsArePresentButton = browser.find_element("xpath", "/html/body/app-root/div/main/search/main/section[1]/div/div/div[2]/div[2]/guest-categories-selectors/div/button").click()
time.sleep(2)

# this returns us from the "Guests" input popup so the "Search" button will be viewable and we get to check all prior inputs are entered correctly before clicking the "Search" button
guestsCheckOptionsArePresentButton = browser.find_element("xpath", "/html/body/app-root/div/main/search/main/section[1]/div/div/div[2]/div[2]/guest-categories-selectors/div/button").click()
time.sleep(2)

# clicks the "Search" button so we are taken to the results page given the inputs we've have selected
searchButton = browser.find_element("xpath", "/html/body/app-root/div/main/search/main/section[1]/div/div/div[2]/div[3]/button").click()

# added a longer sleep time so we could evaulate the search results and validate things such as geolocation results are present and based off of our "Location" input selection of "Lodi, California"
time.sleep(15)
# prints a string notifying the test the script has completed and how much time the script took to run
print("\nThe automation script completed with no issues and took ", (time.time() - startTime) / 60, " minutes to run.")

# closes the current window on which selenium is running the automated test but keeps the webdriver session active
browser.close()
# closes all browsers windows and ends the webdriver session
browser.quit()