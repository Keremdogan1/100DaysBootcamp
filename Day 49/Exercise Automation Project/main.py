from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

import os
from datetime import datetime,timedelta

ACCOUNT_EMAIL = "kerem@test.com"
ACCOUNT_PASSWORD = "password123"
GYM_URL = "https://appbrewery.github.io/gym/"

booked_count = 0
waitlist_count = 0
already_done_count = 0

detailed_information = []

#------------------------------------------------------------------------------

def retry(func, retries=7, description=None):
    tried = 1
    while retries:
        print(f"Trying {description}. Attempt: {tried}")
        try:
            if func():
                return True
        except Exception as e:
            print(f"Error: {e}")
        retries -= 1
        tried += 1
        sleep(1)
    return False

def login():   

    submit_button = wait.until(
        EC.element_to_be_clickable((By.ID, "submit-button"))
    )
    submit_button.click()
    sleep(5)
    error_count = driver.find_elements(By.ID, "error-message")
    if len(error_count) == 0:
        return 1
    else:
        return 0
    
def book_class():
    global booked_count
    global waitlist_count
    global already_done_count

    book_buttons = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[id^='book-button-']"))
    )

    for button in book_buttons:
        if formatted_tuesday_book_time in button.get_attribute("id") or formatted_thursday_book_time in button.get_attribute("id"):

            excersize = button.get_attribute("id").split("-")[2]
            excersize_date_list = button.get_attribute("id").split("-")[3:6]
            excersize_date = datetime(int(excersize_date_list[0]), int(excersize_date_list[1]), int(excersize_date_list[2]))
            remaining_day = (excersize_date - server_datetime).days

            detailed_excersize_date = ""

            if remaining_day == 0:
                detailed_excersize_date = f"Today ({excersize_date.strftime("%a, %b %d")})"
            elif remaining_day == 1:
                detailed_excersize_date = f"Tomorrow ({excersize_date.strftime("%a, %b %d")})"
            else:
                detailed_excersize_date = f"{excersize_date.strftime("%a, %b %d")}"

            text = button.text

            
            
            button.click()
            sleep(5)
            error_count = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-error-']")
            if len(error_count) > 0:
                return 0
            else:
                if text == "Book Class":
                    print(f"✓ Booked: {excersize.title()} Class on {detailed_excersize_date}")
                    detailed_information.append(f"  • [New Booking] {excersize.title()} Class on {detailed_excersize_date}") 
                    booked_count += 1
                elif text == "Booked":
                    print(f"✓ Already booked: {excersize.title()} Class on {detailed_excersize_date}")
                    already_done_count += 1
                elif text == "Join Waitlist":
                    print(f"✓ Joined to waitlist: {excersize.title()} Class on {detailed_excersize_date}")
                    detailed_information.append(f"  • [New Waitlist] {excersize.title()} Class on {detailed_excersize_date}") 
                    waitlist_count += 1
                else:
                    print(f"✓ Already on waitlist: {excersize.title()} Class on {detailed_excersize_date}")
                    already_done_count += 1
                return 1

#------------------------------------------------------------------------------

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)
driver.get(GYM_URL)

login_button = wait.until(
    EC.element_to_be_clickable((By.ID, "login-button"))
)
login_button.click() 

email = wait.until(
    EC.visibility_of_element_located((By.NAME, "email"))
)
email.send_keys(ACCOUNT_EMAIL)

password = wait.until(
    EC.visibility_of_element_located((By.NAME, "password"))
)
password.send_keys(ACCOUNT_PASSWORD)

retry(login, description="Login")

#------------------------------------------------------------------------------

server_date = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "h1"))
)
server_date = server_date.text.split(" ")[3].split(")")[0]
server_date_list = server_date.split(".")
server_datetime = datetime(int(server_date_list[2]), int(server_date_list[1]), int(server_date_list[0]))
today = server_datetime.weekday()

day_to_add_tuesday = (1 - today) % 7
day_to_add_thursday = (3 - today) % 7

tuesday_book_date = server_datetime + timedelta(days=day_to_add_tuesday)
formatted_tuesday_book_time = f"{str(tuesday_book_date).split()[0]}-1800"

thursday_book_date = server_datetime + timedelta(days=day_to_add_thursday)
formatted_thursday_book_time = f"{str(thursday_book_date).split()[0]}-1800"

#------------------------------------------------------------------------------

retry(book_class, description="Booking")

#------------------------------------------------------------------------------

comfirmed_bookings_count = 0
expected_count = booked_count + waitlist_count + already_done_count
found_count = 0

print()
print(f"--- Total Tuesday/Thursday 6pm classes: {expected_count} ---")
print()
print("--- VERIFYING ON MY BOOKINGS PAGE ---")

my_bookings_button = wait.until(
    EC.element_to_be_clickable((By.ID, "my-bookings-link"))
)
my_bookings_button.click()

try:
    comfirmed_bookings = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[id^='booking-card-booking']"))
    )
    for comfirmed_booking in comfirmed_bookings:
        print(f"  ✓ Verified: {comfirmed_booking.get_attribute("data-class-type").title()} Class")
        found_count += 1
except:
    pass

try:
    waitlists = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[id^='waitlist-card-waitlist']"))
    )
    for waitlist in waitlists:
        print(f"  ✓ Verified: {comfirmed_booking.get_attribute("data-class-type").title()} Class (Waitlist)")
        found_count += 1
except:
    pass

print()
print("--- VERIFICATION RESULT ---")
print(f"Expected: {expected_count} bookings")
print(f"Found: {found_count} bookings")

if expected_count == found_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {expected_count - found_count} bookings")

#------------------------------------------------------------------------------

# driver.quit()
