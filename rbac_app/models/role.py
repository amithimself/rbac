class Role(object):
    """roles are associated to permissions to access resources
    """

    def __init__(self):
        """Initializes the a role with the permissions associated with it.
        """
        self.roles = {}

    def add_permission_with_role(self, role, permission_name):
        """add a persmission with a role

        :param name: role name and permission_name
        """

        try:
            self.roles[role].append(permission_name)
        except KeyError:
            self.roles[role] = [permission_name]

    def remove_role(self, role):
        """to remove a role from the app

        :param name: name of role
        """
        self.roles.pop(role)

    def get_permission(self, role):
        """get permission based on role

        :param name: role name
        """
        return self.roles[role]

    def __repr__(self):
        return '<Role %s>' % self.roles
