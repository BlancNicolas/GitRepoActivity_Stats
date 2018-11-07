import requests
import numpy
import json

# Draft
nb_of_pages = range(1, 210)

# ---------
payload = {'since': '2013-05-24T16:00:00Z', 'per_page': '50'}
r_commits = requests.get('https://api.github.com/repos/facebook/react/commits',
                 auth=('token', '5953e738ca9bfa101c5959887e9aff6adf28d21e'), params=payload)
print(r_commits.status_code)
print(r_commits.headers)
print(r_commits.content)
# ---------

data = r_commits.json()

for page in nb_of_pages:
    payload_commits = {'page': str(page), 'per_page': '50'}
    r_commits = requests.get('https://api.github.com/repos/facebook/react/commits',
                     auth=('token', '5953e738ca9bfa101c5959887e9aff6adf28d21e'), params=payload)
    data = r_commits.json()
    res_all_2 = res_all_2 + json.loads(data)
    print("...Fetching page {}, Status : {}".format(page, r.status_code))

res_all_raveled = numpy.ravel(res_all)

# Get commits' authors list
authors = []


# Get events list
for event in data:
    events.append(event["event"])

# Get events type list
events_type = list(set(events))

# Get events list
for event in data:
    dates.append(event["created_at"])

# Get events list
for event in data:
    dates.append(event["commit"]["author"]["date"])










