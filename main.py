from selenium import webdriver
import json
import time
import tkinter as tk
from tkinter import Label, Spinbox, Text, Button, messagebox

def automate_edge(sleep_timer, search_texts):
    # Set up Edge WebDriver
    options = webdriver.EdgeOptions()
    options.use_chromium = True
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Edge(options=options)

    for search_text in search_texts:
        # Open a new tab
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])

        # Open Bing search engine
        driver.get("https://www.bing.com")

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

    # Read search texts from the Text widget
    user_search_texts = search_texts_entry.get("1.0", "end-1c").split(',')

    # Validate input
    if sleep_timer <= 0:
        messagebox.showerror("Error", "Sleep timer should be greater than 0.")
        return

    # Execute the script with user-defined values
    automate_edge(sleep_timer, user_search_texts)
    messagebox.showinfo("Success", "Script executed successfully!")

# Create the GUI window
root = tk.Tk()
root.title("Web Automation Script")

# Label and Spinbox for Sleep Timer
Label(root, text="Sleep Timer (seconds):").pack(pady=5)
sleep_spinbox = Spinbox(root, from_=0.1, to=999.9, increment=0.1, width=5)
sleep_spinbox.pack(pady=5)

# Label and Text for Search Texts
Label(root, text="Search Texts (comma-separated):").pack(pady=5)
search_texts_entry = Text(root, height=4, width=50)
search_texts_entry.pack(pady=5)

# Display predefined search texts in the Text widget
with open('search_data.json') as json_file:
    data = json.load(json_file)
    predefined_search_texts = data.get('search_texts', [])
    search_texts_entry.insert("1.0", ",\n".join(predefined_search_texts))

# Execute Button
execute_button = Button(root, text="Execute Script", command=execute_script)
execute_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
