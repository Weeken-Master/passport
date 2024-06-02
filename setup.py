from DrissionPage import WebPage, ChromiumOptions
from DrissionPage.common import Keys
from DrissionPage.common import Actions
import time
from multiprocessing import Process 


def open_chrome_with_profile(user_data_path ,x):
    co = ChromiumOptions().auto_port()
    # co.set_argument(arg='--start-minimized', value=True)
    co.set_argument(arg='--ignore-ssl-errors', value=True)
    co.set_argument(arg='--user-data-dir', value=user_data_path)
    co.set_argument('--no-sandbox')  # No sandbox mode
    page = WebPage(chromium_options=co)

 
    time.sleep(3000)  # Simulate some action (replace with actual work)
    page.quit()  # Close the driver after each iteration

def main():
    profile_paths = [
        r'C:\Users\ADMIN\AppData\Local\Google\Chrome\User Data\Profile cutuan200'
        r'C:\Users\ADMIN\AppData\Local\Google\Chrome\User Data\Profile 21'
    ]

    processes = []
    x  = 0
    for profile_path in profile_paths:
        x = x +1
        process = Process(target=open_chrome_with_profile, args=(profile_path,x))
        processes.append(process)
        process.start()

    # Wait for all processes to finish (optional)
    for process in processes:
        process.join()

if __name__ == "__main__":
    main()