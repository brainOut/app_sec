import requests
import socket
import sys


class fuzz_url:

    def __init__(self, url, quiet=False):
        self.url = url
        self.quiet = quiet
        self.wordlist = open("wordlist.txt", 'r').readlines()

    def dirchecker(self):
        url_ok = []
        for paths in self.wordlist:
            paths = paths.strip("\r\n")
            try:
                # print('http://' + self.url + '/' + paths)
                response_code = requests.get('http://' + self.url + '/' + paths).status_code
                if not self.quiet:
                    print(f"trying http://{self.url}/{paths}")

                if response_code != 404:
                    url_ok = f"http://{self.url}/{paths} ({response_code})"
            except Exception:
                print(f"exception {Exception}")
        print(url_ok)


if __name__ == "__main__":
    fuzzer = fuzz_url('127.0.0.1:8000', True)
    fuzzer.dirchecker()
