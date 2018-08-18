import praw

reddit = praw.Reddit(user_agent='FlairTemplateChange (by /u/Deadinsky66)',
                     client_id='client_id', client_secret="client_secret",
                     username='username', password='password')

#for template in reddit.subreddit('twitchplayspokemon').flair.templates:
#    print(template)

season = '0'
flairs = int(600/40)
letter1 = 'a'
letter2 = 'a'
for i in range(flairs):
    if (i < 52):
        print_flair = season + letter1
        reddit.subreddit('twitchplayspokemon').flair.templates.add("", css_class=print_flair, text_editable=True)
        letter1 = chr(ord(letter1) + 1)
        if (i == 51):
            letter1 = "a"
        elif (i == 25):
            letter1 = "A"
    else:
        print_flair = season + letter1 + letter2
        reddit.subreddit('twitchplayspokemon').flair.templates.add("", css_class=print_flair, text_editable=True)
        letter2 = chr(ord(letter2) + 1)
        if (((i+1)%52) == 0):
            letter1 += chr(ord(letter1) + 1)
            letter2 = "a"
        elif (((i+1)%26) == 0):
            letter2 = "A"
        
