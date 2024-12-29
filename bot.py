import requests
from fake_useragent import UserAgent
from eth_account import Account

url = "https://bioprotocol.in/register.php"

try:
    ua = UserAgent()
    user_agent = ua.random
except Exception as e:
    print("Error fetching user agent, using Chrome as default.")
    user_agent = ua.chrome

headers = {
    "cache-control": "no-cache, no-store, must-revalidate, max-age=0",
    "content-length": "115",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "PHPSESSID=c55u816vtcpic8fnu2dmmfv49n",
    "origin": "https://bioprotocol.in",
    "pragma": "no-cache",
    "referer": "https://bioprotocol.in/?refer=bf088b",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": user_agent
}

referral_code = input("Masukkan referral code, contoh: bf088b: ")

iterations = int(input("Masukkan jumlah reff: "))

for _ in range(iterations):
    new_account = Account.create()

    with open("akun.txt", "a") as file:
        file.write(f"Address   : {new_account.address}\n")
        file.write(f"Privatekey: {new_account.key.hex()[2:]}\n")

    payload = {
        "email": "",
        "referral_code": referral_code,
        "referral_point": "",
        "password": "",
        "username": new_account.address,
        "register": ""
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:
            if "success" in response.text.lower():
                print("Registration successful!")
            else:
                print("Registration might have failed. Check response body for details.")
        else:
            pass
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)