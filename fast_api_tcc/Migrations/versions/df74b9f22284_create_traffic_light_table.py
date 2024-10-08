"""create Traffic_Light table

Revision ID: df74b9f22284
Revises: 
Create Date: 2024-07-25 08:30:54.838612

"""
from typing import Sequence, Union

from alembic import op

import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'df74b9f22284'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Traffic_Light',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('redDuration', sa.Integer(), nullable=False),
        sa.Column('greenDuration', sa.Integer(), nullable=False),
        sa.Column('cycleStartTime', sa.Integer(), nullable=False),
        sa.Column('creater_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Traffic_Light')
    # ### end Alembic commands ###
