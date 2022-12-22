"""add column to post

Revision ID: af36038d2fae
Revises: 1c691c4200fd
Create Date: 2022-12-21 13:39:51.811011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af36038d2fae'
down_revision = '1c691c4200fd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('published',sa.Boolean(),nullable=False,server_default='TRUE'))
    op.add_column('posts',sa.Column('created_at', sa.TIMESTAMP(timezone=True),
    nullable=False,server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts', 'created_at')
    pass
