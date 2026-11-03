import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

VEZBAONICA_URL = os.getenv("VEZBAONICA_URL", "https://nevenaamilenkovic.github.io/OTS-Selenium-vezbe/")


@pytest.fixture(scope="session")
def vezbaonica_url() -> str:
    return VEZBAONICA_URL


@pytest.fixture
def driver():
    opcije = Options()
    opcije.add_argument("--window-size=1200,800")
    driver = webdriver.Chrome(options=opcije)
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver: WebDriver) -> WebDriverWait:
    return WebDriverWait(driver, timeout=10)


# Svaki test koji trazi VERZIJU se izvrsava dva puta: v1 i v2.
@pytest.fixture(params=["v1", "v2"])
def verzija(request) -> str:
    return request.param


@pytest.fixture
def vezbaonica(driver: WebDriver, vezbaonica_url: str, verzija: str) -> WebDriver:
    url = vezbaonica_url.rstrip("/") + "/"
    if verzija == "v2":
        url += "#v2"
    driver.get(url)
    return driver