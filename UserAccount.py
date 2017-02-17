class UserAccount :
    """
    A class that models a user account for mega-social-media website, GuessMySecret
    """

    def __init__(self, my_username, my_password, my_secret):
        """
        Initialize the UserAccount object:
        :param username: user name (string)
        :param password: password to gain access to account (string)
        :param secret: user's secret, accessible only with password (string)
        """
        self.username=my_username
        self.secret = my_secret
        self.password =my_password
        
        
        #Complete the __init__ method

    def print_secret(self,password_attempt):
        if self.password == password_attempt:
            print (self.secret)
        else:
            print ("Invalid")
        
        """
        Checks user input, password_attempt - if this matches the user's
        password, then the user's secret is printed to the screen.

        :param password_attempt: guess for the password (string)
        """
        #Complete this method - check the input variable, password_attempt,
        #against the password for this user (the value of the instance variable, password).
        #If, and only if, there's a match, then print the user's secret to the screen.
