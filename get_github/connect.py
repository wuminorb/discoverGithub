from github import Github


def connect():
    token_file = open('token')
    try:
        token = token_file.read()
    finally:
        token_file.close()
    g = Github(token, per_page=100)
    return g

G = connect()
