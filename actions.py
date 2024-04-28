
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()


def driver_init():
    driver.get('https://magento.softwaretestingboard.com/')
    driver.maximize_window()


def click_on_man():
    driver.find_element(*Locators.man_button).click()

def click_on_product_link():
    driver.find_element(*Locators.product_link).click()

def click_on_add_to_cart_link():
    WebDriverWait(driver, 4).until(EC.visibility_of_element_located(Locators.add_to_cart_link))
    driver.find_element(*Locators.add_to_cart_link).click()

def check_text():
    WebDriverWait(driver, 4).until(EC.visibility_of_element_located(Locators.text_error))
    element = driver.find_element(*Locators.text_error)
    return element.text

