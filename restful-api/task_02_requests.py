#!/usr/bin/python3
"""
Module that handle fetch posts from JSONPlaceholder
"""
import csv
import json
import requests



def fetch_and_print_posts():
    """function to print posts from given url"""

    r = requests.get("https://jsonplaceholder.typicode.com/posts")


    print(f"Status Code: {r.status_code}")

    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post.get("title"))



def fetch_and_save_posts():
    """function that save all posts from a given url"""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")

    if r.status_code == 200:
        posts = r.json()

        data = []
        for post in posts:
            data.append(
                {
                    "id": post.get("id"),
                    "title": post.get("title"),
                    "body": post.get("body"),
                }
            )

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()