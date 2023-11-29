from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from generate_driver import get_chromedriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium_recaptcha import Recaptcha_Solver
import time


def initBrowser(url, query):
    driver = get_chromedriver(use_proxy=True)
    driver.get("https://stackoverflow.com/")
    driver.maximize_window()
    search_bar = (
        driver.find_element(By.TAG_NAME, "header")
        .find_element(By.CLASS_NAME, "s-topbar--container")
        .find_element(By.ID, "search")
        .find_element(By.TAG_NAME, "input")
    )
    search_bar.send_keys(query)
    driver.implicitly_wait(5)
    search_bar.send_keys(Keys.ENTER)
    driver.implicitly_wait(5)
    solver = Recaptcha_Solver(driver=driver, debug=False)
    solver.solve_recaptcha()
    driver.implicitly_wait(5)
    elements = driver.find_elements(By.CLASS_NAME, "container")
    return elements


url = "https://stackoverflow.com/"

query = input("Enter your query: ")

r = initBrowser(url, query)

print(r)

soup = BeautifulSoup(r.text, "html.parser")

print(soup)


# https://stackoverflow.com/questions/15182496


# class="s-post-summary js-post-summary"


# body --> container --> mainbar
# --> flush-left js-search-results
# --> js-post-summaries --> data-post-id
