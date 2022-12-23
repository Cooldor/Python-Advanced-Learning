class Verification:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__lenpassword()

    def __lenpassword(self):
        if len(self.password) < 5:
            raise ValueError('Weak password')

    def save(self):
        with open('users', 'a') as r:
            r.write(f'{self.login, self.password}'+'\n')
