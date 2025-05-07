
A simple key logger

# Python Keylogger

A simple Python keylogger that captures and logs keystrokes along with timestamps. This project uses the `pynput` library to listen for keyboard events and writes the captured keys to a text file for analysis.

## 📋 Features
- Logs every key pressed with a timestamp
- Handles special keys like `[SPACE]`, `[ENTER]`, and `[BACKSPACE]`
- Gracefully exits on `Esc` key press
- Lightweight and easy to customize

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or later
- `pynput` library (install using `pip install pynput`)

### Installation
Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/YourUsername/basic-keylogger.git
cd basic-keylogger

```

## Usage

Run the keylogger:

``` bash

python keylogger.py

```

Captured keystrokes will be saved to the keys.txt file in the same directory.

 ## Ethical Considerations

Important: This keylogger is intended for educational purposes only. Use it responsibly and always obtain proper consent before logging keystrokes.

##  File Structure

basic-keylogger/
│
├── keylogger.py    # Main script
├── keys.txt        # Log file (generated on first run)
└── README.md       # Project documentation

##  Future Improvements
	•	Add encryption for log files
	•	Implement a stealth mode
	•	Automatically email logs (with consent)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

