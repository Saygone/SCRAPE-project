import requests
from bs4 import BeautifulSoup
import json

# Изначальный url вебсайта
base_url = "http://quotes.toscrape.com/page/"
# Список для хранения данных
quotes_data = []
# Страница 1
page_number = 1

while True:

    url = f"{base_url}{page_number}/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        quote_blocks = soup.find_all("div", class_="quote")

        if not quote_blocks:
            break

        for block in quote_blocks:
            text = block.find("span", class_="text").get_text()
            author = block.find("small", class_="author").get_text()
            tags = [tag.get_text() for tag in block.find_all("a", class_="tag")]

            # Добавление данных о цитате в список
            quotes_data.append({
                "text": text,
                "author": author,
                "tags": tags
            })

        # Переход на следующую страницу
        page_number += 1
    else:
        print("Not found")
        break

with open("quotes.json", "w", encoding="utf-8") as file:
    json.dump(quotes_data, file, ensure_ascii=False, indent=4)


