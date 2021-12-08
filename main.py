from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

#Setup your unique job search URL for LinkedIn
URL = "https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1%2C2&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom"
EMAIL = YOUR EMAIL HERE
PASSWORD = YOUR PASSWOED
PHONE = YOUR PHONE NUMBER

#Download Selenium to your PC
serv = Service("C:\Development\chromedriver.exe")

driver = webdriver.Chrome(service=serv)

driver.get(URL)

#Login to LinkedIn
sign_in_button = driver.find_element(By.CSS_SELECTOR, ".nav__cta-container .nav__button-secondary")
sign_in_button.click()

username = driver.find_element(By.CSS_SELECTOR, "#username")
username.send_keys(EMAIL)

password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys(PASSWORD)

log_in_button = driver.find_element(By.CSS_SELECTOR, ".btn__primary--large.from__button--floating")
log_in_button.click()

#Apply for Jobs

time.sleep(5)

all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
print(all_listings)
for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        # If phone field is empty, then fill your phone number.
        # phone = driver.find_element(By.CSS_SELECTOR, ".fb-single-line-text__input")
        # if phone.text == "":
        #     phone.send_keys(PHONE)

        submit_button = driver.find_element(By.CSS_SELECTOR, "div.ph5.pv4 button.artdeco-button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.text == "Next":
            close_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--circle")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__actionbar .artdeco-button--primary")
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()