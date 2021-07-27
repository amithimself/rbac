class Resources:

    def __init__(self):
        self.resourcesList = {}

    def add_resource(self, resources_name, required_persmission):
        """Add a resource in the system

        :param name: name of resource and permission associated for the resource
        """
        self.resourcesList[resources_name] = required_persmission

    def remove_resource(self, resource_name):
        """Remove a resource

        :param name: name of resource
        """
        self.resourcesList.pop(resource_name)

    def display_resources(self):
        """display all resources available in the system

        """
        for i in range(len(self.resourcesList.keys())):
            print(f'Press {i}. {(list(self.resourcesList.keys()))[i]}')

    def __repr__(self):
        return '<Resources %s>' % self.resourcesList
