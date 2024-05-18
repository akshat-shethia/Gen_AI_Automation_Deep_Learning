import requests

api_key = "a74fca7b6fa39dfecbb224daf5369b6d"


def make_request(city_name):
    r = requests.get(
        f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}")
    content = r.json()
    print(content)


make_request("Surat")
