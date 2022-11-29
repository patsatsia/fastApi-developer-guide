"""Add columnt author to blog model

Revision ID: 4b1f9337571c
Revises: 59cf1e99ab04
Create Date: 2022-11-29 21:47:04.270612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b1f9337571c'
down_revision = '59cf1e99ab04'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('author_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'blog', 'user', ['author_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'blog', type_='foreignkey')
    op.drop_column('blog', 'author_id')
    # ### end Alembic commands ###