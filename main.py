from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


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

# Initialize the Chrome driver with configured options
driver = webdriver.Chrome(
    service=Service(
        ChromeDriverManager().install()
    ),  # Automatically install and use appropriate ChromeDriver
    options=chrome_options,
)

# Navigate to the specified URL
print(f"Navigating to {url}...")  # Add print statement for debugging
driver.get(url)  # Send the navigation command to the browser
print("Navigation command sent.")  # Add print statement for debugging

# Wait for page to load completely
try:
    print("Waiting for page to load...")
    WebDriverWait(driver, 10).until(  # Wait up to 10 seconds for page to load
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )
    print(f"Page loaded: {driver.current_url}")  # Confirm final URL after loading
except Exception as e:
    print(f"Timeout or error waiting for page load: {e}")  # Log any timeout or errors
    print(f"Current URL: {driver.current_url}")  # Log where the browser ended up

# Find and wait for the username field to be visible
username_field = WebDriverWait(driver, 1).until(
    EC.visibility_of_element_located((By.ID, "userName"))
)

# Find and wait for the password field to be visible
password_field = WebDriverWait(driver, 1).until(
    EC.visibility_of_element_located((By.ID, "password"))
)

# Find the login button
login_button = driver.find_element(By.ID, "login")

# Enter credentials and login
username_field.send_keys("NM")  # Enter username
password_field.send_keys("Nm21Nm21@21")  # Enter password
driver.execute_script(
    "arguments[0].click();", login_button
)  # Click login button using JavaScript

# Keep browser open until user input
input("Press Enter to quit...")
driver.quit()  # Close the browser and end the session
