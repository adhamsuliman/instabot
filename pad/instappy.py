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


def job():
    session = InstaPy(username=insta_username, password=insta_password, headless_browser=True, want_check_browser=False)
    with smart_run(session):
        # session.set_smart_location_hashtags([(13.7563,100.5018)], radius=50)
        session.set_do_comment(enabled=True, percentage=20)
        session.set_comments(["That's a great look Pad Thai! @{}"], media='Photo')
        session.set_do_follow(enabled=True, percentage=5, times=2)
        # session.set_mandatory_words(['#ramadan', '#instafood'])
        session.like_by_tags(['padthai', 'PadThai','Padthai'], amount=100, media='Photo')  # 'ramadan', 'Ramadan', , use_smart_location_hashtags=True


schedule.every(1).second.do(job)

while True:
    schedule.run_pending()
    time.sleep(10)
