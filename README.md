# TypeRacerBot

A bot that automates typing on [play.typeracer.com](https://play.typeracer.com/) for fun and educational purposes. This project uses Selenium to control a web browser and simulate typing at various speeds.

## 🚀 Features

* **Automated Typing**: Automatically types the text in a TypeRacer race.
* **Adjustable Speed**: Choose from a range of typing speeds, from a leisurely pace to superhuman speeds.
* **Multi-Browser Support**: Works with Google Chrome, Mozilla Firefox, and Microsoft Edge.
* **User-Friendly Interface**: A simple and colorful command-line interface to control the bot.

## ⚙️ How It Works

The bot is built with Python and utilizes the following libraries:

* **Selenium**: To automate web browser interaction, navigate to the TypeRacer website, and input the text.
* **BeautifulSoup4**: To parse the HTML of the webpage and extract the text that needs to be typed.
* **Colorama, Termcolor, and Pyfiglet**: To create a visually appealing and user-friendly command-line interface.

The main logic is split into two files:
* `BotLogic.py`: This file contains the core functions for browser automation, text extraction, and the typing simulation.
* `TypeRacerBot.py`: This file provides a console application that allows the user to select a browser and typing speed to initiate the bot.

## 🏁 Getting Started

To get the bot up and running on your local machine, follow these simple steps.

### Prerequisites

Make sure you have the following installed on your system:

* **Python 3.x**
* At least one of the following web browsers:
    * Google Chrome
    * Mozilla Firefox
    * Microsoft Edge
* The corresponding WebDriver for your browser may be required if Selenium cannot manage it automatically.

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/TypeRacerBot.git](https://github.com/your-username/TypeRacerBot.git)
    cd TypeRacerBot
    ```

2.  **Install the required Python packages:**
    ```sh
    pip install -r requirements.txt
    ```

## 🎮 Usage

1.  **Run the bot:**
    Execute the `TypeRacerBot.py` script from your terminal:
    ```sh
    python "Source Code/TypeRacerBot.py"
    ```

2.  **Choose your browser:**
    You will first be prompted to select your browser.

3.  **Choose a speed:**
    Next, you will be prompted to choose a typing speed from the menu.

4.  **Let the bot do the work:**
    Once you've made your choices, the bot will open your selected browser, navigate to TypeRacer, and start typing for you!

## 📂 File Descriptions

* `README.md`: This file, providing information about the project.
* `Source Code/BotLogic.py`: Contains the core logic for the bot's automation.
* `Source Code/TypeRacerBot.py`: The main script to run the bot, containing the user interface.
* `requirements.txt`: A list of the Python packages required for the project.

## 📝 Disclaimer

* This bot is intended for educational purposes and personal entertainment only.
* The bot has been tested on Google Chrome, Mozilla Firefox, and Microsoft Edge. Ensure you have at least one of these browsers installed.
