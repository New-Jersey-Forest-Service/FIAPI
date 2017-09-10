# FIAPI
Applications and Libraries for USDA Forest Service, FIA Program's EVALIDator


FIAPI provides webscraping capabilities for EVALIDator queries using Python 2.7 or R. This library follows the protocol released by FIA detailing protocols for retreiving queries by building HTML strings directly (Miles 2015).

Python functionality is provided using the BeautifulSoup package (https://www.crummy.com/software/BeautifulSoup/), while the R version utilizes the library Rvest (https://github.com/hadley/rvest).

Use Case: By providing users with a standardized interface to access data, users can have the most up to date data pull without waiting for an MS Access DB to be released. {to be continued...}

## Installation Instructions for Mac
1. Install the latest version of Python 2.7. This can be installed from (https://www.python.org/downloads/release/python-2713/)
2. Next, install the library BeautifulSoup. The easiest way to install this is with pip. 
   -If you don't have pip, run **sudo easy_install pip** in your terminal.
    
    -Then run **pip install BeautifulSoup**
    
3. Now clone this repository onto your computer.
