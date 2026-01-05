from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

unsorted_advert_links = soup.select(selector=".property-card-link")
unsorted_advert_adresses = soup.select(selector=".Image-c11n-8-84-listing")
unsorted_advert_prices = soup.select(selector=".PropertyCardWrapper__StyledPriceLine")

advert_links = [tag.get("href") for tag in unsorted_advert_links]
advert_prices = [str(element.text).split("+")[0].split("/")[0] for element in unsorted_advert_prices]
advert_adresses = [re.sub(r"\s+", " ",str(tag.get("alt")).replace("|", "")).strip() for tag in unsorted_advert_adresses]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

""" for index in len(advert_links): """
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeOcvyV23TgDz0Y9wiRxLw3ehPV0-_CxecynFp1sA0NdNHxoQ/viewform")

for index in range(len(advert_adresses)):
    inputs = driver.find_elements(By.CSS_SELECTOR, "input.whsOnd.zHQkBf")
    inputs[0].send_keys(advert_adresses[index])
    inputs[1].send_keys(advert_prices[index])
    inputs[2].send_keys(advert_links[index])

    send_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and @aria-label='Submit']"))
    )
    send_button.click()

    link = wait.until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='https://docs.google.com/forms/d/e/1FAIpQLSeOcvyV23TgDz0Y9wiRxLw3ehPV0-_CxecynFp1sA0NdNHxoQ/viewform?usp=form_confirm']"))
    )
    link.click()

