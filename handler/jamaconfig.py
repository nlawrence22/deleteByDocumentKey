
class JamaConfig:
    def __init__(self):
        self.username = "username"
        self.password = "password"
        self.auth = (self.username, self.password)
        self.base_url = "https://{base_url}.jamacloud.com"
        self.rest_url = self.base_url + "/rest/latest/"
        self.itemType = 89008
        self.filename = "deleteDuplicates.csv"
        self.documentKey_column = 2
        self.name_column = 4
        self.verify_ssl = True
