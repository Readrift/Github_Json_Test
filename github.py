import requests

class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = "Your Token"

    def getUser(self, username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json()

    def getRepositories(self,username):
        response = requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()

    def createRepository(self,name):
        response = requests.post(self.api_url+'/users/repos?acces_token='+self.token, json={
            "name": name,
            "description": "I did this with code",
            "homepage": "https://github.com/users/readrift",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True})
            
        return response.json()


github = Github()

while True:
    choose = input("1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nChoose:")

    if choose == '4':
        break
    else:
        if choose == '1':
            username = input('username: ')
            result = github.getUser(username)
            print(f"name:  {result['name']} public repos: {result['public_repos']} follower: {result['followers']}")
        elif choose == '2':
            username = input('username: ')
            result = github.getRepositories(username)
            for repo in result:
                print(repo['name'])
        elif choose == '3':
            name = input('repository name: ')
            result = github.createRepository(name)
            print(result)
        else:
            print("Wrong Choose")

