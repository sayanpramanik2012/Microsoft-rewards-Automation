# automation.py

from selenium import webdriver
import time
from tkinter import messagebox
from selenium.webdriver.common.by import By
from constants import BING_SEARCH_URL, REWARDS_URL

def open_rewards_site(network_quality, sleep_timer):
    try:
        # Set up Edge WebDriver
        options = webdriver.EdgeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Edge(options=options)

        # Open Bing Rewards site in a new tab
        driver.execute_script("window.open('', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(REWARDS_URL)

        # Wait for the page to load
        if network_quality == "Poor":
            time.sleep(10)
        elif network_quality == "Moderate":
            time.sleep(8)
        elif network_quality == "Good":
            time.sleep(5)

        # Fetch and log all links on the page
        links = driver.find_elements(By.TAG_NAME, "a")
        filtered_links = [href for link in links if (href := link.get_attribute("href")) is not None and "Rewards" in href]

        # Print or use the filtered links as needed
        for link in filtered_links:
            print(link)
            # Open link in a new tab
            driver.execute_script("window.open('', '_blank');")
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(link)

            # Wait for n seconds
            time.sleep(sleep_timer+1)

            # Close the tab
            driver.close()

            # Switch back to the main tab
            driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def automate_edge(sleep_timer, search_texts, window_size=(800, 600), network_quality="Good", open_activities=True):
    try:
         # Set up Edge WebDriver
        options = webdriver.EdgeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Edge(options=options)

        # Set the window size
        driver.set_window_size(*window_size)

        for search_text in search_texts:
            # Open a new tab
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])

            # Open Bing search engine
            driver.get(BING_SEARCH_URL)
            # Adjust sleep duration based on network quality
            if network_quality == "Poor":
                time.sleep(10)
            elif network_quality == "Moderate":
                time.sleep(6)
            elif network_quality == "Good":
                time.sleep(4)

            # Perform the search
            search_box = driver.find_element("name", "q")
            search_box.send_keys(search_text)
            search_box.submit()

            # Wait for the specified time
            time.sleep(sleep_timer)

        # Close the original tab
        driver.switch_to.window(driver.window_handles[0])
        driver.close()

        # Open Bing Rewards site if checkbox is ticked
        if open_activities:
            open_rewards_site(network_quality,sleep_timer)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
