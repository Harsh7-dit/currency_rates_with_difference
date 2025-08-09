### **X-Rates Scraper and Currency Rate Comparator**

1. Scrape currency exchange rates for a specific historical date from x-rates.com and downloads it in csv file.

2. Compare currency rates between two dates and save only the difference results in a clean CSV file.

**Features :**

✅ Scrape live historical exchange rate data using pandas.read_html and requests.

✅ Compare two dates and calculate differences in:

USD → Currency

Currency → USD (inverse)

✅ Save the CSV file.


**Requirements :**

- Make sure you have Python 3.7 installed

- Then, library pandas, requests and datetime

**How to Use :**

Run the script " python scraper.py "

Then follow the interactive prompts

**Menu Options :**

1. Download CSV for a specific date

The script will scrape exchange rates for that day and save it to a CSV file.

2. Compare currency rates between two dates

The script scrapes both dates and compares Rate to USD and USD to Currency and save it to a CSV file.

3. Exit from the code.

**License :**

This project is for educational and personal use. Not affiliated with x-rates.com.

