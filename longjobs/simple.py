import bottle
from sowrong import batch


app = bottle.Bottle()


@app.get("/do/<x>")
def do(x):
    big_task(x)


app.run()
