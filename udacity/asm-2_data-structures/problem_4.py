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

    def __repr__(self):
        return f"{self.name} {self.groups} ({self.users})"


def is_user_in_group(user: str, group: Group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user is None or user == '':
        return False
    if type(group) != Group:
        return False

    if user in group.users:
        return True

    for child_group in group.groups:
        if is_user_in_group(user, child_group):
            return True


if __name__ == '__main__':
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    # print(parent.groups[0].groups[0].__dict__)

    # Add your own test cases: include at least three test cases
    # and two of them must include edge cases, such as null, empty or very large values

    # Test Case 1
    print(f'---------- Test 1 ----------- ')
    print(f'user: {sub_child_user}')
    print(f'group: {parent}')
    if (is_user_in_group(sub_child_user, parent)):
        print(f'\n--> user {sub_child_user} exists in group {parent.name}')

    # Test Case 2
    print(f'\n---------- Test 2 -----------')
    user = None
    print(f'user: {user}')
    print(f'group: {parent}')
    print(is_user_in_group(user, parent))

    # Test Case 3
    print(f'\n---------- Test 3 -----------')
    user = ''
    print(f'user: {user}')
    print(f'group: {parent}')
    print(is_user_in_group(user, parent))

    # Test Case 3
    print(f'\n---------- Test 4 -----------')
    group = None
    print(f'user: {sub_child_user}')
    print(f'group: {group}')
    print(is_user_in_group(sub_child_user, group))
