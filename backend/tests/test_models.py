from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from max_miles.models import Card, Transaction


def test_valid_transaction():
    transaction = Transaction(
        amount="25.50",
        currency="SGD",
        merchant="FairPrice",
        card=Card.DBS_YUU,
        timestamp=datetime.now(timezone.utc),
    )

    assert transaction.amount == 25.50
    assert transaction.card == Card.DBS_YUU


def test_negative_amount_rejected():
    with pytest.raises(ValidationError):
        Transaction(
            amount="-10.00",
            merchant="FairPrice",
            card=Card.DBS_YUU,
            timestamp=datetime.now(timezone.utc),
        )


def test_invalid_card_rejected():
    with pytest.raises(ValidationError):
        Transaction(
            amount="25.50",
            merchant="FairPrice",
            card="UNKNOWN_CARD",
            timestamp=datetime.now(timezone.utc),
        )
