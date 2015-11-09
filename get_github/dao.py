from .connect import G
from get_github.models import GithubUser


def save_user(user_data):
    user = GithubUser()
    user.blog = user_data.blog
    user.login = user_data.login
    user.company = user_data.company
    user.create_at = user_data.created_at
    user.emile = user_data.email
    user.hireable = user_data.hireable
    user.location = user_data.location
    user.name = user_data.name
    user.public_repo_num = user_data.public_repos
    user.update_at = user_data.updated_at
    user.save()
    return user


def user_exist(login):
    users = GithubUser.objects.filter(login=login)
    if users.count() > 0:
        return users.first()
    return None


def update_following(user_data, user):
    followings = user_data.get_following()
    for following in followings:
        following_user = user_exist(following.login)
        if not following_user:
            following_user = GithubUser()
            following_user.login = following.login
            following_user.save()

        user.following.add(following_user)
