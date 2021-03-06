"""empty message

Revision ID: 102bbf265d4
Revises: 3d1138bbc68
Create Date: 2015-06-12 01:35:12.398937

"""

# revision identifiers, used by Alembic.
revision = '102bbf265d4'
down_revision = '3d1138bbc68'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('openid', sa.String(length=200), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'openid')
    ### end Alembic commands ###
