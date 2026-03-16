# # Import LoginPage class from pages folder
# from pages.login_page import LoginPage
# from config.config import BASE_URL
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Test case to verify login functionality
# def test_login_page(driver):

#     # Open the login page
#     driver.get(BASE_URL)

#     # Create object of LoginPage and pass driver instance
#     login_page = LoginPage(driver)

#     # Call login method with username and password
#     login_page.login("john@example.com", "User@123")

#     # Wait until some element on dashboard is visible (React apps may not change URL)
#      # Wait until Dashboard heading is visible
#     dashboard_heading = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Dashboard')]"))
#     )

#     # Assertion
#     assert dashboard_heading.is_displayed(), "Dashboard page did not load"