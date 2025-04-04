"""empty message

Revision ID: 3342cf76a6ed
Revises: 
Create Date: 2025-03-30 15:51:02.681572

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '3342cf76a6ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cards',
    sa.Column('card_uid', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('front', sa.String(), nullable=False),
    sa.Column('back', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('card_uid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cards')
    # ### end Alembic commands ###
