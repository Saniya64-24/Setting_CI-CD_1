
import pytest

from Core.driver_factory import DriverFactory
from config.config import BASE_URL


@pytest.fixture
def driver():

    driver = DriverFactory.create_driver()

    driver.get(BASE_URL)
    driver.maximize_window()

    yield driver

    driver.quit()
