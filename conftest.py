import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default='en',
                     help="Choose lang")


@pytest.fixture(scope='function')
def driver(request):
    driver_lang = request.config.getoption("language")
    options = Options()
    if driver_lang == "es":
        options.add_experimental_option('prefs', {'intl.accept_languages': 'es'})
        driver = webdriver.Chrome(options=options)
    elif driver_lang == "en":
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})
        driver = webdriver.Chrome(options=options)
    elif driver_lang == 'ru':
        options.add_experimental_option('prefs', {'intl.accept_languages': 'ru'})
        driver = webdriver.Chrome(options=options)
    elif driver_lang == 'fr':
        options.add_experimental_option('prefs', {'intl.accept_languages': 'fr'})
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Chrome()
    yield driver
    driver.quit()


    