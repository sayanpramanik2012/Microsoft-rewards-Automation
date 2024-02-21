# ui.py

import tkinter as tk
from tkinter import Label, Spinbox, Text, Button, messagebox, ttk, Checkbutton
from data_handler import generate_default_search_data, delete_search_data_file, SEARCH_DATA_FILE
from automation import automate_edge
import json
import os

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Microsoft Rewards Automation")
        self.configure(bg="#f0f0f0")
        self.create_widgets()
        self.load_search_data()

    def create_widgets(self):
        if not os.path.exists(SEARCH_DATA_FILE):
            generate_default_search_data()
        Label(self, text="Wait Time on Searched Topic (seconds):", bg="#f0f0f0").pack(pady=5)
        self.sleep_spinbox = Spinbox(self, from_=1.5, to=60, increment=0.5, width=5, state="readonly")
        self.sleep_spinbox.pack(pady=5)

        Label(self, text="Search Texts (comma-separated):", bg="#f0f0f0").pack(pady=5)
        self.search_texts_entry = Text(self, height=6, width=60)
        self.search_texts_entry.pack(pady=5)

        self.activities_checkbox_var = tk.BooleanVar()
        Checkbutton(self, text="Claim points from Rewards Activities", variable=self.activities_checkbox_var, bg="#f0f0f0").pack(pady=5)

        Label(self, text="Network Quality:", bg="#f0f0f0").pack(pady=5)
        self.network_quality_combobox = ttk.Combobox(self, values=["Good", "Moderate", "Poor"], state="readonly")
        self.network_quality_combobox.set("Good")
        self.network_quality_combobox.pack(pady=5)
        self.network_quality_combobox.bind("<<ComboboxSelected>>", self.update_sleep_duration)

        self.sleep_duration_label = Label(self, text="Timeout of 4 seconds will be added on searching the next text", bg="#f0f0f0")
        self.sleep_duration_label.pack(pady=5)

        self.execute_button = Button(self, text="Execute Script", command=self.execute_script, bg="#4CAF50", fg="white")
        self.execute_button.pack(pady=10)

    def load_search_data(self):
        if os.path.exists(SEARCH_DATA_FILE):
            with open(SEARCH_DATA_FILE) as json_file:
                data = json.load(json_file)
                predefined_search_texts = data.get('search_texts', [])
                self.search_texts_entry.insert("1.0", ", ".join(predefined_search_texts))

    def update_sleep_duration(self, event=None):
        selected_quality = self.network_quality_combobox.get()
        if selected_quality == "Good":
            self.sleep_duration_label.config(text="Timeout of 4 seconds will be added on searching the next text")
        elif selected_quality == "Moderate":
            self.sleep_duration_label.config(text="Timeout of 6 seconds will be added on searching the next text")
        elif selected_quality == "Poor":
            self.sleep_duration_label.config(text="Timeout of 10 seconds will be added on searching the next text")

    def execute_script(self):
        sleep_timer = float(self.sleep_spinbox.get())
        network_quality = self.network_quality_combobox.get()
        open_activities = self.activities_checkbox_var.get()
        user_search_texts = self.search_texts_entry.get("1.0", "end-1c").split(',')

        if sleep_timer < 1.5:
            messagebox.showerror("Error", "Sleep timer should be greater than or equal to 1.5")
            return

        automate_edge(sleep_timer, user_search_texts, network_quality=network_quality, open_activities=open_activities)
        messagebox.showinfo("Success", "Script executed successfully!")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
