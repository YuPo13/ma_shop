"""empty message

Revision ID: 82f2b445ff09
Revises: ff25e4d94a40
Create Date: 2020-01-09 12:44:37.447439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82f2b445ff09'
down_revision = 'ff25e4d94a40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'product_categories', ['uuid'])
    op.add_column('users', sa.Column('uuid', sa.String(length=35), nullable=False))
    op.create_unique_constraint(None, 'users', ['uuid'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'uuid')
    op.drop_constraint(None, 'product_categories', type_='unique')
    # ### end Alembic commands ###
