import requests
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description="Wikipedia scraper")
parser.add_argument("-m", "--more", action="store_true",
                    help="For more detailed information")
parser.add_argument("-s", "--subject", type=str, help="Subject to search for")
args = parser.parse_args()
subject = args.subject

try:

    URL = f"https://en.wikipedia.org/wiki/{subject}"
    response = requests.get(URL, timeout=5)

    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.find("span", class_='mw-page-title-main').text  # type: ignore
    # content = soup.find("div", class_="mw-content-ltr mw-parser-output")
    contents = soup.find_all("p")

    if args.more:
        for content in contents:
            print(title)
            print(content.text)
    else:
        print(title)
        print(contents[1].text)


except requests.exceptions.RequestException as e:
    print(f'Error: {e}')
