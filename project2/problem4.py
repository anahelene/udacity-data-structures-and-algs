class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def get_groups(group, all_groups):
    groups = group.get_groups()
    all_groups = all_groups + groups
    for sub_group in groups:
        all_groups = get_groups(sub_group, all_groups)

    return all_groups

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    all_groups = [group]

    all_groups = get_groups(group, all_groups)

    all_users = [] #could be a set/dict.
    for sub_group in all_groups:
        users = sub_group.get_users()
        all_users = all_users + users
    print(all_users)
    if user in all_users:
        return True
    else:
        return False

print(is_user_in_group('sub_child_user', parent))
#True

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child.add_user("sub_child_user")
sub_child.add_user( "sub_child_user_1")
sub_child.add_user("sub_child_user_2")

child.add_group(sub_child)
parent.add_group(child)

child.add_user('Ana')
child.add_user('Will')
child.add_user('Ana')
parent.add_user('Barbara')
parent.add_user('Daniel')

print(is_user_in_group('Emily', parent))
#False
print(is_user_in_group('Daniel', parent))
#True
