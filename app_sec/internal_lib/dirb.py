import requests
import socket
import sys
from bs4 import BeautifulSoup
import os


def have_inputs(url):
    html = requests.get(url, headers={
        "User-Agent": "Chocapic/3.0"}).content
    html_bs4 = BeautifulSoup(html, 'html.parser')
    html_inputs = html_bs4.findAll('input')

    if len(html_inputs) != 0:
        return True
    else:
        return False


def save_or_return(save_outputs, data):
    if save_outputs:
        file = open('test_url.txt', 'w')
        file.write(str(data))
        
    return data


class FuzzUrl:

    def __init__(self, url, quiet=False):
        self.url = url
        self.quiet = quiet
        self.wordlist = open("wordlist.txt", 'r').readlines()

    def dirchecker(self, with_inputs_only=False, save_outputs=True):
        url_ok = []
        url_with_inputs = []
        for paths in self.wordlist:
            paths = paths.strip("\r\n")
            try:
                response_code = requests.get('http://' + self.url + '/' + paths).status_code
                if not self.quiet:
                    print(f"trying http://{self.url}/{paths} ({response_code})")
                if response_code != 404:
                    url_ok.append(f"http://{self.url}/{paths}")
            except Exception:
                exit(f"Can't reach the host {self.url}")

        if with_inputs_only:
            for url in url_ok:
                if have_inputs(url):
                    url_with_inputs.append(url)

            save_or_return(True, url_with_inputs)
        else:
            save_or_return(True, url_ok)


if __name__ == "__main__":
    fuzzer = FuzzUrl('127.0.0.1:8000', True)
    fuzzer.dirchecker(True)
