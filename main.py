from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import tkinter as tk
from tkinter import Label, Spinbox, Text, Button, messagebox,ttk

def automate_edge(sleep_timer, search_texts,window_size=(800, 600),network_quality="Good"):
    # Set up Edge WebDriver
    options = webdriver.EdgeOptions()
    options.use_chromium = True
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
        driver.get("https://www.bing.com")
        # Adjust sleep duration based on network quality
        if network_quality == "Poor":
            print("POOR")
            time.sleep(15)
        elif network_quality == "Moderate":
            time.sleep(10)
        elif network_quality == "Good":
            time.sleep(3)

        # Perform the search
        search_box = driver.find_element("name", "q")
        search_box.send_keys(search_text)
        search_box.submit()

        # Wait for the specified time
        time.sleep(sleep_timer)

    # Close the original tab
    driver.switch_to.window(driver.window_handles[0])
    driver.close()

def execute_script():
    # Get user input values
    sleep_timer = float(sleep_spinbox.get())
    network_quality = network_quality_combobox.get()

    # Read search texts from the Text widget
    user_search_texts = search_texts_entry.get("1.0", "end-1c").split(',')

    # Validate input
    if sleep_timer <= 0.4:
        messagebox.showerror("Error", "Sleep timer should be greater than 0.4")
        return

    # Execute the script with user-defined values
    automate_edge(sleep_timer, user_search_texts, network_quality=network_quality)
    messagebox.showinfo("Success", "Script executed successfully!")

# Create the GUI window
root = tk.Tk()
root.title("Web Automation Script")

# Label and Spinbox for Sleep Timer
Label(root, text="Sleep Timer (seconds):").pack(pady=5)
sleep_spinbox = Spinbox(root, from_=0.5, to=60, increment=0.5, width=5)
sleep_spinbox.pack(pady=5)

# Label and Text for Search Texts
Label(root, text="Search Texts (comma-separated):").pack(pady=5)
search_texts_entry = Text(root, height=6, width=60)
search_texts_entry.pack(pady=5)

# Display predefined search texts in the Text widget
with open('search_data.json') as json_file:
    data = json.load(json_file)
    predefined_search_texts = data.get('search_texts', [])
    search_texts_entry.insert("1.0", ",\n".join(predefined_search_texts))

# Dropdown selection box for Network Quality
Label(root, text="Network Quality:").pack(pady=5)
network_quality_combobox = ttk.Combobox(root, values=["Good", "Moderate", "Poor"])
network_quality_combobox.set("Good")
network_quality_combobox.pack(pady=5)

# Execute Button
execute_button = Button(root, text="Execute Script", command=execute_script)
execute_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
