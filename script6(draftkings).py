from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date
import pandas as pd

caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Set the path to your web driver executable (e.g., chromedriver)
driver_path = 'path_to_chromedriver.exe'

# Initialize a Chrome driver
driver = webdriver.Chrome()

# Open the URL
url = 'https://sportsbook.draftkings.com/nba-player-props?wpsrc=Organic%20Search&wpaffn=Google&wpkw=https%3A%2F%2Fsportsbook.draftkings.com%2Fnba-player-props&wpcn=nba-player-props'
driver.get(url)

# Wait for a few seconds to allow the page to load
driver.implicitly_wait(12)
#define the lists for each stat that we want to record
players = []
lines = []
probabilities = []
probabilities_overs = []
probabilities_unders = []

today = date.today()

player_name_elements = driver.find_elements(By.CLASS_NAME, "sportsbook-row-name")
for element in player_name_elements:
    player_name = element.text
    if player_name:
        players.append(player_name)

overs_elements = driver.find_elements(By.CLASS_NAME, 'sportsbook-outcome-cell__line')
for element in overs_elements:
    over_line = element.text
    if over_line:
        lines.append(over_line)

probability_element = driver.find_elements(By.CLASS_NAME, 'sportsbook-outcome-cell__element')
for element in probability_element:
    probability = element.text
    if probability:
        probabilities.append(probability)

while probabilities:
    probabilities_overs.append(probabilities[0])
    probabilities_unders.append(probabilities[1])
    probabilities = probabilities[2:]
lines = [lines[i] for i in range(len(lines)) if i % 2 == 0]

print(len(players))
print(len(lines))
print(len(probabilities_overs))
print(len(probabilities_unders))






data = {'players': players, 'line': lines, 'over': probabilities_overs, 'under': probabilities_unders}
df = pd.DataFrame(data)
print(df)

df.to_csv(f'{today} DraftKings Player Props.csv', index=False)

driver.quit
