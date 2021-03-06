import bottle
from sowrong import batch


app = bottle.Bottle()


@batch(app.get("/do/<x>"))
def do(x):
    yield from big_task(x)


app.run()
