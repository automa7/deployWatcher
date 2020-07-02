from deployWatcher.Models.TransitionsModel import TransitionModel
from flask_restful import Resource, reqparse
from datetime import datetime


class Transitions(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('component', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('version', type=float, required=True, help="This field cannot be left blank!")
    parser.add_argument('author', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('status', type=str, required=True, help="This field cannot be left blank!")

    def get(self):
        return {'API': 'OK'}, 200

    def post(self):
        payload = Transitions.parser.parse_args()
        if payload.get('sent_timestamp') is not None:
            try:
                datetime.strptime(payload['sent_timestamp'], '%Y-%m-%d %H:%M:%S.%f')
            except ValueError:
                return {'message': 'Invalid date format. Expected format: %Y-%m-%d %H:%M:%S.%f'}, 500
        transition = TransitionModel(**payload)
        transition.save()

        return {'Status': 'POST for transition id: {} Succesful.'.format(transition.id)}, 200
