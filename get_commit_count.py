import requests
import re
import datetime
import json


def getCurrentWeekCommitCount(user, repo):
    today = (datetime.date.today())
    last_monday = today - datetime.timedelta(days=today.weekday())
    # print("Today's date is: ", today)
    # print("Last Monday's date is: ", last_monday)
    CommitsTillLastMonday = commitCountUntilDate(user, repo, str(last_monday))
    CommitsTillToday = commitCountUntilDate(user, repo, str(today))
    print("***Repo:", repo)
    print("Commits Till Last Monday: ", CommitsTillLastMonday)
    print("Commits Till Today:", CommitsTillToday)
    Count = int(CommitsTillToday)-int(CommitsTillLastMonday)
    print("Total Commits This Week:", Count)
    print()
    return Count


def commitCountUntilDate(u, r, d):
    try:
        return re.search('\d+$', requests.get('https://api.github.com/repos/{}/{}/commits?per_page=1&until={}'.format(u, r, d)).links['last']['url']).group()
    except:
        # print("Seems there are no commits")
        return 0


def getPublicReposList(u):
    return requests.get('https://api.github.com/users/{}/repos'.format(u)).text


user=str(input('GitHub UserName: '))
# user = 'RajeshReddyG'
repos = getPublicReposList(user)
parsedJSON = json.loads(repos)
print("User Stats Of: ", user)
Sum = 0
for i in range(len(parsedJSON)):
    Sum = Sum+getCurrentWeekCommitCount(user, parsedJSON[i]['name'])

print("**************\nTotal Commits in this Week in All Repos:", Sum)
print("**************\nBye...")

# '2020-06-09T12:12:12Z'
