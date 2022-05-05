class Credentials:
    """
    Class to generate instances of Credentials
    """    
    credentials_list = []

    def __init__(self, account_name, account_user_name, account_password):
        '''
        defines properties for our credentials objects.
        '''
        self.account_name = account_name
        self.account_user_name = account_user_name
        self.account_password = account_password