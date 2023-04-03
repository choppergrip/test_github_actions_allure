import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_google_button_name():
    # Set up the webdriver
    driver = webdriver.Chrome()

    # Open Google
    driver.get("https://uk.yahoo.com/")

    # Find the search button and get its name
    button = driver.find_element(By.CSS_SELECTOR, "[name='agree']")

    # Check the name of the button
    assert button.text == "Accept all"

    # Close the webdriver
    driver.quit()
