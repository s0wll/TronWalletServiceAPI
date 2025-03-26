"""add wallet_info

Revision ID: f6bf0fc62dcd
Revises:
Create Date: 2025-03-26 19:27:44.902278

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "f6bf0fc62dcd"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "wallet_info",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("address", sa.String(), nullable=False),
        sa.Column("bandwidth", sa.Float(), nullable=False),
        sa.Column("energy", sa.Float(), nullable=False),
        sa.Column("balance", sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("wallet_info")
