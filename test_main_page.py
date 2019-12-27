import random
from selenium.webdriver.common.by import By
from locators import MainPage
from locators import SearchPage
from locators import ShoppingCartPage


def test_search_product(parametrize_browser):
    bro = parametrize_browser
    bro.maximize_window()
    bro.find_element(By.CSS_SELECTOR, MainPage.MainPage.search_field).send_keys("iphone")
    bro.find_element(By.CSS_SELECTOR, MainPage.MainPage.search_button).click()
    bro.find_element(By.CSS_SELECTOR, SearchPage.SearchPage.product)


def test_go_to_shopping_cart(browser):
    bro = browser
    bro.maximize_window()
    bro.find_element(By.XPATH, MainPage.Header.cart_link).click()
    bro.find_element(By.CSS_SELECTOR, ShoppingCartPage.EmptyCart.continue_button).click()


# def test_go_to_product_category(browser):
# bro = browser
# bro.maximize_window()
# categories = bro.find_elements(By.XPATH, "//ul[@class='nav navbar-nav']//li[@class='dropdown']")
# num = random.randint(1, len(categories))
# bro.find_element(By.XPATH, f"//ul[@class='nav navbar-nav']//li[@class='dropdown'][{num}]").click()


def test_add_product_to_cart(browser):
    bro = browser
    num = random.randint(1, 4)
    bro.maximize_window()
    bro.find_element(By.CSS_SELECTOR, f".product-layout:nth-child({num})").find_element(By.CSS_SELECTOR,
                                                                                        "button:nth-child(1)").click()
    bro.find_element(By.CSS_SELECTOR, ".alert-success")


def test_add_product_to_wish_list(browser):
    bro = browser
    num = random.randint(1, 4)
    bro.maximize_window()
    bro.find_element(By.CSS_SELECTOR, f".product-layout:nth-child({num})").find_element(By.CSS_SELECTOR,
                                                                                        "button:nth-child(2)").click()
    bro.find_element(By.CSS_SELECTOR, ".alert-success")
# def test_go_to_checkout_page(browser):
