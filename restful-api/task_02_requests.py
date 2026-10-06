"""Fetch posts from JSONPlaceholder"""
import requests
import json
import csv

URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    """Fetch and print all posts from JSONPlaceholder"""
    responce = requests.get(URL)
    print(f"Status Code: {responce.status_code}")
    if responce.status_code == 200:
        posts = responce.json()
        for post in posts:
            print(post["title"])
    else:
        print("Failed to fetch posts.")


def fetch_and_save_posts():
    """Fetch and save all posts from JSONPlaceholder"""
    responce = requests.get(URL)
    print(f"Status Code: {responce.status_code}")
    if responce.status_code == 200:
        data = responce.json()
        posts = [{"id": p["id"], "title": p["title"], "body": p["body"]}
                 for p in data
        ]

        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            write = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            write.writeheader()
            write.writerows(posts)

        print(f"Saved {len(posts)} posts to posts.csv")
    else:
        print(f"Request failed with status code {responce.status_code}")

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
