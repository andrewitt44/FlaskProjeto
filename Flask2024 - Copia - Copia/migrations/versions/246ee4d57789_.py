"""empty message

Revision ID: 246ee4d57789
Revises: 2820f842dcb2
Create Date: 2024-04-30 11:44:09.730592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '246ee4d57789'
down_revision = '2820f842dcb2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contato', schema=None) as batch_op:
        batch_op.add_column(sa.Column('comentario', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contato', schema=None) as batch_op:
        batch_op.drop_column('comentario')

    # ### end Alembic commands ###