import logging
from models.action import ActionType


def check_required_permission(resource_object, role_object, user_role, accessed_resource):
    """This method evaluate if a user having permission to access a resource

    :param name: resoureces, role available, current user role, 
                name of resource user trying to acesss
    """

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
    """This is used to init the app

    :param name: user obejct and role object
    """
    print("Welcome to XYZ App...")
    print("Please create admin user to process ")
    user_name = input('Please enter username :')
    user_pass = input('Please enter password :')
    user_object.register_user(user_name, user_pass, 'admin')
    role_object.add_permission_with_role('admin', 'root')
    return user_name


def login_user_option(logged_user_name):
    """Display on screen option for user

    :param name: name of the logged in user
    """
    print('############################################################')
    print(f'Hi {logged_user_name}!!! you logged in successfully')
    print('1. [for login as another user]')
    print('b. [for view roles]')
    print('c. [for access resources]')
    tasks = input('Please enter: ')
    print('############################################################')
    return tasks


def admin_user_option():
    """
     display admin on screen option

    """
    print('############################################################')
    print('Hi !!! you are logged in as admin')
    print('1. [for login as another user]')
    print('2. [for create user]')
    print('3. [edit role]')
    print('4. [create new role]')
    print('5. [create new resources]')
    tasks = input('Please enter: ')
    print('############################################################')
    return tasks


def user_login(user_entity):
    """This method used to login a user

    :param name:user_obejct
    """
    loginInfoUser = (input('Please enter Username:'))
    loginInfoPassword = (input('Please enter Password:'))
    if user_entity.check(loginInfoUser, loginInfoPassword):
        print('logged in...')
        return loginInfoUser

    else:
        logging.error("username/password wrong !!")
        raise ValueError


def register_new_user(user_object, role_object):
    """This method used to create new user in the system

    :param name: user obejct and role object
    """
    logging.info('Registering new user in the system')
    uname = (input('Please enter username:'))
    pword = (input('Please enter password:'))
    print('Please enter Role, for help: ', role_object.roles)
    user_role = input('Please enter role:')
    if user_role not in role_object.roles.keys():
        print("Please provide correct Role...")
        raise KeyError
    user_object.register_user(uname, pword, user_role)
    print("Current user buffer :", user_object.credintials)


def create_new_resources(resource_object):
    """This method used to create new resources in the system

    :param name: resource obejct
    """
    logging.info('Creating new resources in the system...')
    innerStop = 1
    while innerStop == 1:
        print("__________________________________________________________")
        resources_name = input('Please enter resource name :')
        print("Please enter permission, for help :", ActionType.list())
        required_persmission = int(input('Please enter number:'))
        resource_object.add_resource(
            resources_name, ActionType(required_persmission).name)
        print("Current resources buffer :",
              resource_object.resourcesList)
        innerStop = int(
            input(' To add more resources Press 1 otherwise 2 :'))
        print("__________________________________________________________")


def create_new_role(role_object):
    """This method used to create new role in the system

    :param name: role obejct
    """

    logging.info("Creating role with permission in the system")
    innerStop = 1
    while innerStop == 1:
        print("__________________________________________________________")
        role_name = input('Please enter role name :')
        print("Please enter permission, for help :", ActionType.list())
        permission_name = int(input('Please enter number :'))
        role_object.add_permission_with_role(
            role_name, ActionType(permission_name).name)
        print("Current roles buffer :", role_object.roles)
        innerStop = int(
            input(' To add more permission Press 1 otherwise 2 :'))
        print("__________________________________________________________")
