from flask_restful import Resource


class IndexRouter(Resource):
    def get(self):
        return {
            'status': True,
            'message': 'Ok'
        }
