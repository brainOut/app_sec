import requests
import socket
import sys


class fuzz_url:
    def __init__(self, url, wordlist):
        self.url = url
        self.wordlist = wordlist

    def dirchecker(self):

        for paths in self.wordlist:
            try:
                # print('http://' + self.url + '/' + paths)
                response_code = requests.get('http://' + self.url + '/' + paths).status_code
                if response_code != 404:
                    print(f"http://{self.url}/{paths} ({response_code})")
            except Exception:
                print(f"exception {Exception}")


if __name__ == "__main__":
    fuzzer = fuzz_url('127.0.0.1:8000', ["toto", "tata", "admin"])
    fuzzer.dirchecker()
