import praw
import wikipedia
import time

print('Starting App')
reddit = praw.Reddit(user_agent='Sellorekt (by /u/Sellorekt)',
                     client_id='', client_secret='', username='Sellorekt', password='')
print('Connected to the server')

wt_done = []
with open('wt_done.txt', 'r') as file:
    wt_done = eval(file.readline())
print('Database loaded successfully')

subreddit = reddit.subreddit('Warthunder')

tanks = open('tanks.txt').read().splitlines()
print('List of Tanks loaded successfully')

while True:
    print(f'{time.strftime("%H:%M:%S", time.localtime())} Checking for new posts')
    for submission in subreddit.new(limit=10):
        # print(submission.title)
        for x in tanks:
            if x in submission.title:
                print(f'Found match for Tank {x} in thread {submission.title} posted by: {submission.author} (Post ID: {submission.id})')
                if submission.id not in wt_done:
                    wiki = wikipedia.summary(x)
                    print(f'Posting comment: Hey, did you know, that {wiki}\n\n You can read more about it at {wikipedia.page(x).url}')
                    submission.reply(f'Hey, did you know, that {wiki}\n\n You can read more about it at {wikipedia.page(x).url}')
                    wt_done.append(submission.id)
                    with open('wt_done.txt', 'w') as file:
                        file.write(str(wt_done))
                    print('Done!')
                else:
                    print('Already posted in this thread!')

    print('No more posts to process. Going to sleep for 60 seconds')
    time.sleep(60)
