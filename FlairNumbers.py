import praw

SUBREDDIT = 'twitchplayspokemon' #subreddit w/o the /r/
reddit = praw.Reddit(user_agent='CountingFlairs (modified by /u/Deadinsky66)',
                     client_id='client_id', client_secret="client_secret",
                     username='username', password='password')
subreddit = reddit.subreddit(SUBREDDIT)

flairs = {None: 0}
for fc in subreddit.flair.templates:
    if fc['flair_css_class']:
        flairs[fc['flair_css_class'][6:]] = 0

for f in subreddit.flair():
    if not f['flair_css_class'] in flairs:
        flairs[f['flair_css_class']] = 0

    flairs[f['flair_css_class']] += 1

sorted_flairs = sorted(flairs.items(), key=lambda x: x[1], reverse=True)
for name, count in sorted_flairs:
    print( '* {}: {}'.format(name, count))
