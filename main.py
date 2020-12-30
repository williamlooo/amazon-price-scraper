#!/usr/bin/env python3
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle 
import time

options = Options()
options.add_argument("--headless") # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('--disable-gpu')  # applicable to windows os only
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")

CHROMEDRIVER_PATH = "/"
AMAZON_ITEM_URL_STRING = "https://www.amazon.com/dp/B07ZPC9QD4?ref=ods_ucc_kindle_B07ZPC9QD4_nrc_ucc"
PICKLE_NAME = "airpod_prices.p"
PLOT_FILENAME = "airpod_prices.png"



def collect_point_and_plot():
	global data
	driver = webdriver.Chrome(options=options, executable_path=CHROMEDRIVER_PATH)
	driver.get(AMAZON_ITEM_URL_STRING)
	price = driver.execute_script("return parseFloat(document.getElementById('priceblock_ourprice').innerText.slice(1,100))")
	
	if price:
		#print("today's price is: "+str(float(price)))
		now = time.localtime(time.time())
		current_date,current_time = time.strftime("%m-%d-%Y", now),time.strftime("%m-%d %H:%M", now)

		data[current_date] = float(price)
		sorted_keys = sorted(list(data.keys()))
		sorted_values = [data[key] for key in sorted_keys]

		fig = plt.figure(figsize=(18,10))
		plt.title("Item Prices, last run "+str(current_time))
		plt.xlabel('Date')
		plt.ylabel('Price')
		plt.xticks(rotation=45, ha='right')
		plt.plot(sorted_keys, sorted_values)
		plt.savefig(PLOT_FILENAME)

	else:
		print("error retrieving price")
		exit()

	driver.close()

def pickle_save():
	global data
	f = open(PICKLE_NAME, 'wb') 
	pickle.dump(data, f)
	f.close()

def load_pickle():
	global data 
	f = open(PICKLE_NAME, 'rb')
	data = pickle.load(f)
	f.close() 

if __name__ == '__main__':
	data = {}
	load_pickle()
	collect_point_and_plot()
	pickle_save()
	print("[INFO] PLOT UPDATE COMPLETE")
