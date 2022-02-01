"""
instagram bot with instaPy
"""


from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace


user = ""
senha = ""
path = (r"~/geckodriver.exe")
comments = ['Your feed is an inspiration. @{}', 'I love your profile!@{}',]
session = InstaPy(username= user, 
                  password= senha, 
                  geckodriver_path= path,
                  headless_browser = True
                  )
with smart_run(session):
    session.set_relationship_bounds(enabled = True,
                                    delimit_by_numbers= True,
                                    max_followers= 8500,
                                    min_followers= 50,
                                    min_following= 9)
    
    
    
    #session.set_do_comment(enabled=True, percentage=100)
    #session.set_comments(comments)
    #session.like_by_tags(['kalilinux', 'cybersecurity', 'linux', 'programming'], amount=30, interact=True)
    #session.set_user_interact(amount=50, randomize=True, percentage=100)
    session.unfollow_users(amount=126, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=655)
    #session.set_user_interact(amount=50, randomize=True, percentage=100)
    session.end()
    
