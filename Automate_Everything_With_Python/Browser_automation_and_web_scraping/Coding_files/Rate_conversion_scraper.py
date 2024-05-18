from bs4 import BeautifulSoup
import requests


def get_currency(inp_curr, op_curr):
    url = f"https://www.x-rates.com/calculator/?from={
        inp_curr}&to={op_curr}&amount=1"

    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:-4])
    return rate


print(get_currency("INR", "USD"))
