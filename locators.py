from selenium.webdriver.common.by import By


class Locators:
    man_button = (By.ID, 'ui-id-5')
    product_link = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[2]/div[3]/div/div/ol/li[1]/div/div/strong/a')
    add_to_cart_link = (By.XPATH, '//*[@id="product-addtocart-button"]')
    text_error = (By.XPATH, '//*[@id="super_attribute[93]-error"]')
