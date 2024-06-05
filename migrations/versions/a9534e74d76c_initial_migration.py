"""Initial migration

Revision ID: a9534e74d76c
Revises: e5be76199cee
Create Date: 2024-06-05 04:49:17.366767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9534e74d76c'
down_revision = 'e5be76199cee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=60),
               type_=sa.String(length=150),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=150),
               type_=sa.VARCHAR(length=60),
               existing_nullable=False)

    # ### end Alembic commands ###