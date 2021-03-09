import requests
import socket
import sys
from bs4 import BeautifulSoup


def make_soup(url):
    html = requests.get(url, headers={
        "User-Agent": "Chocapic/3.0"}).content
    html_bs4 = BeautifulSoup(html, 'html.parser')
    html_inputs = html_bs4.findAll('input')

    for input in html_inputs:
        return input


class FuzzUrl:

    def __init__(self, url, quiet=False):
        self.url = url
        self.quiet = quiet
        self.wordlist = open("wordlist.txt", 'r').readlines()

    def dirchecker(self):
        url_ok = []
        for paths in self.wordlist:
            paths = paths.strip("\r\n")
            try:
                response_code = requests.get('http://' + self.url + '/' + paths).status_code
                if not self.quiet:
                    print(f"trying http://{self.url}/{paths}")
                if response_code != 404:
                    url_ok = f"http://{self.url}/{paths}"
                    print(f"http://{self.url}/{paths} ({response_code})")
            except Exception:
                exit(f"Can't reach the host {self.url}")

        print(make_soup(url_ok))
        return url_ok
        # print(url_ok)


if __name__ == "__main__":
    fuzzer = FuzzUrl('127.0.0.1:8000', True)
    fuzzer.dirchecker()
