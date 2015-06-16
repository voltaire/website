from flask import jsonify
from ..models import User
from . import ApiBase


class UserProfileAPI(ApiBase):
    def get(self, user_id):
        if user_id:
            profiles = User.query.all()
        else:
            profiles = User.query.filter_by(user_id=user_id).first()
        return jsonify(profiles)
