def has_permission(page):
    def inner(username):
        if username == 'Admin':
            return "'{0}' does have access to {1}.".format(username, page)
        else:
            return "'{0}' does NOT have access to {1}.".format(username, page)

    # you can return a inner function from outer function
    return inner


current_user = has_permission('Admin Area')
print(current_user('Admin'))
