from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Define columns for the CSV
columns = ["Brand", "Car Model", "Mileage Drove", "City", "Price", "Member", "How Long Ago"]

def parse_car_data(flat_data):
    """
    Converts flattened data into structured lists of car details.
    Handles time information like 'minutes ago' or 'hours ago'.
    """
    structured_data = []
    temp_data = []
    member_flag = False
    how_long_ago = "Not given"

    for item in flat_data:
        if item == "FEATURED":
            continue
        if item == "AUTH DEALER":
            continue
        if item == "MEMBER":
            member_flag = True
            continue
        if "minute" in item or "hour" in item:  # Check for time information
            how_long_ago = item
            continue

        temp_data.append(item)
        if len(temp_data) == 4:  # Group every 4 items into one car's details
            structured_data.append({
                "Brand": temp_data[0].split(" ")[0],
                "Car Model": temp_data[0],
                "Mileage Drove": temp_data[1],
                "City": temp_data[2].split(",")[0],
                "Price": temp_data[3],
                "Member": "Yes" if member_flag else "No",
                "How Long Ago": how_long_ago
            })
            temp_data = []  # Reset for the next group
            member_flag = False  # Reset member flag
            how_long_ago = "Not given"  # Reset time info

    return structured_data

def main():
    all_car_data = []  # List to store all cars' data
    driver = None

    try:
        # Initialize Selenium WebDriver
        driver = webdriver.Chrome()

        # Loop through pages (modify the range for more pages)
        for page_id in range(1, 19):  # Adjust range as needed
            url = f"https://bikroy.com/en/ads/bangladesh/cars?sort=date&order=desc&buy_now=0&urgent=0&page={page_id}"
            driver.get(url)

            # Wait for the listings to load
            WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.list--3NxGO'))
            )

            # Find all rows in the car list
            rows = driver.find_elements(By.CSS_SELECTOR, '.list--3NxGO')
            print(f"Scraping page {page_id}... Found {len(rows)} rows.")

            # Flatten all text from rows into one long list
            flat_data = []
            for row in rows:
                flat_data.extend(row.text.split("\n"))

            # Debugging: Print raw flat data
            print(f"Flat Data Extracted: {flat_data}")

            # Parse the flattened data into structured car data
            page_car_data = parse_car_data(flat_data)
            all_car_data.extend(page_car_data)

            # Wait before proceeding to the next page
            time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Ensure driver is properly closed
        if driver:
            driver.quit()

    # Save the structured data into a CSV file
    print(f"Total car listings scraped: {len(all_car_data)}")
    df = pd.DataFrame(all_car_data, columns=columns)
    df.to_csv("secondhand_car_details.csv", index=False)
    print("Data saved to secondhand_car_details.csv")

if __name__ == "__main__":
    main()
