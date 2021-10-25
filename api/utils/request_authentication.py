username = 'bmm'
token = 'a0efa2a3e7ede444a0b1eff83f91fd2a930eacf8dff36f278ac979eb5212dcaf'
users_db = {username:token}
class requestAuthentication:
    def __init__(self, request_header):
        self.username = request_header.get('username', '')
        self.token = request_header.get('token', '')
        if self.token[4:] == users_db[self.username]:
            self.content = request_header.get('Content-Type')
            self.action = request_header.get('action')
            self.auth = True
        else:
            self.auth = False