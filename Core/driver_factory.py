from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from config.config import BROWSER, EXECUTION_MODE, GRID_URL, HEADLESS_MODE

class DriverFactory:

    @staticmethod
    def create_driver():
        if EXECUTION_MODE == "remote":
            return DriverFactory._create_remote_driver()
        return DriverFactory._create_local_driver()

    @staticmethod
    def _create_local_driver():
        if BROWSER.lower() == "chrome":
            options = ChromeOptions()
            if HEADLESS_MODE:
                options.add_argument("--headless=new")  # Use new headless mode (better support)
                options.add_argument("--window-size=1920,1080")  # Explicitly set window size
            else:
                options.add_argument("--start-maximized")

            driver = webdriver.Chrome(options=options)

        elif BROWSER.lower() == "firefox":
            options = FirefoxOptions()
            if HEADLESS_MODE:
                options.add_argument("--headless")
                options.add_argument("--width=1920")
                options.add_argument("--height=1080")
            else:
                options.add_argument("--start-maximized")

            driver = webdriver.Firefox(options=options)

        else:
            raise Exception("Unsupported browser")

        # Fallback maximize (for non-headless mode)
        if not HEADLESS_MODE:
            driver.maximize_window()

        return driver

    @staticmethod
    def _create_remote_driver():
        if BROWSER.lower() == "chrome":
            options = ChromeOptions()
        elif BROWSER.lower() == "firefox":
            options = FirefoxOptions()
        else:
            raise Exception("Unsupported browser")

        if HEADLESS_MODE:
            options.add_argument("--headless=new")  # new headless mode
            options.add_argument("--window-size=1920,1080")
        else:
            options.add_argument("--start-maximized")

        driver = webdriver.Remote(
            command_executor=GRID_URL,
            options=options
        )

        if not HEADLESS_MODE:
            driver.maximize_window()

        return driver