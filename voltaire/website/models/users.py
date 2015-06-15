from sqlalchemy.dialects.postgresql import UUID
from .. import db
from . import Base


roles = db.Table(
    'roles',
    db.Column('role_id', UUID, db.ForeignKey('role.id')),
    db.Column('user_id', UUID, db.ForeignKey('user.id'))
)

socialmedianetworks = db.Table(
    'socialmedianetworks',
    db.Column('socialmedianetwork_id', UUID, db.ForeignKey('socialmedianetwork.id')),  # noqa
    db.Column('profile_id', UUID, db.ForeignKey('profile.id'))
)


class User(Base, db.Model):
    __tablename__ = 'user'
    openid = db.Column(db.String(200))
    profile = db.relationship('Profile', backref='user', lazy='dynamic',
                              uselist=False)
    roles = db.relationship('Role', backref=db.backref('user', lazy='dynamic'),
                            lazy='dynamic', secondary=roles)

    def __init__(self, openid):
        self.openid = openid


class Role(Base, db.Model):
    __tablename__ = 'role'
    name = db.Column(db.String(80), unique=True)

    def __init__(self, name):
        self.name = name


class SocialMediaNetwork(Base, db.Model):
    __tablename__ = 'socialmedianetwork'
    network = db.Column(db.String(10))
    username = db.Column(db.String(255))

    def __init__(self, network, username):
        self.network = network
        self.username = username


class Profile(Base, db.Model):
    __tablename__ = 'profile'
    username = db.Column(db.String(80), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    display_name = db.Column(db.String(80), index=True, unique=True)
    first_name = db.Column(db.String(80), index=True)
    last_name = db.Column(db.String(80), index=True)
    user_id = db.Column(UUID, db.ForeignKey('user.id'))
    social_media_networks = db.relationship(
        'SocialMediaNetwork', backref=db.backref('user', lazy='dynamic'),
        lazy='dynamic', secondary=socialmedianetworks)

    def __init__(self, username, email, first_name=None, last_name=None,
                 display_name=None, user_id=None, social_media_networks=None):
        self.username = username
        self.email = email
        if not display_name:
            self.display_name = username
        else:
            self.display_name = display_name
        self.first_name = first_name
        self.last_name = last_name

        self.social_media_networks = social_media_networks

        self.user_id = user_id
