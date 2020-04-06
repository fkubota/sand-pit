from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

# Require a parser to parse our POST request.
print('----- begin python-----')
parser = reqparse.RequestParser()
parser.add_argument("arg01")


class MyApi(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)
        val_A = args['hello']
        val_val = val_A + 'api dekita'
        return {"AA": val_val}


api.add_resource(MyApi, "/myapi")

if __name__ == "__main__":
    app.run(debug=True)
