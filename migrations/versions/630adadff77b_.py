"""empty message

Revision ID: 630adadff77b
Revises: 
Create Date: 2019-04-09 23:04:52.257039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '630adadff77b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('coaches', sa.Column('deleted', sa.Boolean(), nullable=False, server_default=sa.schema.DefaultClause("0")))
    op.add_column('coaches', sa.Column('deleted_name', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('coaches', 'deleted_name')
    op.drop_column('coaches', 'deleted')
    # ### end Alembic commands ###