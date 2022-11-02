import pytest
from selenium import webdriver

from Library.configure import Configuration


@pytest.fixture(params=["chrome", "edge"])
def init_driver(request):
    browser = request.param

    if browser.lower() == "chrome":
        driver = webdriver.Chrome(executable_path=Configuration.CHROME_PATH)

    else:
        driver = webdriver.Edge(executable_path=Configuration.MSEDGE_PATH)

    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get(Configuration.URL)
    yield driver
    driver.close()
