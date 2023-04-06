import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_google_button_name():
    # Set up the webdriver
    driver = webdriver.Remote(
        command_executor=f"http://{os.getenv('SELENIUM') or 'selenium'}:4444",
        desired_capabilities={
            "browserName": os.getenv('BROWSER'),
        })

    # Open Google
    driver.get("https://uk.yahoo.com/")

    # Find the search button and get its name
    button = driver.find_element(By.CSS_SELECTOR, "[name='agree']")

    # Check the name of the button
    assert button.text == "Accept all"

    # Close the webdriver
    driver.quit()
