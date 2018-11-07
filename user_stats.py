from typing import List

import pandas as pd
import matplotlib.pyplot as plt

stats_columns: List[str] = [
    "login",
    "name",
    "nb_followers",
    "nb_following",
    "nb_contributions",
    "nb_org",
    "nb_repos_a",
    "nb_repos_m",
    "nb_repos_o"
]


def get_user_stats(github_user):
    """get_user_stats
    :parameter : Github user object
    :return : List of stats on the user
    """
    nb_followers = github_user.followers
    nb_following = github_user.following
    nb_contributions = github_user.contributions
    nb_org = github_user.get_orgs().totalCount
    nb_repos_all = github_user.get_repos(type='all', sort='updated').totalCount
    nb_repos_owner = github_user.get_repos(type='owner', sort='updated').totalCount
    nb_repos_member = github_user.get_repos(type='member', sort='updated').totalCount

    return [
            github_user.login,
            github_user.name,
            nb_followers,
            nb_following,
            nb_contributions,
            nb_org,
            nb_repos_all,
            nb_repos_owner,
            nb_repos_member]


def generate_users_stats(github_users_list):
    """
    :param github_users_list:
    :return: dataframe of users' stats
    """
    print("- Generating users' stats list")
    users_stats_list = []

    for user in github_users_list:
        print("Current user : {} ".format(user.login))
        users_stats_list.append(get_user_stats(user))

    return pd.DataFrame(users_stats_list, columns=stats_columns)


def topk_followed(github_users_information, k=10):
    """display_topk_foll
    :param github_users_information: array of stats per user (user who are collaborators in React)
           k                       : number of users in the top
    :return: a dataframe of the top k users
    """
    github_users_information = github_users_information.sort_values('nb_followers', ascending=False)
    returned_df = github_users_information[['login', 'nb_followers']]
    return returned_df[0:k]


def topk_contributions(github_users_information, k=10):
    github_users_information = github_users_information.sort_values('nb_contributions', ascending=False)
    returned_df = github_users_information[['login', 'nb_contributions']]
    return returned_df[0:k]


def topk_repos_owner(github_users_information, k=10):
    github_users_information = github_users_information.sort_values('nb_repos_o', ascending=False)
    returned_list = github_users_information[['login', 'nb_repos_o']]
    return returned_list[0:k]


def display_repart_total_contrib(github_users_information, type='hist'):
    github_users_information.sort_values('nb_contributions', ascending=False)
    if type == 'loglog':
        github_users_information['nb_contribution'].reset_index().plot(loglog=True)
        plt.xlabel('Number of contributors')
        plt.ylabel('Number of contributions in all users repos')
        plt.title('Evolution of the number of contributions by number of contributors')
        plt.show()
    else:
        hist = github_users_information['nb_contributions'].hist(bins=100)
        hist.plot()
        plt.xlabel('Number of contributions')
        plt.ylabel('Number of contributors')
        plt.title('Number of contributors per number of contributions')
        plt.show()

