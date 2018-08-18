import praw

reddit = praw.Reddit(user_agent='CountingEmotes (by /u/Deadinsky66)',
                     client_id='client_id', client_secret="client_secret",
                     username='username', password='password')
emotes = ['](#helix', '](#dome', '](#martyr', '](#falseprophet', '](#pcblood', '](#lazor', '](#burrito', '](#c3', '](#m4', '](#wattson', '](#WAHAHA', '](#ziggy', '](#martyr', '](#spinarak', '](#root', '](#olden', '](#solareon', '](#sunshine', '](#tppPokeball', '](#baba', '](#chatot', '](#awoo', '](#tppRng', '](#tppPokeyen', '](#tppCrit', '](#tppHax', '](#tppMiss', '](#tppPc', '](#tppRobored', '](#tppRiot', '](#tppDome', '](#tppHelix', '](#tppSlowpoke', '](#tppCursor', '](#tppTrumpet', '](#tppFogChamp', '](#kappa', '](#Kappa', '](#kreygasm', '](#Kreygasm', '](#pogchamp', '](#PogChamp', '](#keepo', '](#Keepo', '](#swiftrage', '](#SwiftRage', '](#failfish', '](#FailFish', '](#onehand', '](#OneHand', '](#trihard', '](#TriHard', '](#kapow', '](#KAPOW', '](#biblethump', '](#BibleThump', '](#praiseit', '](#PraiseIt', '](#dansgame', '](#DansGame', '](#elegiggle', '](#EleGiggle', '](#wutface', '](#WutFace', '](#prchase', '](#PRChase', '](#opieop', '](#OpieOP', '](#babyrage', '](#BabyRage', '](#residentsleeper', '](#ResidentSleeper', '](#bort', '](#BORT', '](#deilluminati', '](#deIlluminati', '](#minglee', '](#MingLee', '](#tppUrn', '](#datsheffy', '](#DatSheffy', '](#seemsGood', '](#Seemsgood', '](#notlikethis', '](#NotLikeThis', '](#brokeback', '](#BrokeBack', '](#4head', '](#4Head', '](#amber', '](#jasmine', '](#VoHiYo', '](#vohiyo', '](#BloodTrail', '](#bloodtrail', '](#BigBrother', '](#bigbrother', '](#solface', '](#KappaPride', '](#kappapride', '](#phancero']
emote_count = [0] * len(emotes)
new_submissions = reddit.subreddit('twitchplayspokemon').new(limit=1000)
submissions = list(new_submissions)
for submissionid in submissions:
    submission = reddit.submission(id=submissionid)
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        for i in range(len(emotes)):
            if emotes[i] in comment.body:
                emote_count[i]+=1
for i in range(len(emotes)):
    print( '* {}: {}'.format((emotes[i])[3:len(emotes[i])], emote_count[i]))
for i in range(len(emotes)):
    print((emotes[i])[3:len(emotes[i])])
for i in range(len(emotes)):
    print(emote_count[i])
