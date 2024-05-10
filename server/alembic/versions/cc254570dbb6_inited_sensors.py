"""Inited sensors

Revision ID: cc254570dbb6
Revises: 42924feab5bd
Create Date: 2024-05-09 03:43:33.499444

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy.sql import table, column
from sqlalchemy import String, Text, Numeric


# revision identifiers, used by Alembic.
revision: str = 'cc254570dbb6'
down_revision: Union[str, None] = '42924feab5bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # SQL схема
    sensors = table('sensors',
                    column('sgid', String(64)),
                    column('name', String(255)),
                    column('description', Text),
                    column('latitude', Numeric),
                    column('longitude', Numeric))

    # Добавляем 2 датчика
    op.bulk_insert(sensors,
                   [
                       {'sgid': 'SENSOR_1', 'name': 'Test Sensor One', 'description': 'First sensor', 'latitude': 35.6895,
                        'longitude': 139.6917},
                       {'sgid': 'SENSOR_2', 'name': 'Test Sensor Two', 'description': 'Second sensor', 'latitude': 34.0522,
                        'longitude': -118.2437}
                   ])

def downgrade() -> None:
    op.execute("DELETE FROM sensors WHERE sgid IN ('SENSOR_1', 'SENSOR_2')")