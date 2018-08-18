import praw

SUBREDDIT = 'TwitchDatesPokemon'
CHANGE_FROM = ['burrito', 'burritojesus', 'birdjesus', 'xatu', 'burrixatu', 'helix', 'burlix', '3-burritobrian', '2-brian', 'burritogator', 'lazorgator', 'burritie', 'katie', 'burritoprophet', 'falseburrito' 'martyr']
REPLACEMENT = ['new-burrito', 'new-burritoabba', 'new-abba', 'new-burrito', 'new-burrito', 'new-burrito', 'new-burrito', 'new-burritobrian', 'new-brian', 'new-burritogator', 'new-gator', 'new-burritokatie', 'new-katie', 'new-burritomary', 'new-burritomary', 'new-mary']

print('\nLength %d vs Length %d' % (len(CHANGE_FROM), len(REPLACEMENT)))

if len(CHANGE_FROM) == len(REPLACEMENT):
    reddit = praw.Reddit(user_agent='FlairChangeKichi',
                     client_id='client_id', client_secret="client_secret",
                     username='username', password='password')
    subreddit = reddit.subreddit(SUBREDDIT)
    all_flairs = list(subreddit.flair())
    print('Found %d user flairs' % len(all_flairs))

# This just counts the flairs to be changed
    counterall = 0
    for userflair in all_flairs:
        flaircss = userflair['flair_css_class']
        for placement in range(0, len(CHANGE_FROM)):
            if flaircss == CHANGE_FROM[placement]:
    	        counterall += 1
    
# This changes the flair css classes    
    counter = 0
    for userflair in all_flairs:
        flaircss = userflair['flair_css_class']
        for placement in range(0, len(CHANGE_FROM)):
            if flaircss == CHANGE_FROM[placement]:
                counter += 1
                username = userflair['user']
                flairtext = userflair['flair_text']
                print('%d of %d: Changing flair for /u/%s' % (counter, counterall, username))
                subreddit.flair.set(username, flairtext, REPLACEMENT[placement])
print('\nDone.')
