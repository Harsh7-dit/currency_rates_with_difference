from utilities import *
from setting import *

def main_menu():
    while True:
        print("\n--- X-Rates Scraper and Comparator ---")
        print("1. Download CSV for a specific date")
        print("2. Compare currency rates between two dates")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            date = get_valid_date_input("Enter the date for which to download data (YYYY-MM-DD): ")
            data = scrape_xrates_for_date(date)
            if data is not None:
                filename = f"xrates_data_{date}.csv"
                data.to_csv(filename, index=False)
                print(f"Data saved to '{filename}'")
            else:
                print("Failed to fetch data for the given date.")
        elif choice == '2':
            calculate_usd_exchange_difference()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()
