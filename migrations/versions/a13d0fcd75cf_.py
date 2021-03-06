"""empty message

Revision ID: a13d0fcd75cf
Revises: ece57eecf468
Create Date: 2020-04-15 17:02:34.595219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a13d0fcd75cf'
down_revision = 'ece57eecf468'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'completed',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'completed',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###
