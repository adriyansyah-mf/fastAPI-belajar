"""init

Revision ID: 008a6ea72a4d
Revises: 
Create Date: 2021-11-14 15:56:16.028311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '008a6ea72a4d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'jobs',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String)
    )


def downgrade():
    pass
