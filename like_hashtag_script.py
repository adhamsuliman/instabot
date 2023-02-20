# Import library
"""
Example to handle Email/SMS challenges
"""
import email
import imaplib
import re
import random

from instagrapi import Client
from instagrapi.mixins.challenge import ChallengeChoice
from dotenv import load_dotenv,find_dotenv
import os
import time

class insta:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.CHALLENGE_EMAIL = os.environ['CHALLENGE_EMAIL']
        self.CHALLENGE_PASSWORD = os.environ['CHALLENGE_PASSWORD']
        self.IG_USERNAME = os.environ['IG_USERNAME']
        self.IG_PASSWORD = os.environ['IG_PASSWORD']

        # Instantiate Client
        self.cl = Client()
        self.cl.challenge_code_handler = self.challenge_code_handler
        self.cl.change_password_handler = self.change_password_handler
        self.cl.login('i.spy.padthai', 'Padthai894')

    def get_code_from_email(self, username):
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(self.CHALLENGE_EMAIL, self.CHALLENGE_PASSWORD)
        mail.select("inbox")
        result, data = mail.search(None, "(UNSEEN)")
        assert result == "OK", "Error1 during get_code_from_email: %s" % result
        ids = data.pop().split()
        for num in reversed(ids):
            mail.store(num, "+FLAGS", "\\Seen")  # mark as read
            result, data = mail.fetch(num, "(RFC822)")
            assert result == "OK", "Error2 during get_code_from_email: %s" % result
            msg = email.message_from_string(data[0][1].decode())
            payloads = msg.get_payload()
            if not isinstance(payloads, list):
                payloads = [msg]
            code = None
            for payload in payloads:
                body = payload.get_payload(decode=True).decode()
                if "<div" not in body:
                    continue
                match = re.search(">([^>]*?({u})[^<]*?)<".format(u=username), body)
                if not match:
                    continue
                print("Match from email:", match.group(1))
                match = re.search(r">(\d{6})<", body)
                if not match:
                    print('Skip this email, "code" not found')
                    continue
                code = match.group(1)
                if code:
                    return code
        return False

    def get_code_from_sms(username):
        while True:
            code = input(f"Enter code (6 digits) for {username}: ").strip()
            if code and code.isdigit():
                return code
        return None

    def challenge_code_handler(self, username, choice):
        if choice == ChallengeChoice.SMS:
            return self.get_code_from_sms(username)
        elif choice == ChallengeChoice.EMAIL:
            return self.get_code_from_email(username)
        return False

    def change_password_handler(self, username):
        # Simple way to generate a random string
        chars = list("abcdefghijklmnopqrstuvwxyz1234567890!&£@#")
        password = "".join(random.sample(chars, 10))
        return password

    def start(self):
        # find top 20
        hashtag = self.cl.hashtag_medias_recent('thaifood', 5)

        for i, h in enumerate(hashtag):
            pictures = h.dict()['resources']
            if len(pictures) > 1:
                for p in pictures:
                    pk = p['pk']
                    self.cl.media_like(pk)
                    continue
            else:
                pk = h.dict()['pk']
                self.cl.media_like(pk)
            print(f'Liked {i} pictures')



if __name__ == "__main__":
    i = insta()
    while True:
        i.start()
        time.sleep(600)
