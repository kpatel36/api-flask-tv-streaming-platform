"""empty message

Revision ID: a190a910bc82
Revises: 
Create Date: 2022-03-17 23:58:31.697337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a190a910bc82'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('television_series',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('show_title', sa.String(length=150), nullable=False),
    sa.Column('seasons', sa.Integer(), nullable=True),
    sa.Column('mpaa_rating', sa.String(length=10), nullable=True),
    sa.Column('genre', sa.String(length=50), nullable=False),
    sa.Column('network', sa.String(length=50), nullable=True),
    sa.Column('language', sa.String(length=50), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('television_series')
    # ### end Alembic commands ###
