import random

from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import schedule
import time
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv()
CHALLENGE_EMAIL = os.environ['CHALLENGE_EMAIL']
CHALLENGE_PASSWORD = os.environ['CHALLENGE_PASSWORD']
IG_USERNAME = os.environ['IG_USERNAME']
IG_PASSWORD = os.environ['IG_PASSWORD']
# your login credentials
insta_username = IG_USERNAME
insta_password = IG_PASSWORD

# path to your workspace
set_workspace(path=None)


class Instapy_bot:
    def __init__(self):
        CHALLENGE_EMAIL = os.environ['CHALLENGE_EMAIL']
        CHALLENGE_PASSWORD = os.environ['CHALLENGE_PASSWORD']
        IG_USERNAME = os.environ['IG_USERNAME']
        IG_PASSWORD = os.environ['IG_PASSWORD']
        self.session = InstaPy(username=IG_USERNAME, password=IG_PASSWORD, headless_browser=True, want_check_browser=False)

    def run(self):
        with smart_run(self.session):
            # session.set_smart_location_hashtags([(13.7563,100.5018)], radius=50)
            self.session.set_do_comment(enabled=True, percentage=20)
            self.session.set_comments(["That's a great look Pad Thai! @{}"], media='Photo')
            self.session.set_do_follow(enabled=True, percentage=5, times=2)
            # session.set_mandatory_words(['#ramadan', '#instafood'])
            self.session.like_by_tags(['padthai', 'PadThai', 'Padthai'], amount=100,
                                      media='Photo')  # 'ramadan', 'Ramadan', , use_smart_location_hashtags=True

    def job(self):
        for i in range(3):
            delay = random.randint(1, 60 * 60 // 3)
            self.schedule.enter(delay, 1, self.run())
        self.schedule.run()


if __name__ == '__main__':
    bot = Instapy_bot()
    while True:
        if random.random() < 1 / 3:
            bot.run()
            time.sleep(1)
