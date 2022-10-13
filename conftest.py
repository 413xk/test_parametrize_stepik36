import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


supported_browsers = {
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox
}


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose your browser: chrome or firefox')
    parser.addoption('--language', action='store', default='ru',
                     help='Choose language')



@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    if browser_name in supported_browsers:
        print(f'\nstart {browser_name} browser for test')
        browser = supported_browsers.get(browser_name)(options=options)
    else:
        joined_browsers = ', '.join(supported_browsers.keys())
        raise pytest.UsageError(f"--browser_name is invalid, supported browsers: {joined_browsers}")

    yield browser
    print("\nquit browser..")
    browser.quit()