"""empty message

Revision ID: 75c523820d41
Revises: e4b2fcc4a2e4
Create Date: 2017-09-06 16:18:44.977000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75c523820d41'
down_revision = 'e4b2fcc4a2e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('public_info', sa.Column('update_time', sa.DateTime(), nullable=True))
    op.add_column('public_info', sa.Column('update_user', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('public_info', 'update_user')
    op.drop_column('public_info', 'update_time')
    # ### end Alembic commands ###
