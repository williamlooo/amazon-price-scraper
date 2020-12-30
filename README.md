# amazon-scraper
simple inventory price tracking utility with Selenium and Matplotlib.

## execution instructions (macOS, Linux)
1. download the latest chromedriver and place in this directory. (https://chromedriver.chromium.org/downloads)
1. if using macOS, chromedriver permissions may need to be granted. run __xattr -d com.apple.quarantine chromedriver__ in terminal.
1. run __pip install -r requirements.txt__ in terminal to install python packages.
1. run python3 main.py in terminal. Alternatively you may [set up a cron job](https://man7.org/linux/man-pages/man5/crontab.5.html) to automate data collection. 

