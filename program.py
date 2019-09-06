from selenium import webdriver
import time
from datetime import datetime, timedelta, time as datetimeTime
import random

accounts = [
# Not to be published
]

SEVEN_AM = datetimeTime(7,0,0)
ELEVEN_PM = datetimeTime(23,0,0)

def attemptToVote(account):
  num = random.randint(0,100)
  if(num < 133): 
    try: 
      options = webdriver.ChromeOptions()
      options.add_argument('--headless')
      website = webdriver.Chrome("/Users/connoringlis/Downloads/ChromeDriver/chromedriver", options=options)
      time.sleep(4)
      website.get("https://embed-572075.secondstreetapp.com/embed/80cea25e-f0f5-4856-a7e6-b9fee20d21c0/gallery/159284152/")
      time.sleep(4)
      website.execute_script("window.localStorage.setItem('SS_572075_accessToken','{}')".format(account["accessToken"]))
      time.sleep(4)
      website.get("https://embed-572075.secondstreetapp.com/embed/80cea25e-f0f5-4856-a7e6-b9fee20d21c0/gallery/159284152/")
    except:
      print("Could not connect to website")
      website.quit()
      return
    try:
      time.sleep(10)
      votedSymbol = website.find_element_by_class_name("entry-voted-for")
      time.sleep(2)
      print(account["Name"], "alreadyVoted")
      website.quit()
      time.sleep(random.randint(2, 60))
      return
    except:
      voteButton = website.find_element_by_class_name("vote-button")
      time.sleep(3)
      voteButton.click()
      time.sleep(6)
      print("------------ ",account["Name"], "voted at", datetime.now().strftime("%H:%M %p"),"! ------------")
      website.quit()
      time.sleep(random.randint(2,60))
  

while True:
  if(datetime.now().time() > SEVEN_AM and datetime.now().time() < ELEVEN_PM):
    print("")
    for account in accounts:
      print(account["Name"])
      attemptToVote(account)
      time.sleep(2)
      
  time.sleep(random.randint(120,240))

