from flask import g
from . import app
import .models


@app.before_request
def before_request():
    g.user = None
    if 'openid' in session:
        g.user = models.User.query.filter_by(openid=session['openid']).first()
