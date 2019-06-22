from aiohttp import web
import asyncio

request_q = asyncio.Queue()
response_q = asyncio.Queue()
handling_something = False


class Method:
    def __init__(self, method):
        self.method = method
        self.last_response = None
        self.url = None

    def __call__(self, url):
        self.url = url
        return self

    def __aiter__(self):
        return self

    async def __anext__(self):
        global request_q, response_q
        if self.last_response is not None:
            await response_q.put(self.last_response)
            self.last_response = None
            raise StopAsyncIteration
        else:
            try:
                req_resp = request_q.get_nowait()
            except asyncio.QueueEmpty:
                raise StopAsyncIteration
            else:
                req, resp = req_resp
                if req.path == self.url:
                    self.last_response = resp
                    return req_resp
                else:
                    await request_q.put(req_resp)
                    raise StopAsyncIteration


async def handle(request):
    global handling_something
    while handling_something:
        await asyncio.sleep(0.1)
    handling_something = True
    response = web.Response(text="")
    await request_q.put((request, response))
    await request.app["sowrong"]()
    response = await response_q.get()
    handling_something = False
    return response


def run(sowrong_app):
    app = web.Application()
    app["sowrong"] = sowrong_app
    app.add_routes([web.get("/{url:.*}", handle), web.get("/{name}", handle)])

    web.run_app(app)


GET = Method("GET")
