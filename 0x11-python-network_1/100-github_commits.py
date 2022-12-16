#!/usr/bin/python3
"""lists the 10 most recent commits on a given GitHub repository.
[2;2R[>77;30502;0c]10;rgb:bfbf/bfbf/bfbf]11;rgb:0000/0000/0000"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
