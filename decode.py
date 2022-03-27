from flask_restful import Resource, reqparse
import base64

encode_post_args = reqparse.RequestParser()
encode_post_args.add_argument("message", type=str, help="Message to be encoded")


class Decode16(Resource):
    def post(self):
        message = encode_post_args.parse_args()["message"]
        output = base64.b32decode(message.encode('ascii')).decode('ascii')
        return output


class Decode32(Resource):
    def post(self):
        message = encode_post_args.parse_args()["message"]
        output = base64.b32decode(message.encode('ascii')).decode('ascii')
        return output


class Decode64(Resource):
    def post(self):
        message = encode_post_args.parse_args()["message"]
        output = base64.b64decode(message.encode('ascii')).decode('ascii')
        return output
