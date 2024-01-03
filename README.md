# campspotAutomationSeleniumPython
this project automated opening the campspot.com homepage via selenium and python, click on elements to pick a location, time & date, guests, and then view the results based off of these parameters. i included an option for choosing either the production URL or staging/development URL.

how to install selenium webdriver on macOS to use with Python:
pip3 install selenium

1st note: this project requires Python3 to be installed on your OS
2nd note: due to defects that I have logged, the automation script I have written will not work against the "developmentURL" variable until a developer fixes the issues with the inputs "Location", "Dates", and "Guests". For the purpose of this automation demo, the production variable "productionUrl" is used.
