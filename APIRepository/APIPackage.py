import requests

# 簡單封裝 Request 方法

class APIPackage():
    def __init__(self):
        self.session = requests.session()
        self.csrf = None
        self.headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
            'Accept' : 'application/json',
            'Content-Type' : 'application/json'
        }

    def requests(self, url, method, data=None):
        # CHECK CSRF IF NOT NONE
        if(self.csrf != None):
            self.headers['X-CSRF-Token'] = self.csrf

        # DO [ GET | POST ] REQUEST
        if method.upper() == 'GET':
            response = self.session.get(url, headers=self.headers, params=data) if data else self.session.get(url,headers=self.headers)
        elif method.upper() == 'POST':
            response = self.session.post(url, headers=self.headers, data=data) if data else self.session.post(url,headers=self.headers)

        # UPDATE CSRF IF RESPONSE HEADER CONTAINS "X-CSRF-TOKEN" FIELD
        if("X-CSRF-Token" in response.headers):
            self.csrf = response.headers.get("X-CSRF-Token")

        return response