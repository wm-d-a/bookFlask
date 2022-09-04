"""new fields in user model

Revision ID: 937bb600fa3c
Revises: f9e2a0c848f8
Create Date: 2022-09-04 15:04:13.379936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '937bb600fa3c'
down_revision = 'f9e2a0c848f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
