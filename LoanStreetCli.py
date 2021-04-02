
import requests

class LoanStreetCli:
    REMOTE_URL = 'https://loanstreet-demo.herokuapp.com'
    LOCAL_URL = 'http://localhost:3000'
    BASE_URL = REMOTE_URL
    DEFAULT_PASSWORD = 'default_pass'
    DEFAULT_USER = 'default_user'

    def __init__(self, userName=DEFAULT_USER, password=DEFAULT_PASSWORD, url=BASE_URL):
        self.userName = userName
        self.password = password
        self.url = url
        self.bearerToken = None

        self.sendRequest()

    def sendRequest(self, path='', verb='post', payload=None):
        # login with user info to get bearer token
        if self.bearerToken is None:
            try:
                r = requests.post(self.url + '/login', data = { 'username': self.userName, 'password': self.password })
                self.bearerToken = r.json()['access_token']
            except:
                print('Something went wrong while authenticating')

        if self.bearerToken is None:
            return
            
        # send the actual request we want
        headers = {'Authorization': 'Bearer ' + self.bearerToken}
        if verb == 'get':
            r = requests.get(f'{self.url}/{path}' , headers = headers)
        elif verb == 'post':
            r = requests.post(f'{self.url}/{path}' , headers = headers, data = payload)
        elif verb == 'put':
            r = requests.put(f'{self.url}/{path}' , headers = headers, data = payload)
        elif verb == 'patch':
            r = requests.patch(f'{self.url}/{path}' , headers = headers, data = payload)

        return r

    def getAllLoans(self):
        return self.sendRequest('loan', 'get').json()

    def createLoan(self, loan):
        return self.sendRequest('loan', 'post', loan).json()

    def getLoan(self, id):
        return self.sendRequest(f'loan/{id}', 'get').json()

    def updateLoan(self, id, loan):
        return self.sendRequest(f'loan/{id}', 'put', loan).json()

    def patchLoan(self, id, loan):
        return self.sendRequest(f'loan/{id}', 'patch', loan).json()

