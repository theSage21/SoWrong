from sowrong import GET, run


async def application():
    async for request, response in GET("/robot"):
        response.body = "🤖"

    async for request, response in GET("/hello"):
        response.body = "hello world."


run(application)
