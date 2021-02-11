"""empty message

Revision ID: 307046f9332d
Revises: 
Create Date: 2021-02-10 12:02:16.901823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '307046f9332d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_text',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_text')
    # ### end Alembic commands ###
