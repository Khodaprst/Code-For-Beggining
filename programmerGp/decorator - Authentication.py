users = {
    'Amir' : '1045421067',
    'mhmd' : 'Prince Of Darkeness',
    'heli' : 'Mew'
}

def authorized(func):
    def wrapper(name, password):
        if name in users.keys():
            if password == users[name]:
                return func(name, password)
        return 'Unknown Person'
    return wrapper

@authorized
def blog_getter(name, password):
    return 'this is your blog.'

@authorized
def comment_getter(name, password):
    return 'this is your comment.'

print(comment_getter('Amir', '1045421067'))