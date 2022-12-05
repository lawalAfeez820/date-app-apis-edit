"""empty message

Revision ID: 8a997037c27c
Revises: ceccaec6e120
Create Date: 2022-09-06 12:40:39.449436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a997037c27c'
down_revision = 'ceccaec6e120'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'image_url')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('image_url', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
