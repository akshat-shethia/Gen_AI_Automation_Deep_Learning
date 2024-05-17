from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

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
    driver.get("https://automated.pythonanywhere.com/")
    return driver


def main():
    driver = get_driver()
    text_extracted = driver.find_element(
        By.XPATH, "//body/div[@class='container']//h1[@class='animated fadeIn mb-4']")
    return text_extracted.text


if __name__ == "__main__":
    print(main())
