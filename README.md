[![Build Status](https://travis-ci.org/New-Jersey-Forest-Service/FIAPI.svg?branch=master)](https://travis-ci.org/New-Jersey-Forest-Service/FIAPI)

# FIAPI
Applications and Libraries for USDA Forest Service, FIA Program's EVALIDator


FIAPI provides batch reporting capabilities for EVALIDator queries using Python 2.7 or R. This library follows the protocol released by FIA detailing protocols for retreiving queries by building HTML strings directly (Miles 2015: https://apps.fs.usda.gov/fia/datamart/datamart_api_tutorials.html).

Python functionality is provided using the BeautifulSoup package (https://www.crummy.com/software/BeautifulSoup/), while the R version utilizes the library Rvest (https://github.com/hadley/rvest).

Use Case: By providing users with a standardized interface to access data, users can have the most up to date data pull without waiting for an MS Access DB to be released. {to be continued...}

## Installation Instructions for Mac
1. Install the latest version of Python 2.7. This can be installed from (https://www.python.org/downloads/release/python-2713/)
2. Next, install the library BeautifulSoup. The easiest way to install this is with pip. 
   - If you don't have pip, run **sudo easy_install pip** in your terminal
   - Then run **pip install BeautifulSoup**
3. Now clone this repository onto your computer.
   - Click the green button in the top right that says **Clone or download** and clone with whichever method your prefer.
   - Click the clipboard to copy the link to your clipboard
   - Then in you terminal type **git clone** and then paste the link.
   - Hit enter and the repository will be cloned onto your computer.
4. Navigate to the FIAPI/Python2x/TestImpl folder in the terminal.
5. In your terminal run **python FIATestRun05.py** and the test code will run.
6. In the same folder you should see 3 new html files, which are the html tables that have been retrieved.

## Installation Instructions for Windows
1. Install the latest version of Python 2.7. This can be installed from (https://www.python.org/downloads/release/python-2713/)
2. Next, install the library BeautifulSoup. This can be downloaded from (https://www.crummy.com/software/BeautifulSoup/bs4/download/4.6/).
   - After downloading BeautifulSoup, you need to install it. To install it open the command prompt and run **C:\Path\To\Python27\python.exe "C:\Path\To\BeautifulSoup\setup.py" install**. 
3. Now you need to clone the github repository.
   - On the FIAPI github page, click the green button and copy the https clone link.
   - Now download and install git for windows. It can be found here (https://git-for-windows.github.io/).
   - Once setup, run **git clone https://github.com/wzip/FIAPI.git** (this is the link you copied). 
4. After that, navigate to the FIAPI/Python2x directory and open the PyEVALIDator.py in notepad. Near the top add a **#** in front of **from BeautifulSoup import BeautifulSoup**, and get rid of the **#** in front of the **from bs4 import BeautifulSoup**. Lastly, save the file.
5. Now you can run the FIATestRun05.py to test out the library. In command prompt type **C:\Path\to\Python27\python.exe C:\Path\to\FIAPI\Python2x\TestImpl\FIATestRun05.py**

## Licensing
No code was modified in the "Requests" library for Python for use in this project.  Licensing for "Requests" may be found at: http://docs.python-requests.org/en/master/user/intro/#requests-license
