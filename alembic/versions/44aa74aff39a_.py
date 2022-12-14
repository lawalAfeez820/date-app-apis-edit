"""empty message

Revision ID: 44aa74aff39a
Revises: 46e05473aeb9
Create Date: 2022-09-10 21:50:31.004998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44aa74aff39a'
down_revision = '46e05473aeb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('gender', sa.String(), server_default='', nullable=True))
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('users', 'gender')
    # ### end Alembic commands ###
