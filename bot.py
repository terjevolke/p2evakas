import requests
from bs4 import BeautifulSoup
URL = "https://www.paevapraad.ee/parnu/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
food_elements = soup.find_all("div", class_="food")
resto_list =[]
for food_el in food_elements:
    food_name = food_el.find("span").string.lower()
    if "juustu" in food_name:
        if len(food_el.find_parents("div", class_="resto"))==1:
            resto = food_el.find_parents("div",class_="resto")[0].find("h2").contents[-1]
            resto_list.append([resto, food_name])
            # print(food_name)
print(resto_list)
