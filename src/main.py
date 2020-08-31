# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# Example rest code
import http.client

conn = http.client.HTTPSConnection("www.buycrash.com")

payload = ""

headers = {
    'authority': "www.buycrash.com",
    'cache-control': "max-age=0",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'sec-fetch-site': "cross-site",
    'sec-fetch-mode': "navigate",
    'sec-fetch-user': "?1",
    'sec-fetch-dest': "document"
    }

conn.request("GET", "/", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8")n)
