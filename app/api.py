from flask_restful import Api
# importando as rotas
from app.routes.index_router import IndexRouter
from app.routes.auth_router import AuthRouter
from app.routes.auth_router import AuthRefreshRouter
from app.routes.user_router import UserRouter


api = Api(prefix="/api/v1")


# configurações da API
def configure_api(app):
    # injeção de rotas
    api.add_resource(IndexRouter, "/")
    api.add_resource(AuthRouter, "/auth")
    api.add_resource(AuthRefreshRouter, "/auth/refresh")
    api.add_resource(UserRouter, "/users",
                                 "/users/<int:page>/<int:page_size>",
                                 "/users/<string:email>")
    # inicializa flask_restful
    api.init_app(app)
