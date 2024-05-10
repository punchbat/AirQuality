"""Migrating to db

Revision ID: 42924feab5bd
Revises: 67ea65546e7f
Create Date: 2024-05-09 03:43:24.497438

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42924feab5bd'
down_revision: Union[str, None] = '67ea65546e7f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sensors',
    sa.Column('sgid', sa.VARCHAR(length=64), nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('latitude', sa.NUMERIC(), nullable=False),
    sa.Column('longitude', sa.NUMERIC(), nullable=False),
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sensors_sgid'), 'sensors', ['sgid'], unique=True)
    op.create_table('users',
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('surname', sa.String(), nullable=True),
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('sensor_data',
    sa.Column('sensor_id', sa.UUID(), nullable=False),
    sa.Column('temperature', sa.FLOAT(), nullable=True),
    sa.Column('humidity', sa.FLOAT(), nullable=True),
    sa.Column('CO2', sa.FLOAT(), nullable=True),
    sa.Column('latitude', sa.NUMERIC(), nullable=True),
    sa.Column('longitude', sa.NUMERIC(), nullable=True),
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['sensor_id'], ['sensors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sensor_data')
    op.drop_table('users')
    op.drop_index(op.f('ix_sensors_sgid'), table_name='sensors')
    op.drop_table('sensors')
    # ### end Alembic commands ###
