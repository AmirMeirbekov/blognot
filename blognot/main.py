from aiohttp import web
import aiohttp_cors

from routes import setup_routes
from views.views import *


app = web.Application()
cors = aiohttp_cors.setup(app)
resource = cors.add(app.router.add_resource('/'))
route = cors.add(
    resource.add_route("GET", index), {
        "http://localhost:8000": aiohttp_cors.ResourceOptions(
            expose_headers="*",
            allow_headers="*",
        )
    })

web.run_app(app, host='0.0.0.0', port=8000)