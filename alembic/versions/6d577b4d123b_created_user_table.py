"""created user table

Revision ID: 6d577b4d123b
Revises: bc52210e78f4
Create Date: 2022-12-21 13:16:18.875616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d577b4d123b'
down_revision = 'bc52210e78f4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
            sa.Column('id',sa.Integer(),nullable = False),
            sa.Column('email',sa.String(),nullable = False),
            sa.Column('password',sa.String(),nullable = False),
            sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False),
            sa.PrimaryKeyConstraint('id'),
            sa.UniqueConstraint('email')
            )
    pass


def downgrade():
    op.drop_table('users')
    pass
