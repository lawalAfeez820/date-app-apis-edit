"""empty message

Revision ID: ee47a2c7ce06
Revises: 44aa74aff39a
Create Date: 2022-09-12 10:06:23.481771

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ee47a2c7ce06'
down_revision = '44aa74aff39a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('age', sa.String(), server_default='', nullable=False))
    op.drop_column('users', 'dob')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('dob', postgresql.TIMESTAMP(timezone=True), server_default=sa.text("'2022-09-06 11:32:27.839577+00'::timestamp with time zone"), autoincrement=False, nullable=False))
    op.drop_column('users', 'age')
    # ### end Alembic commands ###
