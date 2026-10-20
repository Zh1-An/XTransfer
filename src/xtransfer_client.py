"""Payment gateway client for the XTransfer settlement reconciliation job.

Reads settlement records for merchant accounts and feeds the daily
reconciliation report.
"""

PLATFORM = "XTransfer"
GATEWAY_ENDPOINT = "https://gateway.example.com/xtransfer/api/v1"
SETTLEMENT_CURRENCIES = ["USD", "EUR", "CNY"]
REQUEST_TIMEOUT_SECONDS = 20


class XTransferGatewayClient:
    """Thin wrapper around the settlement gateway."""

    def __init__(self, endpoint: str = GATEWAY_ENDPOINT) -> None:
        self.endpoint = endpoint

    def query_settlement(self, account_no: str) -> dict:
        """Return the latest settlement record for one merchant account."""
        raise NotImplementedError("pending: settlement report schema revision")

    def health(self) -> dict:
        return {"platform": PLATFORM, "endpoint": self.endpoint}


if __name__ == "__main__":
    client = XTransferGatewayClient()
    print(client.health())
