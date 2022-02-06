[![Build Status](https://travis-ci.org/New-Jersey-Forest-Service/FIAPI.svg?branch=master)](https://travis-ci.org/New-Jersey-Forest-Service/FIAPI)
## Please be aware that this library is no longer being updated or maintained, due to changes in the FIA EVALIDator interface!
## The code from this project will remain avaialable so that those who find it useful may continue to use it.
# FIAPI
Applications and Libraries for USDA Forest Service, FIA Program's EVALIDator


FIAPI provides batch reporting capabilities for EVALIDator queries using Python 2.7. This library follows the protocol released by FIA detailing protocols for retreiving queries by building HTML strings directly (Miles 2015: https://apps.fs.usda.gov/fia/datamart/datamart_api_tutorials.html).

Python functionality is provided using the BeautifulSoup package (https://www.crummy.com/software/BeautifulSoup/), while the R version utilizes the library Rvest (https://github.com/hadley/rvest).

Use Case: By providing users with a standardized interface to access data, users can have the most up to date data pull without waiting for an MS Access DB to be released.

## Installation Instructions for Mac
1. Install the latest version of Python 2.7. This can be installed from (https://www.python.org/downloads/release/python-2713/)
2. Next, install the BeautifulSoup 4 and requests libraries. The easiest way to install these is with pip. 
   - If you don't have pip, run **sudo easy_install pip** in your terminal
   - Run **pip install bs4**
   - Run **pip install requests**
3. Now clone this repository onto your computer.
   - Click the green button in the top right that says **Clone or download** and clone with whichever method your prefer.
   - Click the clipboard to copy the link to your clipboard
   - Then in you terminal type **git clone** and then paste the link.
   - Hit enter and the repository will be cloned onto your computer.
4. Navigate to the FIAPI/Python2x/TestImpl folder in the terminal.
5. In your terminal run **python FIATestRun09.py** and the test code will run.
6. In the same folder you should see 3 new html files, which are the html tables that have been retrieved.

## Installation Instructions for Windows
1. Install the latest version of Python 2.7. This can be installed from (https://www.python.org/downloads/release/python-2713/)
2. Next, install the BeautifulSoup 4 and requests libraries. The easiest way to install these is with pip. 
   - locate a command prompt by searching in the start menu or seach box in Windows 10 for **cmd**
   - Right click on the item labeled **Command Prompt** and select "Run as administrator"
   - At the prompt type **pip install bs4** and hit "Enter"
   - At the prompt type **pip install requests** and hit "Enter"
3. Now you need to clone the github repository.
   - On the FIAPI github page, click the green button and copy the https clone link.
   - Now download and install git for windows. It can be found here (https://git-for-windows.github.io/).
   - Once setup, run **git clone https://github.com/wzip/FIAPI.git** (this is the link you copied). 
4. Now you can run the FIATestRun09.py to test out the library. In command prompt type **C:\Path\to\Python27\python.exe C:\Path\to\FIAPI\Python2x\TestImpl\FIATestRun09.py** It can also be run by editing FIATestRun09.py in Idle and selecting the "run" option (or pressing F5).

## Licensing
No code was modified in the "Requests" library for Python for use in this project.  Licensing for "Requests" may be found at: http://docs.python-requests.org/en/master/user/intro/#requests-license
