import praw

reddit = praw.Reddit(user_agent='Sellorekt (by /u/Sellorekt)',
                     client_id='', client_secret='', username='Sellorekt', password='')

print('Reddit Downvoter App')
print(f'Logged as: {reddit.user.me()}')
username = input('Enter username: ')
user = reddit.redditor(username)
print(f'Downvoting user: {user}\nIt might take a while...')

try:
    for comment in user.comments():
        comment.downvote()
        print(f'Downvoted: {comment}')
except:
    print('Other posts are older than 6 months. No point downvoting.')
else:
    print('Success!')
