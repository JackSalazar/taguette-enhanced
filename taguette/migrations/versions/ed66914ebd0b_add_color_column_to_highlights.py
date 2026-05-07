"""add color column to highlights
Revision ID: ed66914ebd0b
Revises: c04102f5eddc
Create Date: 2026-04-30 15:19:57.991430
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ed66914ebd0b'
down_revision = 'c04102f5eddc'
branch_labels = None
depends_on = None

def upgrade():
    # Add color column to highlights
    with op.batch_alter_table('highlights', schema=None) as batch_op:
        batch_op.add_column(sa.Column('color', sa.String(length=20),
            server_default=sa.text("'yellow'"), nullable=True))

def downgrade():
    # Remove color column from highlights
    with op.batch_alter_table('highlights', schema=None) as batch_op:
        batch_op.drop_column('color')