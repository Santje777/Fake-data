from rich import print

print("Hello, [red]Susanne[/red]!")
print("Hello, [bold underline red]Susanne[/bold underline red]!")

import requests

response  = requests.get("https://jsonplaceholder.typicode.com/photos/1")

photo = response.json()
print(response)
print(photo)
print(photo['title'])
print(photo['thumbnailUrl'])