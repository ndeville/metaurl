import os
from requests import get
from dotenv import load_dotenv
load_dotenv()

MYIP = os.getenv("MYIP")

def check_ip():
    global MYIP

    myip = get('https://api.ipify.org').content.decode('utf8')

    if MYIP == myip:
        return True
    else:
        return False



########################################################################################################

if __name__ == '__main__':
    print()
    myip = get('https://api.ipify.org').content.decode('utf8')
    print(f"{myip=}")
    if MYIP == myip:
        print("\nIP has NOT changed")
    else:
        print("\nIP has changed")
    print()
