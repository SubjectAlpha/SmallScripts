import time, requests, asyncio
from datetime import datetime

#time in seconds to wait between checks
WAIT_TIME = 10 

#URLS you want to check
URLS = [
    "https://www.amazon.com/NVIDIA-RTX-3090-Founders-Graphics/dp/B08HR6ZBYJ/ref=sr_1_2?crid=3SD7RX8HMKXS8&keywords=rtx+3090&qid=1641489047&sprefix=rtx+3090%2Caps%2C101&sr=8-2",
    "https://www.newegg.com/asus-geforce-rtx-3090-rog-strix-rtx3090-o24g-gaming/p/N82E16814126456?Description=3090&cm_re=3090-_-14-126-456-_-Product&quicklink=true",
    "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-ti-12gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6462956.p?skuId=6462956"
]

ACCESS_ERRORS = [
    "access denied",
]

#Set the strings that should be on the page if the product is not available
OUT_OF_STOCK_STRINGS = [
    "sold out",
    "out of stock",
    "backorder",
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

    if any(e in productpage for e in ACCESS_ERRORS):
        print("[", current_time, "]", bcolors.FAIL + "Access denied" + bcolors.ENDC)
        return False

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
