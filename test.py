import requests

BASE = "http://127.0.0.1:5000/"

newdata = {
    'brand': 'yeos',
    'variety': 'asd',
    'style': 'cup',
    'country': 'japan',
    'stars': 3,
    'topTen': '123'
}

updatedata = {
    'variety': 'lOw',
    'style': 'aaaaaaa',
    'country': 'malaysia',
    'stars': 4.0
}

response = requests.put(BASE + "reviews/5", updatedata)
print(response.json())


response = requests.post(BASE + "reviews", newdata)
print(response.json())

response = requests.get(BASE + "reviews?query=Assss&country=uk")
print(response.json())

response = requests.get(BASE + "reviews?query=low&country=japan")
print(response.json())

response = requests.get(BASE + "reviews?query=Ha&country=uk")
print(response.json())

response = requests.get(BASE + "reviews")
print(response.json())

# response = requests.post(BASE + "helloworld")
# print(response.json())
# response = requests.get(BASE + "helloworld/junwei")
# print(response.json())


