from typing import List

import pandas as pd

stats_columns: List[str] = [
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
        users_stats_list.append(get_user_stats(user))

    return pd.DataFrame(users_stats_list, columns=stats_columns)

def showTopKFollowed(github_collaborators_stats):

