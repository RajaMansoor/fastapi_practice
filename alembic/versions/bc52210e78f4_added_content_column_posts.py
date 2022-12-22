"""added content column->posts

Revision ID: bc52210e78f4
Revises: 4f9abc128acb
Create Date: 2022-12-21 13:08:51.081872

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc52210e78f4'
down_revision = '4f9abc128acb'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
