import praw

SUBREDDIT = 'PokemonPrism' #subreddit w/o the /r/
reddit = praw.Reddit(user_agent='FullFlairSet (modified by /u/Deadinsky66)',
                     client_id='client_id', client_secret="client_secret",
                     username='username', password='password')
subreddit = reddit.subreddit(SUBREDDIT)
submissions = list(subreddit.new(limit=1000))

for submissionid in submissions:
    submission = reddit.submission(id=submissionid)
    if 'question' in submission.title.lower():
        submission.flair.select('6b875498-4ca4-11e7-a8ad-0eebad244e0c')
    elif 'help' in submission.title.lower():
        submission.flair.select('6b875498-4ca4-11e7-a8ad-0eebad244e0c')
    elif 'bug' in submission.title.lower():
        submission.flair.select('66ef6286-4ca4-11e7-90e9-0e5f5958cf48')
    elif 'glitch' in submission.title.lower():
        submission.flair.select('66ef6286-4ca4-11e7-90e9-0e5f5958cf48')
    elif '?' in submission.title.lower():
        submission.flair.select('6b875498-4ca4-11e7-a8ad-0eebad244e0c')
    else:
        submission.flair.select('4a197d9e-4ca5-11e7-8f35-0e297cfcc1b8')
