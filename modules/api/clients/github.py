import requests


class GitHub:
    '''
    def get_user_defunkt(self):
        r = requests.get('https://api.github.com/users/defunkt')
        body = r.json()

        return body
    
    def get_non_exist_user(self):
        r = requests.get('https://api.github.com/users/sergii_butenko')
        body = r.json()

        return body
    '''
    # We can improve our code, and combine two methods in one, here is new version
    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        #r = requests.get(r.format('https://api.github.com/users/{username}'))
        body = r.json()

        return body
    
    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name}
        )
        body = r.json()

        return body