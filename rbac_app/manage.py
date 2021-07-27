
import traceback
import sys
import logging
from models.action import ActionType
from models.role import Role
from models.appuser import User
from models.resources import Resources
from rbac.utils import *

"""This method evaluate if a user having permission to access a resource
param name: resoureces, role available, current user role, 
            name of resource user trying to acesss
"""


def check_required_permission(resource_object, role_object, user_role, accessed_resource):
    logging.info('Checking if user having required permission')
    resource_key = (list(resource_object.resourcesList.keys()))[
        accessed_resource]
    required_permission = resource_object.resourcesList[resource_key]
    user_role
    if 'admin' in user_role:
        return True
    user_permission = []
    for role in user_role:
        user_permission.extend(role_object.get_permission(role))

    return True if required_permission in user_permission else False


# init the app
def app_init(user_object, role_object):
    print("Welcome to XYZ App...")
    print("Please create admin user to process ")
    user_name = input('Please enter username :')
    user_pass = input('Please enter password :')
    user_object.register_user(user_name, user_pass, 'admin')
    role_object.add_permission_with_role('admin', 'root')
    return user_name


def main():
    user_entity = User()
    role_entity = Role()
    resource_entity = Resources()
    logged_user_name = app_init(user_entity, role_entity)
    logged_user_role = 'admin'

    Stop = 1
    while Stop == 1:
        try:
            if logged_user_role == 'admin':
                tasks = admin_user_option()

            if logged_user_role != 'admin':
                tasks = login_user_option(logged_user_name)

            # task to login
            if tasks == 'Login' or tasks == '1':
                logged_user_name = user_login(user_entity)
                logged_user_role = 'admin'
                if 'admin' not in user_entity.credintials[logged_user_name]['roles']:
                    logged_user_role = 'not_admin'

            # task to register user
            if tasks == 'Register' or tasks == '2':
                register_new_user(user_entity, role_entity)

            # edit roles in the system
            if tasks == '3':
                user = (input('Please enter username:'))
                print("Available roles :", role_entity.roles)
                role = (input('Please enter role to be added:'))
                user_entity.add_role(user, role)
                print("Current user buffer :", user_entity.credintials[user])

            # create new roles in the system
            if tasks == '4':
                create_new_role(role_entity)

            # create new resources in the system
            if tasks == '5':
                create_new_resources(resource_entity)

            # check log of current user
            if tasks == 'b':
                print('Accessing role of user :', logged_user_name)
                print(user_entity.get_roles(logged_user_name))

            # check if a user having permission of selected resources
            if tasks == 'c':
                resource_entity.display_resources()
                user_input = int(input('Enter resource number to access :'))
                print('Having Permission :', check_required_permission(resource_entity, role_entity,
                                                                       user_entity.get_roles(logged_user_name), user_input))
            # quit the program
            if tasks == 'quit' or tasks == '9':
                print("See you later!")
                Stop = 2

        except Exception:
            logging.error("Please follow correct instructions...",
                          traceback.print_exc())


if __name__ == '__main__':
    main()
