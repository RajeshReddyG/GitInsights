import requests
import re
import datetime 
  
  

user=str(input('GitHub UserName: '))
repo=str(input('GitHub Repo: '))
# Returns the current local date 
today =(datetime.date.today())
last_monday = today - datetime.timedelta(days=today.weekday())
print("Today date is: ", today) 
print("Today date is: ", last_monday) 


def commitCountUntilDate(u, r,d):
	return re.search('\d+$', requests.get('https://api.github.com/repos/{}/{}/commits?per_page=1&until={}'.format(u, r,d)).links['last']['url']).group()
CommitsTillLastMonday=commitCountUntilDate(user, repo, str(last_monday))
CommitsTillToday=commitCountUntilDate(user, repo, str(today))
print ("Commits Till Last Monday: ",CommitsTillLastMonday)
print ("Commits Till Today:",CommitsTillToday)
print ("Total Commits This Week:",int(CommitsTillToday)-int(CommitsTillLastMonday))
print ("Bye...")


# '2020-06-09T12:12:12Z'