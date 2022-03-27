from flask_restful import Resource, reqparse
import base64

encode_post_args = reqparse.RequestParser()
encode_post_args.add_argument("message", type=str, help="Message to be encoded")


class Encode16(Resource):
    def post(self):
        message = encode_post_args.parse_args()["message"]
        output = base64.b16encode(message.encode()).decode()
        return output


class Encode32(Resource):
    def post(self):
        message = encode_post_args.parse_args()["message"]
        output = base64.b32encode(message.encode()).decode()
        return output


class Encode64(Resource):
    def post(self):
        message = encode_post_args.parse_args()["message"]
        output = base64.b64encode(message.encode()).decode()
        return output
