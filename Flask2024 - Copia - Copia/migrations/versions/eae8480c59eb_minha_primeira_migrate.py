"""minha primeira migrate

Revision ID: eae8480c59eb
Revises: 
Create Date: 2024-04-09 09:01:08.215972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eae8480c59eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contato',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_envio', sa.DateTime(), nullable=True),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('assunto', sa.String(), nullable=True),
    sa.Column('mensagem', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contato')
    # ### end Alembic commands ###
