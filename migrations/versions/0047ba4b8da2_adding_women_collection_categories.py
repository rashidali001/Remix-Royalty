"""Adding women collection categories

Revision ID: 0047ba4b8da2
Revises: 24afb2904f26
Create Date: 2023-07-19 09:57:59.813835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0047ba4b8da2'
down_revision = '24afb2904f26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blouse',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('barcode_no', sa.String(length=20), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('womenscollection', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['womenscollection'], ['womenscollection.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blouse')
    # ### end Alembic commands ###
