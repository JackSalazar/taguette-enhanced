"""add color column to highlights

Revision ID: e6bbd7fcc45c
Revises: db5e31a0233d
Create Date: 2026-04-30 14:43:56.486353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6bbd7fcc45c'
down_revision = 'db5e31a0233d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('highlights', sa.Column('color', sa.Text(), nullable=False, server_default='#ffff00'))


def downgrade():
    op.drop_column('highlights', 'color')