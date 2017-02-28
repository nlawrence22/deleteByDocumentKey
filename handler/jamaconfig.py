
class JamaConfig:
    def __init__(self):
        # please fill in the CONFIG section below:
        self.username = "username"
        self.password = "password"
        self.base_url = "https://{base_url}.jamacloud.com"
        self.itemType = 89008
        self.filename = "deleteDuplicates.csv"
        self.documentKey_column = 2
        self.name_column = 4


        # NOT part of the CONFIG section
        self.auth = (self.username, self.password)
        self.rest_url = self.base_url + "/rest/latest/"
        self.verify_ssl = True
