"""Adding the quantity field

Revision ID: 21a6332694e4
Revises: 19f98a104a04
Create Date: 2023-07-05 13:27:07.945534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21a6332694e4'
down_revision = '19f98a104a04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('jeans', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quantity', sa.Integer(), nullable=True))

    with op.batch_alter_table('shirts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quantity', sa.Integer(), nullable=True))

    with op.batch_alter_table('trousers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quantity', sa.Integer(), nullable=True))

    with op.batch_alter_table('tshirts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quantity', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tshirts', schema=None) as batch_op:
        batch_op.drop_column('quantity')

    with op.batch_alter_table('trousers', schema=None) as batch_op:
        batch_op.drop_column('quantity')

    with op.batch_alter_table('shirts', schema=None) as batch_op:
        batch_op.drop_column('quantity')

    with op.batch_alter_table('jeans', schema=None) as batch_op:
        batch_op.drop_column('quantity')

    # ### end Alembic commands ###
