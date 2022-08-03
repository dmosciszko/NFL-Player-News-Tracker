import praw
from datetime import datetime

# ORGANIZE CODE
# NEXT IMPLEMENT SORT POSTS BY TIME
output = open("C:\\Users\\David\\Desktop\\fantasy.txt","w")

reddit = praw.Reddit(
    client_id="wwm3v1KBNeAiR8fYfcskcg",
    client_secret="SuNPhkN4LaVQLdTdoLOy1OFT60xIxw",
    user_agent="<console:BryceHall:1.0>",
    username="BryceHallBot",
    password="Bard2018"
    )

subreddit = reddit.subreddit("fantasyfootball")
user = reddit.user.me()
'''
for c in user.new(limit = 1000):
    c.delete()
'''


players = ["lamar jackson",
           "dalvin cook",
           "kenyan drake",
           "justin jefferson",
           "dk metcalf",
           "t.j hockenson",
           "chase edmonds",
           "michael carter",
           "matt prater",
           "mike evans",
           "ronald jones",
           "corey davis",
           "mike williams",
           "chase claypool",
           "antonio brown"]
for player in players:
    player_count = 0
    for submission in subreddit.hot(limit=1000):
        if player in submission.title.lower():
            if player_count == 0:
                output.write("==========================================\n")
                output.write(player.upper() + '\n')
                player_count += 1
            time = int(submission.created_utc)
            output.write(datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S\n'))
            output.write(submission.title + '\n')

'''
    for comment in submission.comments:
        if hasattr(comment, "body"):
            lowercase_comment = comment.body.lower()
            if "bryce hall" in lowercase_comment:
                comment.upvote()
                print("------------")
                print(comment.body)
                comment.reply("Bryce Hall")
'''
