# TypeRacerBot

A bot that automates typing on [play.typeracer.com](https://play.typeracer.com/) for fun and educational purposes. This project uses Selenium to control a web browser and simulate typing at various speeds.

## 🚀 Features

* **Automated Typing**: Automatically types the text in a TypeRacer race.
* **Adjustable Speed**: Choose from a range of typing speeds, from a leisurely pace to superhuman speeds.
* **User-Friendly Interface**: A simple and colorful command-line interface to control the bot.
* **Fun Speed Tiers**: Amusing speed descriptions to add a bit of fun to the experience.

## ⚙️ How It Works

The bot is built with Python and utilizes the following libraries:

* **Selenium**: To automate web browser interaction, navigate to the TypeRacer website, and input the text.
* **BeautifulSoup4**: To parse the HTML of the webpage and extract the text that needs to be typed.
* **Colorama, Termcolor, and Pyfiglet**: To create a visually appealing and user-friendly command-line interface.

The main logic is split into two files:
* `BotLogic.py`: This file contains the core functions for browser automation, text extraction, and the typing simulation.
* `TypeRacerBot.py`: This file provides a console application that allows the user to select a typing speed and initiate the bot.

## 🏁 Getting Started

To get the bot up and running on your local machine, follow these simple steps.

### Prerequisites

Make sure you have the following installed on your system:

* **Python 3.x**
* **Microsoft Edge** browser
* **Microsoft Edge WebDriver**: The WebDriver must match your version of Microsoft Edge. You can download it from the [official Microsoft Edge WebDriver page](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).

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

2.  **Choose a speed:**
    You will be prompted to choose a typing speed from the menu. Enter a number from 0 to 5 to select your desired speed.

    ```
    Choose the desired Speed:
      -enter 0 to type like my grandma
      -enter 1 to type using two fingers just like your sister
      -enter 2 to type like you have two hands
      -enter 3 to type like a touchtyping world champ
      -enter 4 and they'll eat your dust
      -enter 5 fuck it i'm a hacker
    ```

3.  **Let the bot do the work:**
    Once you've made your choice, the bot will open Microsoft Edge, navigate to TypeRacer, and start typing for you!

## 📂 File Descriptions

* `README.md`: This file, providing information about the project.
* `Source Code/BotLogic.py`: Contains the core logic for the bot's automation.
* `Source Code/TypeRacerBot.py`: The main script to run the bot, containing the user interface.
* `requirements.txt`: A list of the Python packages required for the project.

## 📝 Disclaimer

* This bot is intended for educational purposes and personal entertainment only.
* The bot uses the Microsoft Edge web driver, so please ensure that both Microsoft Edge and its corresponding WebDriver are installed on your system.
* For a ready-to-use version without manual setup, you can download the `.exe` file from the `EXE` folder (if available).
