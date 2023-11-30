from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from generate_driver import get_chromedriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium_recaptcha import Recaptcha_Solver
import time


def initBrowser(query):
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
    solver = Recaptcha_Solver(driver=driver, debug=True)
    solved = solver.solve_recaptcha()
    if solved:
        html = driver.page_source
        driver.quit()
        return html
    else:
        print("Captcha not solved")
        driver.quit()
        return None


def getResults(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.find_all("div", class_="s-post-summary js-post-summary")


url = "https://stackoverflow.com/"

query = input("Enter your query: ")

initBrowser(query)

print(getResults())


# https://stackoverflow.com/questions/15182496


# class="s-post-summary js-post-summary"


# body --> container --> mainbar
# --> flush-left js-search-results
# --> js-post-summaries --> data-post-id
