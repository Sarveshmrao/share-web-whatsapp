from selenium import webdriver
from time import sleep
import sys
import os

sessionFileName = "00"

if len(sys.argv) == 2:
    sessionFileName = sys.argv[1]

session = None

possible_paths = [os.path.join("sessions", sessionFileName), sessionFileName]
possibleSessionFilePath = ""
for path in possible_paths:
    if os.path.exists(path):
        possibleSessionFilePath = path

if possibleSessionFilePath == "":
    raise IOError('"' + sessionFileName + '" is not exist.')

with open(possibleSessionFilePath, "r", encoding="utf-8") as sessionFile:
    try:
        session = eval(sessionFile.read())
    except:
        raise IOError('"' + possibleSessionFilePath + '" is invalid file.')

driver = webdriver.Chrome("./chromedriver")

driver.get("https://web.whatsapp.com/")

sleep(1)

print("Injecting session...")

driver.execute_script(
    """
var keys = Object.keys(arguments[0]);
var values = Object.values(arguments[0]);
for(i=0;i<keys.length;++i) window.localStorage.setItem(keys[i], values[i]);
""",
    session,
)

driver.refresh()
input("Enter any key to exit.")
driver.close()
