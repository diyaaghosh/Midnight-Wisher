#  Midnight-Wisher

A simple Python script that automatically sends a **"Happy Birthday "** message on **WhatsApp** right at **12:00 AM** — so you never miss wishing your friends at midnight again!

---

##  Features

- Sends **automated WhatsApp messages** via WhatsApp Web
- Triggers **exactly at midnight** (12:00 AM)
- Customizable birthday message
- Lightweight and easy to use
- Made just for fun!

---

##  Built With

- **Python 3**
- [`pywhatkit`](https://github.com/Ankit404butfound/PyWhatKit) – to send WhatsApp messages
- `datetime` – for time calculations
- `time` – to control program flow

---

##  Requirements

- Python 3.6 or higher
- `pywhatkit` library

Install using pip:

```bash
pip install pywhatkit
```
Make sure you're logged into WhatsApp Web in your default browser.

## How to Use
- Clone or download this repo.

- Open the midnight_wisher.py file.

- Update the script with:

  #### 1.Phone number of your friend (with country code)

  #### 2.Your custom birthday message (optional)

#### 3. Run the script before 12:00 AM and leave it running.
```
python midnight_wisher.py
```
## At exactly 12:00 AM, the message will be sent automatically through WhatsApp Web.

```
import pywhatkit
import datetime
import time

# Set recipient's number and message
phone_number = "+91XXXXXXXXXX"
message = " Happy Birthday! Hope you have a great year ahead! "

# Wait until it's midnight
while True:
    now = datetime.datetime.now()
    if now.hour == 0 and now.minute == 0:
        pywhatkit.sendwhatmsg(phone_number, message, 0, 1)
        break
    time.sleep(30)

```
## Notes
- Keep your system and browser active.

- Don’t close the terminal or browser before midnight.

- This only works if WhatsApp Web is logged in and accessible.

  ## License
- This project is licensed under the MIT License – see the LICENSE file for details.

