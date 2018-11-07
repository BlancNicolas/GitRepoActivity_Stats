import requests
import json
import numpy
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import user_stats as us
from github import Github

nb_of_pages = range(1, 210)
item_per_pages = 100
events = []
dates = []
res_all = []

# Get the list of all commits per contributors
r_contributors = requests.get('https://api.github.com/repos/facebook/react/stats/contributors',
                              auth=('token', '5953e738ca9bfa101c5959887e9aff6adf28d21e'))
data_contributors = json.loads(r_contributors.content)

# Columns
keys = [
    "author",
    "total",
    "weeks",
]

columns = [
    "login",
    "id",
    "node_id",
    "avatar_url",
    "gravatar_id",
    "url",
    "html_url",
    "followers_url",
    "following_url",
    "gists_url",
    "starred_url",
    "subscriptions_url",
    "organizations_url",
    "repos_url",
    "events_url",
    "received_events_url",
    "type",
    "site_admin",
    "total",
    "w",
    "a",
    "d",
    "c",
]

# ---------------------------------------------------
# Data formatting
# ---------------------------------------------------

data = []

# Browsing all the rows and creating a list of list(tuples defined by columns)
# ---------------------------------------------------

for contributor in data_contributors:
    row = []
    returned_list = []
    author_infos = list(contributor["author"].values())
    total = [contributor["total"]]
    row = author_infos + total
    for x in contributor["weeks"]:
        print(row + list(x.values()))
        returned_list.append(row + list(x.values()))
    data = data + returned_list

stats = pd.DataFrame(data, columns=columns)
stats_1 = stats[['login', 'id', 'node_id', 'total', 'w', 'a', 'd', 'c']]
list_contributors = list(stats_1['login'].unique())

# We have all the contributions per week of each contributor, the fact is that :
# -> If we want to know the number of all commits of a contributor now, we can't sum
# because each week ('w' column) represents the total number of commit at that point of time
# -> So we have to apply a groupBy and sort on 'w' and take the first of each group

grouped_stats_1 = stats_1.sort_values(['login','w'],ascending=False).groupby('login')
top_contributors = grouped_stats_1.first().sort_values('total', ascending=False)

grouped_stats_date = stats_1.sort_values('w', ascending=False)

# ---------------------------------------------------
# Repartition of contributor per contribution number
# ---------------------------------------------------
hist = top_contributors['total'].hist(bins=100)
plt.xlabel('Number of contributions')
plt.ylabel('Number of contributors')
plt.title('Number of contributors per number of contributions')
plt.show()
n_bins = 1000
fig, axs = plt.subplots
axs[0].hist(top_contributors['total'], bins=n_bins)

# ---------------------------------------------------
# Log Log
# ---------------------------------------------------
top_contributors['total'].reset_index().plot(loglog= True)
plt.xlabel('Number of contributors')
plt.ylabel('Number of contributions')
plt.title('Evolution of the number of contributions by number of contributors')
plt.show()

# ---------------------------------------------------
# Activity per user
# ---------------------------------------------------


g = Github("5953e738ca9bfa101c5959887e9aff6adf28d21e")
repo = g.get_repo("facebook/react")
stats_contributors = repo.get_stats_contributors()

contributors = repo.get_contributors()
stats_users = us.generate_users_stats(contributors)

contributors_list = []

for contributor in contributors:
    contributors_list.append(contributor)

