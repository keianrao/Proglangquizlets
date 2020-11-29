
class IncorrectPasswordException(Exception):
    pass



##  %%  ##  %%  ##  %%  ##  %%  ##  %%  ##  %%  ##

def logged_in(username):
    return False;

def login(username, password):
    raise IncorrectPasswordException;
