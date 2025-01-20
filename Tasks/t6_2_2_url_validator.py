import webbrowser


def validator(func):
    def wrapper(url):
        print('Before')
        if '.' in url:
            func(url)
        else:
            print('Wrong link')
        func(url)
        print('After')
    return wrapper

@validator
def open_url(url):
    webbrowser.open(url)


open_url('https://itproger.com/ua')
