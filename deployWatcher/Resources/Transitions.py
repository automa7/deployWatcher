from deployWatcher.Models.TransitionsModel import TransitionModel
from flask_restful import Resource, reqparse
from datetime import datetime

 
class Transitions(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('component', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('version', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('author', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('status', type=str, required=True, help="This field cannot be left blank!")

    @staticmethod
    def _validate_payload(payload_data):
        try:
            if payload.get('sent_timestamp') is not None:
                datetime.strptime(payload['sent_timestamp'], '%Y-%m-%d %H:%M:%S.%f')
            datetime.strptime(payload['receivedTimestamp'], '%Y-%m-%d %H:%M:%S.%f')
        except ValueError:
            return {'message': 'Invalid date format used. Expected format: %Y-%m-%d %H:%M:%S.%f'}, 500
        
        if isinstance(payload.get('component'), str):
            if len(payload.get('component')) > 140:
                return {'message': 'Component too big. Max 140 chars'}, 500
        else:
            return {'message': 'Component not a string'}, 500
        
        # if isinstance(payload.get('version'), float):
        #     pass
        # else:
        #     return {'message': 'Version must be a float.'}, 500
        
        return 0


    def post(self):
        payload = Transitions.parser.parse_args()
        
        try:
            if payload.get('sent_timestamp') is not None:
                datetime.strptime(payload['sent_timestamp'], '%Y-%m-%d %H:%M:%S.%f')
            datetime.strptime(payload['receivedTimestamp'], '%Y-%m-%d %H:%M:%S.%f')
        except ValueError:
            return {'message': 'Invalid date format. Expected format: %Y-%m-%d %H:%M:%S.%f'}, 500
        
        validation = self._validate_payload(payload_data=payload)
        
        if validation != 0:
            return validation

        transition = TransitionModel(**payload)
        transition.save()

        return {'Status': 'POST for transition id: {} Succesful.'.format(transition.id)}, 200
