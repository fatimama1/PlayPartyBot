"""fill initial users

Revision ID: 414a148b555c
Revises: 055322daada1
Create Date: 2025-11-02 12:56:39.711432

"""

import os
from collections.abc import Sequence

from sqlalchemy.orm import Session

from alembic import op
from app.db.models.user import User

# revision identifiers, used by Alembic.
revision: str = "414a148b555c"
down_revision: str | Sequence[str] | None = "055322daada1"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade():
    bind = op.get_bind()
    session = Session(bind=bind)

    user_ids = os.getenv("USERS", "")
    ids = [int(x.strip()) for x in user_ids.strip("[]").split(",") if x.strip()]

    for tg_id in ids:
        user = User(tg_id=tg_id, balance=500)
        session.add(user)

    session.commit()


def downgrade():
    bind = op.get_bind()
    session = Session(bind=bind)

    user_ids = os.getenv("USERS", "")
    ids = [int(x.strip()) for x in user_ids.strip("[]").split(",") if x.strip()]

    session.query(User).filter(User.tg_id.in_(ids)).delete(synchronize_session=False)
    session.commit()
