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


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user in group.get_users():
        return True
    else:
        sub_groups = group.get_groups()
        for sub_group in sub_groups:
            if is_user_in_group(user, sub_group):
                return True

    return False


if __name__ == "__main__":

    # Test 1: provided test
    print("---\nTest#1")
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group(sub_child_user, parent))  # True
    print(is_user_in_group("notpresent", parent))  # False

    # Test 2: Edge case, an empty group
    print("---\nTest#2")
    emptyGroup = Group("Empty Group")
    print(is_user_in_group("No user", emptyGroup))  # False

    # Test 3: Combining two groups of gorups in a hierarchical manner, and testing if newly added group contains a user
    print("---\nTest#3")

    # First: Create two nested groups

    # Group 2 tree
    group2 = Group('Group #2')
    s_group2 = Group('Sub Group #2')
    ss_group2 = Group('Sub Sub Group #2')
    sss_group2 = Group('Sub Sub Sub Group #2')

    sss_group2.add_user("sss group 2 user")
    ss_group2.add_user("ss group 2 user")
    s_group2.add_user("s group 2 user")
    group2.add_user("group 2 user")

    ss_group2.add_group(sss_group2)
    s_group2.add_group(ss_group2)
    group2.add_group(s_group2)

    # Group 1 tree
    group1 = Group('Group #1')
    s_group1 = Group('Sub Group #1')
    ss_group1 = Group('Sub Sub Group #1')
    sss_group1 = Group('Sub Sub Sub Group #1')

    sss_group1.add_user("sss group 1 user")
    ss_group1.add_user("ss group 1 user")
    s_group1.add_user("s group 1 user")
    group1.add_user("group 1 user")

    ss_group1.add_group(sss_group1)
    s_group1.add_group(ss_group1)
    # Then add s_group2 as a sub sub group 1
    ss_group1.add_group(s_group2)
    group1.add_group(s_group1)

    # Test if group 1 contains "sss group 2 user"
    print(is_user_in_group("sss group 2 user", group1))  # True
    print(is_user_in_group("group 2 user", group1))  # False
