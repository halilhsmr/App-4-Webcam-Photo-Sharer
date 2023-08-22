import wikipedia
import requests


page = wikipedia.page("summer")
print(type(page))
print(page)
print(page.images)
link = page.images[0]
print(link)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/56.0.2924.76 Safari/537.36'}
response = requests.get(url=link, headers=headers)
print(response.status_code)

if response.status_code == 200:
    print("ow yeah")
    # with open("files/summer.jpg", "wb") as file:
    #     file.write(response.content)
