import logging


class User(object):

    def __init__(self):
        # buffer to hold all registered user
        self.credintials = {}

    def register_user(self, username, password, role):
        """This used to resgister a new user

        :param role: username and password and role
        """
        self.credintials[username] = {"password": password, "roles": [role]}

    def check(self, user, password):
        """This used to check if the username and paword is exist or not

        :param role: username and password
        """
        if user in self.credintials.keys() and password == self.credintials[user]["password"]:
            return True
        else:
            return False

    def add_role(self, username, role):
        """Adds the role to this user

        :param role: the role to be assigned to the user
        """
        try:
            self.credintials[username]["roles"].append(role)
            print(
                f'Successfully added role, {username} new roles : {self.credintials[username]["roles"]}')
        except KeyError:
            logging.error('Please provide correct username')

    def get_roles(self, username):
        """get the role to this user

        :param role: the user name 
        """
        return self.credintials[username]['roles']

    def __repr__(self):
        return '<All Users %s>' % self.credintials
