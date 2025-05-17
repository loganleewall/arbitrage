# from selenium import webdriver
# from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)



# website = 'https://www.adamchoi.co.uk/overs/detailed'
# path = '/Users/loganwall/Desktop/chromedriver-mac-x64/chromedriver'
# driver = webdriver.Chrome(options=options)
# driver.get(website)

# all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
# all_matches_button.click()

# matches = driver.find_elements(By.TAG_NAME, 'tr')

# date = []
# home_team = []
# score = []
# away_team = []

# for match in matches: 
#     cells = match.find_elements(By.TAG_NAME, 'td')
#     date.append(cells[1].text)
#     home_team.append(cells[2].text)
#     print(cells[1].text)
#     score.append(cells[3].text)
#     away_team.append(cells[4].text)

# print(date)




from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = '/Users/loganwall/Desktop/chromedriver-mac-x64/chromedriver'
driver = webdriver.Chrome(options=options)
driver.get(website)

all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button.click()

#selecting from the drop-down menu

dropdown = Select(driver.find_element(By.ID, 'country'))
dropdown.select_by_visible_text("Italy")
league_dropdown = Select(driver.find_element(By.ID, 'league'))
league_dropdown.select_by_visible_text("Serie B")
year_dropdown = Select(driver.find_element(By.ID, 'season'))
year_dropdown.select_by_visible_text("18/19")

# Use the correct tag name 'tr' instead of a full XPath
matches = driver.find_elements(By.TAG_NAME, 'tr')

date = []
home_team = []
score = []
away_team = []

for match in matches:  # Skip the first row (header row)
    cells = match.find_elements(By.TAG_NAME, 'td')
    date.append(cells[0].text)
    home_team.append(cells[1].text)
    print(cells[1].text)
    score.append(cells[2].text)
    away_team.append(cells[3].text)
#driver.quit()

#exports the information to a csv file
df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team})
df.to_csv('football_data.csv', index=False)
print(df)

