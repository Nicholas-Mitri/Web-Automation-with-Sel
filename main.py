from curses import def_prog_mode
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class WebAutomation:
    def __init__(self):
        # Target URL for the login page
        url = "https://demoqa.com/login"

        # Configure Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
        chrome_options.add_argument("--window-size=1920,1080")  # Set window size
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
        chrome_options.add_argument(
            "--disable-dev-shm-usage"
        )  # Overcome limited resource problems
        chrome_options.add_argument(
            "--disable-search-engine-choice-screen"
        )  # Disable search engine choice dialog

        # Initialize the Chrome self.driver with configured options
        self.driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            ),  # Automatically install and use appropriate Chromeself.driver
            options=chrome_options,
        )

        # Navigate to the specified URL
        print(f"Navigating to {url}...")  # Add print statement for debugging
        self.driver.get(url)  # Send the navigation command to the browser
        print("Navigation command sent.")  # Add print statement for debugging

        # Wait for page to load completely
        try:
            print("Waiting for page to load...")
            WebDriverWait(
                self.driver, 10
            ).until(  # Wait up to 10 seconds for page to load
                lambda driver: driver.execute_script("return document.readyState")
                == "complete"
            )
            print(
                f"Page loaded: {self.driver.current_url}"
            )  # Confirm final URL after loading
        except Exception as e:
            print(
                f"Timeout or error waiting for page load: {e}"
            )  # Log any timeout or errors
            print(
                f"Current URL: {self.driver.current_url}"
            )  # Log where the browser ended up

    def login(self, username, password):
        # Find and wait for the username field to be visible
        username_field = WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.ID, "userName"))
        )

        # Find and wait for the password field to be visible
        password_field = WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )

        # Find the login button
        login_button = self.driver.find_element(By.ID, "login")

        # Enter credentials and login
        username_field.send_keys(username)  # Enter username
        password_field.send_keys(password)  # Enter password
        self.driver.execute_script(
            "arguments[0].click();", login_button
        )  # Click login button using JavaScript

    def submit_form(self):
        pass

    def close_browser(self):
        self.driver.quit()  # Close the browser and end the session


if __name__ == "__main__":
    web_automation = WebAutomation()
    web_automation.login("NM", "Nm21Nm21@21")
    web_automation.submit_form()
    input("")
    web_automation.close_browser()
