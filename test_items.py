import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_add_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(30)
    button_cart = browser.find_elements(By.CSS_SELECTOR, '.btn-primary.btn-add-to-basket')
    assert len(button_cart) > 0, "No button 'add to cart' on this page!"

