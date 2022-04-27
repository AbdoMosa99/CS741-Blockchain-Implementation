from datetime import datetime
import hashlib
from typing import List

from cs741_blockchain.interface.transaction import Transaction


class Block:
    def __init__(self, created_by):
        self.creation_time: datetime = datetime.now()
        self.seal_time: datetime = None
        self.transactions: List[Transaction] = []
        self.prev_hash: str = ""
        self.hash: str = ""
        self.create_by = created_by

    def _hash_block(self):
        self.hash = hashlib.sha256(
            bytearray(
                str(self.prev_hash)
                + str(self.creation_time)
                + str(self.seal_time)
                + "".join([t.hash for t in self.transactions]),
                "utf-8"
            )
        ).hexdigest()

    def add_transaction(self, transaction_data):
        transaction = Transaction(transaction_data)
        if self.transactions:
            transaction.prev_hash = self.transactions[-1].hash

        transaction.seal()
        self.transactions.append(transaction)

    def seal(self):
        self.seal_time = datetime.now()
        self._hash_block()

    def validate(self):
        for i, transaction in enumerate(self.transactions):
            try:
                transaction.validate()
                if (i > 0 and
                        transaction.prev_hash != self.transactions[i-1].hash):
                    raise Exception(
                        f"Transaction #{i} has invalid message link."
                    )
            except Exception as e:
                raise Exception(f"Invalid Block: {e} In block: {str(self)}")

