import flask


class Auth():
    def __init__(self):
        pass

    def req_login(self, **okwargs):
        def inner_decorator(func):
            def inside(*args, **kwargs):
                def empty():
                    return flask.redirect(
                        '/login?r=' + func.__name__ + ' requires login&goto=' +
                        okwargs.get('route', str(flask.request.url_rule)))

                if (flask.request.headers['X-Replit-User-Id']):
                    return func(*args, **kwargs)
                else:
                    return okwargs.get('callback', empty)(*args, **kwargs)

            inside.__name__ = func.__name__
            return inside

        return inner_decorator
