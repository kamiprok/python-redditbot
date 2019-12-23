import praw

reddit = praw.Reddit(user_agent='',
                     client_id='',
                     client_secret='',
                     username='',
                     password='')

print('Reddit Downvoter App')
print(f'Logged as: {reddit.user.me()}')

is_user = True
while is_user:
    try:
        username = input('Enter username: ')
        user = reddit.redditor(username)
        print(f"{user}'s karma: {user.link_karma}")
        is_user = False
    except:
        print(f'User {user} does not exist')
    else:
        is_user = False

print(f'Downvoting user: {user}\nIt might take a while...')

i = 1
try:
    for comment in user.comments.new():
        print(f'{i}. {comment.body[:40]}...')
        comment.downvote()
        i += 1
except:
    print('No more comments to downvote.')
    pass
else:
    print('Success!')
print(f'Downvoted {i} comments.')
