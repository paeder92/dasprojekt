"""empty message

Revision ID: 838ac323702b
Revises: 2c7692396886
Create Date: 2020-04-16 16:57:48.038656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '838ac323702b'
down_revision = '2c7692396886'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todolists', sa.Column('alldone', sa.Boolean(), nullable=True))
    op.execute('UPDATE todolists SET alldone = False WHERE alldone IS NULL;')

    op.alter_column('todolists', 'alldone', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todolists', 'alldone')
    # ### end Alembic commands ###
