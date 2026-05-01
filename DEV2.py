from selenium import webdriver
from selenium.webdriver.common.by import By

# Start Chrome browser
driver = webdriver.Chrome()

# Open Google homepage
driver.get("https://www.facebook.com/")

# Inspect and locate search box element
search_box = driver.find_element(By.NAME, "q")

# Print confirmation
print("Search box element found:", search_box)

# Keep browser open until user input
input("Press Enter to close...")

# Close browser
driver.quit()