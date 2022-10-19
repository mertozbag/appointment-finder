import time
import telegram_send
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""
It`s a script to check and get appointment for driving license.
Webdriver version can be different depends on your browser version.
"""

# browser settings
options = webdriver.ChromeOptions()
options.headless = False
browser = webdriver.Chrome(options=options)
browser.set_window_size(1250, 850)
browser.maximize_window()



# main website
browser.get("https://telegov.njportal.com/njmvc/AppointmentWizard/12/130")
time.sleep(2)

while True:
    try:
        try:
            time.sleep(2)
            # to reach current month
            button_left = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div[2]/div/div"
                                                                                                 "/div/div[3]/div/div[1]/div/div/div/nav[1]/div[1]")))
            button_left.click()
            time.sleep(3)
        except:
            pass

        # days for appointment
        day1 = browser.find_element_by_xpath("/html/body/main/div/div[2]/div/div/div/div[3]"
                                             "/div/div[1]/div/div/div/div[3]/div[5]")
        day2 = browser.find_element_by_xpath("/html/body/main/div/div[2]/div/div/div/div[3]"
                                             "/div/div[1]/div/div/div/div[3]/div[6]")
        day3 = browser.find_element_by_xpath("/html/body/main/div/div[2]/div/div/div/div[3]"
                                             "/div/div[1]/div/div/div/div[3]/div[7]")



        day1_a = day1.get_attribute("class")
        day2_a = day2.get_attribute("class")
        day3_a = day3.get_attribute("class")




        # to check if day is available or not
        if not "pmu-disabled disabled pmu-button" in day1_a and\
                not "pmu-disabled pmu-today disabled pmu-button" in day1_a:
            # message to send via telegram if there`s any available appointment
            telegram_send.send(messages=["I found something for Real ID. Please check: "
                                         "https://telegov.njportal.com/njmvc/AppointmentWizard/12/130"])
            # screenshot to avoid false alert
            browser.save_screenshot("license_photo.png")
            with open("license_photo.png", "rb") as f:
                telegram_send.send(images=[f])
            time.sleep(15)
            telegram_send.send(messages=["I found something for Real ID. Please check: "
                                         "https://telegov.njportal.com/njmvc/AppointmentWizard/12/130"])
            time.sleep(360)
            # to clean browser and opening new session
            browser.quit()
            browser = webdriver.Chrome(options=options)
            browser.set_window_size(1250, 850)
            browser.maximize_window()
            browser.get("https://telegov.njportal.com/njmvc/AppointmentWizard/12/130")
            time.sleep(1)
        elif not "pmu-disabled disabled pmu-button" in day2_a and\
                not "pmu-disabled pmu-today disabled pmu-button" in day2_a:
            telegram_send.send(messages=["I found something for Real ID. Please check: "
                                         "https://telegov.njportal.com/njmvc/AppointmentWizard/12/130"])
            browser.save_screenshot("license_photo.png")
            with open("license_photo.png", "rb") as f:
                telegram_send.send(images=[f])
            time.sleep(15)
            telegram_send.send(messages=["I found something for Real ID. Please check: "
                                         "https://telegov.njportal.com/njmvc/AppointmentWizard/12/130"])
            time.sleep(360)
            browser.quit()
            browser = webdriver.Chrome(options=options)
            browser.set_window_size(1250, 850)
            browser.maximize_window()
            browser.get("https://telegov.njportal.com/njmvc/AppointmentWizard/12/130")
            time.sleep(1)
        elif not "pmu-disabled disabled pmu-button" in day3_a and\
                not "pmu-disabled pmu-today disabled pmu-button" in day3_a:
            telegram_send.send(messages=["I found something for Real ID. Please check: "
                                         "https://telegov.njportal.com/njmvc/AppointmentWizard/12/130"])
            browser.save_screenshot("license_photo.png.png")
            with open("license_photo.png", "rb") as f:
                telegram_send.send(images=[f])
            time.sleep(15)
            telegram_send.send(messages=["I found something for Real ID. Please check: "
                                         "https://telegov.njportal.com/njmvc/AppointmentWizard/12/130"])
            time.sleep(360)
            browser.quit()
            browser = webdriver.Chrome(options=options)
            browser.set_window_size(1250, 850)
            browser.maximize_window()
            browser.get("https://telegov.njportal.com/njmvc/AppointmentWizard/12/130")
            time.sleep(1)


        else:
            print("code block316")
            browser.quit()
            browser = webdriver.Chrome(options=options)
            browser.set_window_size(1250, 850)
            browser.maximize_window()
            browser.get("https://telegov.njportal.com/njmvc/AppointmentWizard/12/130")
            time.sleep(1)
    # in case there`s a problem on website
    except:
        browser.quit()
        browser = webdriver.Chrome(options=options)
        browser.set_window_size(1250, 850)
        browser.maximize_window()
        browser.get("https://telegov.njportal.com/njmvc/AppointmentWizard/12/130")
        time.sleep(1)

    # For the second town / same as above
    try:
        browser.quit()
        browser = webdriver.Chrome(options=options)
        browser.set_window_size(1250, 850)
        browser.maximize_window()
        browser.get("https://telegov.njportal.com/njmvc/AppointmentWizard/12/135")
    except:
        browser.get("https://telegov.njportal.com/njmvc/AppointmentWizard/12/135")
    time.sleep(1)

    try:
        try:
            time.sleep(2)
            button_left = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/main/div/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/nav[1]/div[1]")))
            button_left.click()
            time.sleep(3)
        except:
            pass

        day1 = browser.find_element_by_xpath("/html/body/main/div/div[2]/div/div/div/div[3]"
                                             "/div/div[1]/div/div/div/div[3]/div[5]")
        day2 = browser.find_element_by_xpath("/html/body/main/div/div[2]/div/div/div/div[3]"
                                             "/div/div[1]/div/div/div/div[3]/div[6]")
        day3 = browser.find_element_by_xpath("/html/body/main/div/div[2]/div/div/div/div[3]"
                                             "/div/div[1]/div/div/div/div[3]/div[7]")



        day1_a = day1.get_attribute("class")
        day2_a = day2.get_attribute("class")
        day3_a = day3.get_attribute("class")


        if not "pmu-disabled disabled pmu-button" in day1_a and \
                not "pmu-disabled pmu-today disabled pmu-button" in day1_a:
            telegram_send.send(messages=["I found something for Real ID. Please check: "
                                         "https://telegov.njportal.com/njmvc/AppointmentWizard/12/135"])
            browser.save_screenshot("license_photo.png")
            with open("license_photo.png", "rb") as f:
                telegram_send.send(images=[f])
            time.sleep(15)
            telegram_send.send(messages=["I found something for Real ID. Please check: "
                                         "https://telegov.njportal.com/njmvc/AppointmentWizard/12/135"])
            time.sleep(360)
            browser.quit()
            browser = webdriver.Chrome(options=options)
            browser.set_window_size(1250, 850)
            browser.maximize_window()
            browser.get("https://telegov.njportal.com/njmvc/AppointmentWizard/12/135")
            time.sleep(1)
        elif not "pmu-disabled disabled pmu-button" in day2_a and \
                not "pmu-disabled pmu-today disabled pmu-button" in day2_a:
            telegram_send.send(messages=["I found something for Real ID. Please check: "
                                         "https://telegov.njportal.com/njmvc/AppointmentWizard/12/135"])
            browser.save_screenshot("license_photo.png")
            with open("license_photo.png", "rb") as f:
                telegram_send.send(images=[f])
            time.sleep(15)
            telegram_send.send(messages=["I found something for Real ID. Please check: "
                                         "https://telegov.njportal.com/njmvc/AppointmentWizard/12/135"])
            time.sleep(360)
            browser.quit()
            browser = webdriver.Chrome(options=options)
            browser.set_window_size(1250, 850)
            browser.maximize_window()
            browser.get("https://telegov.njportal.com/njmvc/AppointmentWizard/12/135")
            time.sleep(1)

        elif not "pmu-disabled disabled pmu-button" in day3_a and \
                not "pmu-disabled pmu-today disabled pmu-button" in day3_a:
            telegram_send.send(messages=["I found something for Real ID. Please check: "
                                         "https://telegov.njportal.com/njmvc/AppointmentWizard/12/135"])
            browser.save_screenshot("license_photo.png")
            with open("license_photo.png", "rb") as f:
                telegram_send.send(images=[f])
            time.sleep(15)
            telegram_send.send(messages=["I found something for Real ID. Please check: "
                                         "https://telegov.njportal.com/njmvc/AppointmentWizard/12/135"])
            time.sleep(360)
            browser.quit()
            browser = webdriver.Chrome(options=options)
            browser.set_window_size(1250, 850)
            browser.maximize_window()
            browser.get("https://telegov.njportal.com/njmvc/AppointmentWizard/12/135")
            time.sleep(1)


        else:
            browser.quit()
            browser = webdriver.Chrome(options=options)
            browser.set_window_size(1250, 850)
            browser.maximize_window()
            browser.get("https://telegov.njportal.com/njmvc/AppointmentWizard/12/130")
            time.sleep(1)
    except:
        browser.quit()
        browser = webdriver.Chrome(options=options)
        browser.set_window_size(1250, 850)
        browser.maximize_window()
        browser.get("https://telegov.njportal.com/njmvc/AppointmentWizard/12/130")
        time.sleep(1)