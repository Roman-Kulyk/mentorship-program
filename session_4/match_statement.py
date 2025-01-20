"""The match statement initialized with the match keyword creating a block and
taking a parameter(her the name is also a parameter) and then steps down to the
various cases using the case keyword and the pattern, for the pattern to match
the parameter. The "_" is the wildcard character which is run when nothing is
matched.
"""

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


print(http_error(400))

print(http_error(404))

print(http_error(418))

print(http_error(500))


def what_i_am_going_to_do(action):
    match action:
        case 'running':
            return "I'm gonna to run"
        case 'sleeping':
            return "I'm gonna to sleep"
        case 'do exercises':
            return "I'm gonnat to do exercises"
        case _:
            return "I don't know what I'm gonna to do"


print(what_i_am_going_to_do('afgafg'))


print(what_i_am_going_to_do('running'))
