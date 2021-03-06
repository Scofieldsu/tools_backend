"""empty message

Revision ID: 0ad5001838f7
Revises: 2c39c89c3018
Create Date: 2017-07-26 11:00:03.783000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ad5001838f7'
down_revision = '2c39c89c3018'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('service', sa.Column('update_user', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'service', 'user', ['update_user'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'service', type_='foreignkey')
    op.drop_column('service', 'update_user')
    # ### end Alembic commands ###
