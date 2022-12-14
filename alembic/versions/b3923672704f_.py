"""empty message

Revision ID: b3923672704f
Revises: 256c4177a6c9
Create Date: 2022-09-09 18:54:36.171392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3923672704f'
down_revision = '256c4177a6c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('codes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('reset_code', sa.String(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('expired_in', sa.TIMESTAMP(timezone=True), server_default='now()', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_codes_id'), 'codes', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_codes_id'), table_name='codes')
    op.drop_table('codes')
    # ### end Alembic commands ###
