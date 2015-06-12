from flask import jsonify, render_template
from flask.views import View
from .. import app


class ApiBase(View):
    methods = []

    @property
    def template(self):
        raise NotImplementedError()

    def get_objects(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.template, **context)

    def dispatch_request(self, **kwargs):
        response = {'objects': self.get_objects(**kwargs)}
        return jsonify(response)
