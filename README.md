# Microsoft-rewards-Automation (Education Purpose Only)

## Overview

This Python script automates web interactions using the Selenium library. It opens the Microsoft Edge browser, performs searches on Bing, and automates the process in a loop based on user-defined parameters.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)

## Prerequisites

Before running the script, ensure you have the following installed:

- [Python](https://www.python.org/) (version 3.6 or higher)
- [Microsoft Edge](https://www.microsoft.com/en-us/edge) browser
- [WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) for Microsoft Edge

## Installation 
One Click Install, Executable available in Release
1. Clone the repository:

    ```bash
    git clone https://github.com/sayanpramanik2012/Microsoft-rewards-Automation.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Microsoft-rewards-Automation

    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the script, execute the following command:

```bash
python main.py
```
This will open a GUI window with input fields for sleep timer and search texts, allowing users to interact with the script more convenientlyafter clicking execute it will open the Microsoft Edge browser, perform searches on Bing, and close the tabs based on the specified parameters.

## Configuration
Edit the search_data.json file to customize the search texts used by the script. Additionally, you can adjust the sleep timer and other parameters directly in the script.
