from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest


# Ensure the path to chromedriver is correct
service = Service("C:\\chromedriver.exe")


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("no-sandbox")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")

    # Initialize the Chrome driver with service and options
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://automated.pythonanywhere.com/login/")
    return driver


class TestCase:
    @pytest.mark.check
    def test_extract_text(self):
        driver = get_driver()
        driver.implicitly_wait(2)
        time.sleep(2)

        username = driver.find_element(
            By.XPATH, "/html//input[@id='id_username']")
        username.send_keys("automated")

        password = driver.find_element(
            By.XPATH, "/html//input[@id='id_password']")
        password.send_keys("automatedautomated")

        login = driver.find_element(
            By.XPATH, "//body/div[@class='container']//form[@method='post']/button[@type='submit']")
        login.click()

        Welcome_automated = driver.find_element(
            By.XPATH, "//body//h1[@class='mt-5 text-center']")
        assert Welcome_automated.text == "Welcome automated"

        wait = WebDriverWait(driver, 10)
        temperature_extracted = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div[1]/h1[2]")))
        print(temperature_extracted.text)
