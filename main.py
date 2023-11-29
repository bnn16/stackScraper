from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from generate_driver import get_chromedriver


def initBrowser(url, query):
    driver = get_chromedriver(use_proxy=True)
    driver.implicitly_wait(5)
    driver.get("https://stackoverflow.com/")
    driver.implicitly_wait(4)
    search_bar = (
        driver.find_element(By.TAG_NAME, "header")
        .find_element(By.CLASS_NAME, "s-topbar--container")
        .find_element(By.ID, "search")
        .find_element(By.TAG_NAME, "input")
    )
    search_bar.send_keys(query)
    driver.implicitly_wait(5)
    elements = driver.find_element(By.CLASS_NAME, "container")
    return elements.get_attribute("")


url = "https://stackoverflow.com/"

query = input("Enter your query: ")
# headers = {
#    "Accept-Encoding": "identity",
#    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0",
# }
# r = requests.get(url, headers=headers)

r = initBrowser(url, query)

# soup = BeautifulSoup(r.text, "html.parser")

print(r)
# body = soup.body.find("div", {"class": "container"})


# https://stackoverflow.com/questions/15182496


# class="s-post-summary js-post-summary"


# body --> container --> mainbar
# --> flush-left js-search-results
# --> js-post-summaries --> data-post-id
