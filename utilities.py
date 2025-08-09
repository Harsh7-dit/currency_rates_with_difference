import requests
import pandas as pd
from datetime import datetime
from setting import *


def get_valid_date_input(prompt):
    while True:
        date_str = input(prompt)
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD (e.g., 2023-01-15).")


def scrape_xrates_for_date(target_date):
    date_for_url = target_date.strftime("%Y-%m-%d")
    url = xrates_url + date_for_url
    print(f"\nScraping data for {date_for_url} from: {url}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        tables = pd.read_html(response.text)

        if len(tables) > 1:
            currency_table = tables[1].copy()
            if len(currency_table.columns) >= 3:
                currency_table.columns = ['Currency', 'Rate to USD', 'USD to Currency']
                return currency_table
            else:
                print("Scraped table does not have expected structure.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Network or HTTP error fetching {url}: {e}")
    except ValueError as e:
        print(f"HTML parsing error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None


def calculate_usd_exchange_difference():
    print("\n--- Option 2: Compare Currency Rates Between Two Dates ---")
    date1 = get_valid_date_input("Enter the first date (YYYY-MM-DD): ")
    date2 = get_valid_date_input("Enter the second date (YYYY-MM-DD): ")

    df1 = scrape_xrates_for_date(date1)
    df2 = scrape_xrates_for_date(date2)


    if df1 is None or df2 is None:
        print("Failed to retrieve data for one or both dates.")
        return
    try:

        merged_df = pd.merge(df1, df2, on='Currency', suffixes=(f'_{date1}', f'_{date2}'))

        # Calculate difference
        merged_df['Rate to USD Diff'] = merged_df[f'Rate to USD_{date2}'] - merged_df[f'Rate to USD_{date1}']
        merged_df['USD to Currency Diff'] = merged_df[f'USD to Currency_{date2}'] - merged_df[f'USD to Currency_{date1}']

        output_file = f"usd_exchange_difference_{date1}_vs_{date2}.csv"
        merged_df.to_csv(output_file, index=False)
        print(f"\nExchange rate difference saved to: {output_file}")

    except Exception as e:
        print(f"Error comparing data: {e}")