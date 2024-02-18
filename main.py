import os
import json
import random
import string
import atexit
from faker import Faker
from selenium import webdriver
import time
import tkinter as tk
from tkinter import Label, Spinbox, Text, Button, messagebox, ttk

SEARCH_DATA_FILE = "search_data.json"
fake = Faker()

def generate_default_search_data():
    random_search_texts = [fake.word() for _ in range(20)]

    default_search_data = {"search_texts": random_search_texts}

    with open(SEARCH_DATA_FILE, "w") as json_file:
        json.dump(default_search_data, json_file, indent=2)

def delete_search_data_file():
    if os.path.exists(SEARCH_DATA_FILE):
        os.remove(SEARCH_DATA_FILE)

# Register the delete_search_data_file function to be called on script exit
atexit.register(delete_search_data_file)

def update_sleep_duration(event=None):
    selected_quality = network_quality_combobox.get()
    if selected_quality == "Good":
        sleep_duration_label.config(text=f"Timeout of 4 seconds will be added on searching the next text")
    elif selected_quality == "Moderate":
        sleep_duration_label.config(text=f"Timeout of 6 seconds will be added on searching the next text")
    elif selected_quality == "Poor":
        sleep_duration_label.config(text=f"Timeout of 10 seconds will be added on searching the next text")

def automate_edge(sleep_timer, search_texts, window_size=(800, 600), network_quality="Good"):
    # Set up Edge WebDriver
    options = webdriver.EdgeOptions()
    # options.use_chromium = True
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

def execute_script():
    # Get user input values
    sleep_timer = float(sleep_spinbox.get())
    network_quality = network_quality_combobox.get()

    # Read search texts from the Text widget
    user_search_texts = search_texts_entry.get("1.0", "end-1c").split(',')

    # Validate input
    if sleep_timer < 1.5:
        messagebox.showerror("Error", "Sleep timer should be greater than or equal to 1.5")
        return

    # Execute the script with user-defined values
    automate_edge(sleep_timer, user_search_texts, network_quality=network_quality)
    messagebox.showinfo("Success", "Script executed successfully!")

# Check if search_data.json exists, if not, generate it
if not os.path.exists(SEARCH_DATA_FILE):
    generate_default_search_data()

# Create the GUI window
root = tk.Tk()
root.title("Microsoft Rewards Automation")

# Set background color
root.configure(bg="#f0f0f0")

# Label and Spinbox for Sleep Timer
Label(root, text="Wait Time on Searched Topic (seconds):", bg="#f0f0f0").pack(pady=5)
sleep_spinbox = Spinbox(root, from_=1.5, to=60, increment=0.5, width=5, state="readonly")
sleep_spinbox.pack(pady=5)

# Label and Text for Search Texts
Label(root, text="Search Texts (comma-separated):", bg="#f0f0f0").pack(pady=5)
search_texts_entry = Text(root, height=6, width=60)
search_texts_entry.pack(pady=5)

# Display predefined search texts in the Text widget
with open('search_data.json') as json_file:
    data = json.load(json_file)
    predefined_search_texts = data.get('search_texts', [])
    search_texts_entry.insert("1.0", ",\n".join(predefined_search_texts))

# Dropdown selection box for Network Quality
Label(root, text="Network Quality:", bg="#f0f0f0").pack(pady=5)
network_quality_combobox = ttk.Combobox(root, values=["Good", "Moderate", "Poor"], state="readonly")
network_quality_combobox.set("Good")
network_quality_combobox.pack(pady=5)

# Label to display sleep duration dynamically
sleep_duration_label = Label(root, text="Timeout of 4 seconds will be added on searching the next text", bg="#f0f0f0")
sleep_duration_label.pack(pady=5)

# Bind the <<ComboboxSelected>> event to the update_sleep_duration function
network_quality_combobox.bind("<<ComboboxSelected>>", update_sleep_duration)

# Execute Button
execute_button = Button(root, text="Execute Script", command=execute_script, bg="#4CAF50", fg="white")
execute_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
