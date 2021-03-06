"""empty message

Revision ID: 4a4563cff76d
Revises: 
Create Date: 2021-02-04 17:44:59.790201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a4563cff76d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=120), nullable=True),
    sa.Column('lastname', sa.String(length=120), nullable=True),
    sa.Column('account_balance', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_accounts')
    # ### end Alembic commands ###
