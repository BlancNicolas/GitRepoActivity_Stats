# GitRepoActivity_Stats
A python script that fetch informations about repo. 

## Credentials and use of a token 
If you want you can make this GET request with authentication but you only can do 60 requests without. Otherwise
you can use a token you can find on your profile and put in in cred.py. 

## Variables 
- stats : Basically a DataFrame created thanks to Pandas which contains the result of the 
request GET : "https://api.github.com/repos/facebook/react/stats/contributors". 
- stats_1 : reduced DataFrame of basic information. 
- list_contributors : The list of contirbutors 
- grouped_stats_1 : stats_1 grouped by login and date 'w'
- top_contributors : Sorted dataframe of top contributors with most recent information ( indicated in by 'w' ) 
- hist : Number of contributors per number of contributions
- log-log using : Evolution of the number of contributions by number of contributors 

## Use of PyGithub 
After using the Github API and understanding how it worked, I decided to use this library to fetch stats per user. 
All the informations are in users_stats.py. 

### Topk information on users 

There are 3 functions that return a list of top k users  : 

- topk_followed
- topk_contributions
- topk_repos_owner 

You can decide how many users you want in the top K.


