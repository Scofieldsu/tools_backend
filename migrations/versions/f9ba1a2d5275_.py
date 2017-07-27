"""empty message

Revision ID: f9ba1a2d5275
Revises: fefc39b2abc7
Create Date: 2017-07-27 20:10:48.210728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9ba1a2d5275'
down_revision = 'fefc39b2abc7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('service', sa.Column('visit_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('service', 'visit_count')
    # ### end Alembic commands ###
