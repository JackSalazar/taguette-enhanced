"""add description to tags_directorys

Revision ID: 7e8fea7efb8f
Revises: 875fa0d1a76d
Create Date: 2026-05-05

"""
from alembic import op
import sqlalchemy as sa

revision = '7e8fea7efb8f'
down_revision = '875fa0d1a76d'
branch_labels = None
depends_on = None

def upgrade():
    with op.batch_alter_table('tags_directorys', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.Text(), nullable=True))

def downgrade():
    with op.batch_alter_table('tags_directorys', schema=None) as batch_op:
        batch_op.drop_column('description')