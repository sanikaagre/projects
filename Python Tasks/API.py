import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    post = data[0]  
    title = post['title']
    body = post['body']
    
    print(f"Title: {title}")
    print(f"Body: {body}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
