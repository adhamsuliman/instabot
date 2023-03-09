from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import schedule
import time
from dotenv import load_dotenv,find_dotenv
import os

load_dotenv()
CHALLENGE_EMAIL = os.environ['CHALLENGE_EMAIL']
CHALLENGE_PASSWORD = os.environ['CHALLENGE_PASSWORD']
IG_USERNAME = os.environ['IG_USERNAME']
IG_PASSWORD = os.environ['IG_PASSWORD']
#your login credentials
insta_username=IG_USERNAME
insta_password=IG_PASSWORD 

#path to your workspace
set_workspace(path=None)

def job():
  session = InstaPy(username=insta_username, password=insta_password)
  with smart_run(session):
    session.set_smart_location_hashtags(['215069212','217184762'], radius=50)
    session.set_do_comment(enabled=True, percentage=20)
    session.set_comments(['Ramadan Kareem! @{}'], media='Photo')
    session.set_do_follow(enabled=True, percentage=5, times=2)
    session.set_mandatory_words(['#ramadan', '#instafood'])
    session.like_by_tags(['رمضان'], amount=100, media='Photo', use_smart_location_hashtags=True) #'ramadan', 'Ramadan',

schedule.every().hour.do(job)

while True:
  schedule.run_pending()
  time.sleep(10)