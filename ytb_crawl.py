import requests

API_KEY = "AIzaSyA6qFUWtEjAHW-2iaOyDqt-3MVba4NtPMI"
url = f"https://www.googleapis.com/youtube/v3/search"

with open('keywords.txt', 'r', encoding='utf-8') as file:
    keywords = [line.strip() for line in file if line.strip()]
for query in keywords:
    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'maxResults': 5,
        'key': API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()
    for item in data['items']:
        title = item['snippet']['title']
        video_id = item['id']['videoId']
        link = f"https://www.youtube.com/watch?v={video_id}"
        print(f"{title}\n {link}\n")

