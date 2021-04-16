import time, requests, asyncio
from datetime import datetime

#time in seconds to wait between checks
WAIT_TIME = 10 

#URLS you want to check
URLS = [
    "url1",
    "url2"
]

#Set the strings that should be on the page if the product is not available
OUT_OF_STOCK_STRINGS = [
    "out of stock"
]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


async def CheckStock(url):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("[", current_time, "]", bcolors.WARNING + "Checking stock of", url + bcolors.ENDC)
    # Get the text from that page and put everything in lower cases
    productpage = requests.get(url).text.lower()

    # Check whether the strings are in the text of the webpage
    if any(x in productpage for x in OUT_OF_STOCK_STRINGS):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("[", current_time, "]", bcolors.FAIL + "Out of stock" + bcolors.ENDC)
    else:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("[", current_time, "]", bcolors.OKGREEN + "IN STOCK" + bcolors.ENDC)

async def main():
    while True:
        for url in URLS:
            await CheckStock(url)
        time.sleep(WAIT_TIME)

if __name__ == "__main__":
    asyncio.run(main());
