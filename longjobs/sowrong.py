import bottle
from functools import wraps


fn_list = {}


def batch(method, batch_size=10):
    def wrapper(fn):
        @wraps(fn)
        def new_fn(*a, **kw):
            sig = str(a) + str(kw)
            global fn_list
            if sig not in fn_list:
                fn_list[sig] = fn(*a, **kw)
            done = [i for i, _ in zip(fn_list[sig], range(batch_size))]
            if len(done) == 0:
                fn_list.pop(sig)
                return "ok"
            return bottle.redirect(bottle.request.url)

        new_fn = method(new_fn)
        return new_fn

    return wrapper
