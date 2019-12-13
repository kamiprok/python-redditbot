import praw
import time
import random


print('Starting App')
reddit = praw.Reddit(user_agent='Sellorekt (by /u/Sellorekt)',
                     client_id='', client_secret='', username='Sellorekt', password='')
print('Connected to the server')
already_done = []
with open('already_done.txt', 'r') as file:
    already_done = eval(file.readline())
print('Database loaded successfully')
subreddit = reddit.subreddit('LeagueofLegends')
#champions = ['Ahri', 'Illaoi', 'Kayle', 'Morgana', 'Neeko', 'Sivir', 'Tristana']
champions = open('champs.txt').read().splitlines()
print('List of Champions loaded successfully')
while True:
    try:
        print('\n')
        print(time.strftime('%H:%M:%S', time.localtime()), ' Checking for new posts...')
        for submission in subreddit.new(limit=10):
            for x in champions:
                if x in submission.title:
                    print('Found match for Champion: ', x, '    in thread: ', submission.title, ' posted by: ', submission.author, '(Post ID:', submission.id, ')')
                    # for comment in submission.comments.list():
                    #     if comment.author == 'Sellorekt':
                    if submission.id not in already_done:
                        print('Posting comment...')
                        adjectives = ["That's so cool!", "That's awesome!", 'Excellent!', 'Neat!', 'Dandy!', "That's great!", "Nice!"]
                        y = random.choice(adjectives)
                        # submission.reply(f'{x} is my favourite Champion! If you are new to the game check out these useful links:'
                        #                  f'\n\nWiki: [{x}](https://leagueoflegends.fandom.com/wiki/{x})'
                        #                  f'\n\nOP.GG: [{x}](https://www.op.gg/champion/{x}/statistics/)'
                        #                  f"\n\n^(I'm a little friendly Bot in training. Sorry for inconvenience!)")
                        submission.reply(f"{y} {x} is my favourite champion! ")
                        print(f"{y} {x} is my favourite champion! ")
                        print('Comment posted!')
                        print('Marking post as processed...')
                        already_done.append(submission.id)
                        with open('already_done.txt', 'w') as file:
                            file.write(str(already_done))
                        print('Done!')
                    else:
                        print('Already posted in this thread!')

        print('No more posts to process. Going to sleep. (60 seconds)')
        time.sleep(60)
        # for i in range(9, 1, -1):
        #     print(f'Sleeping. {i} minutes')
        #     time.sleep(60)
        # print('Sleeping. 1 minute left...')
    except:
        print('Oops! Something went wrong. Going to sleep for a while. (60 seconds)')
        time.sleep(60)
        # for i in range(9, 1, -1):
        #     print(f'Sleeping. {i} minutes')
        #     time.sleep(60)
        # print('Sleeping. 1 minute left...')
