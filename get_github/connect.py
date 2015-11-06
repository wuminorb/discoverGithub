from github import Github


def connect():
    token_file = open('token')
    try:
        token = token_file.read()
    finally:
        token_file.close()
    g = Github(token)
    return g

G = connect()
