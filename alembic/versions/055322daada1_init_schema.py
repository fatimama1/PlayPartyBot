"""init schema

Revision ID: 055322daada1
Revises:
Create Date: 2025-11-02 12:53:10.312580
"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "055322daada1"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    # --- USERS ---
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("tg_id", sa.Integer(), unique=True, nullable=False),
        sa.Column("balance", sa.Integer(), nullable=False, default=500),
    )

    # --- EVENTS ---
    op.create_table(
        "events",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("time", sa.String(), nullable=False),
    )

    # --- PARTICIPANTS ---
    op.create_table(
        "participants",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("tg_id", sa.Integer(), sa.ForeignKey("users.tg_id")),
        sa.Column("event_id", sa.Integer(), sa.ForeignKey("events.id")),
        sa.Column("is_going", sa.Boolean(), default=True),
    )

    # --- BETS ---
    op.create_table(
        "bets",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("tg_id", sa.BigInteger(), sa.ForeignKey("users.tg_id"), index=True),
        sa.Column("bet", sa.Integer(), nullable=False),
        sa.Column("win", sa.Boolean(), nullable=False),
        sa.Column(
            "timestamp", sa.DateTime(timezone=True), server_default=sa.func.now()
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("bets")
    op.drop_table("participants")
    op.drop_table("events")
    op.drop_table("users")
