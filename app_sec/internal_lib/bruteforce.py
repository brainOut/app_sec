from dirb import FuzzUrl  # \o/ Merci François
from bs4 import BeautifulSoup
import requests
import socket
import sys
from bs4 import BeautifulSoup
import os


class BruteForcer:

    def __init__(self, userlist="wordlist/users.txt", passlist="wordlist/rockyou.txt"):
        self.userlist = userlist
        self.passlist = passlist

    @staticmethod
    def get_urls(url, filename):
        s = FuzzUrl(f'{url}', True)
        s.dirchecker(True, True, f'{filename}')

        for url in open('results/'+filename, 'r').readlines():
            html = requests.get(url, headers={
                "User-Agent": "Chocapic/3.0"}).content
            html_bs4 = BeautifulSoup(html, 'html.parser')
            html_inputs = html_bs4.findAll('input')

        print("done")
        return True


# -------------------------
# 1 - récuperer les champs depuis le fuzzer OK
# 2 - faire la requete en POST avec les users/ pass (users.txt et rockyou.txt)
# 3 - vérifier le retour de la requete (savoir si c'est ok ou ko)

if __name__ == "__main__":
    # s = FuzzUrl('127.0.0.1:8000')
    # s.dirchecker(True, True, 'urls_to_bruteforce.txt')

    b = BruteForcer.get_urls("127.0.0.1:8000", "urls.txt")
