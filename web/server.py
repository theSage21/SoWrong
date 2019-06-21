from sowrong import GET, run


async def application():
    async for request, response in GET("/"):
        response.body = "hi"

    async for request, response in GET("/hello"):
        response.body = "world"


run(application)
