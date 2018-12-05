from sanic import Sanic, response

hello_service = Sanic()

@hello_service.route("/sayhello", methods=['GET'])
async def index(request):
    return response.json("Hello, world!")

if __name__ == "__main__":
    hello_service.run(host="0.0.0.0", port=8000)