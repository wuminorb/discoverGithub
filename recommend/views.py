from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render
from cache_github.models import GithubRepo, get_user_from_db
from recommend.models import AlsoLikeRepo


@transaction.atomic
def refresh_also_like_repo(request, full_name, force=False):
    repo = GithubRepo.objects.get(full_name=full_name)
    AlsoLikeRepo.objects.filter(base_repo=repo).delete()
    repo_data = repo.get_data()
    stargazers = repo_data.get_stargazers()
    if not force:
        stargazers = stargazers.get_page(0)

    i = 0
    for stargazer in stargazers:
        print("%i/%i" % (len(stargazers), i))
        i += 1
        user = get_user_from_db(stargazer.login)

        if user.starred.count() == 0:
            user.refresh_from_github()
            user.refresh_starred()

        for starred_repo in user.starred.all():
            also_like, created = AlsoLikeRepo.objects.get_or_create(base_repo=repo, like_repo=starred_repo)
            also_like.weight += 1
            also_like.save()

    return HttpResponse("success")
