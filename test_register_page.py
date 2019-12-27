from selenium.webdriver.common.by import By
from locators import MainPage
from locators import SearchPage

def test_register_fail(parametrize_browser):
    bro = parametrize_browser
    bro.maximize_window()
    link = bro.current_url + 'index.php?route=account/register'
    bro.get(link)
    bro.find_element(By.CLASS_NAME, "btn-primary").click()
    bro.find_element(By.CLASS_NAME, 'text-danger')
