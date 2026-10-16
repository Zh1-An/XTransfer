# SYNTHETIC TEST DATA - not a real leak. All identifiers are fabricated test fixtures.
# This file is a synthetic canary fixture for authorized internal detection validation.

"""Draft payment gateway client extracted from an internal service.

Platform identifier: XTransfer
"""

PLATFORM = "XTransfer"
GATEWAY_ENDPOINT = "https://gateway.internal.example.com/xtransfer/api/v1"
SETTLEMENT_CURRENCIES = ["USD", "EUR", "CNY"]


class XTransferGatewayClient:
    """Minimal stub used as a synthetic leak fixture. No real logic."""

    def __init__(self, endpoint: str = GATEWAY_ENDPOINT) -> None:
        self.endpoint = endpoint

    def query_settlement(self, account_no: str) -> dict:
        raise NotImplementedError("synthetic fixture - no real implementation")


if __name__ == "__main__":
    client = XTransferGatewayClient()
    print(PLATFORM, client.endpoint)
