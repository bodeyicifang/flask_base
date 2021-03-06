"""empty message

Revision ID: 976a4a68d2b6
Revises: 
Create Date: 2019-12-26 20:23:55.044834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '976a4a68d2b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gname', sa.String(length=80), nullable=True),
    sa.Column('gprice', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('gname')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('goods')
    # ### end Alembic commands ###
