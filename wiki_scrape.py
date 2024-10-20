import requests
from bs4 import BeautifulSoup

try:

    URL = "https://en.wikipedia.org/wiki/India"
    response = requests.get(URL, timeout=5)

    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.find("span", class_='mw-page-title-main').text  # type: ignore
    # content = soup.find("div", class_="mw-content-ltr mw-parser-output")
    contents = soup.find_all("p")

    print(title)
    print(contents[1].text)

    # for content in contents:
    # print(content.text)

except requests.exceptions.RequestException as e:
    print(f'Error: {e}')
