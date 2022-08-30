# Import required modules
from lxml import html
import requests
import pyautogui
import time  

# Request the page
page = requests.get('https://www.letras.mus.br/mc-carol/ar-condicionado/')
  
# Parsing the page
tree = html.fromstring(page.content)
  
# Get element using XPath
list_frases = tree.xpath(
    '//*[@id="js-lyric-cnt"]/article/div[2]/div[2]/p/text()')

time.sleep(1)

print(list_frases)
for line in list_frases:
    pyautogui.typewrite(line)
    pyautogui.press("enter")
    time.sleep(1)
