import bottle
from sowrong import batch


app = bottle.Bottle()


@batch(app.get("/do/<x>"))
def do(x):
    for i in range(int(x)):
        yield i


app.run()
