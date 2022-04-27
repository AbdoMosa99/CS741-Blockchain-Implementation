import hashlib
import time


class Transaction:
    def __init__(self, data):
        self.hash = ''
        self.prev_hash = ''
        self.timestamp = time.time()
        self.size = len(str(data).encode('utf-8'))   # length in bytes
        self.data = data
        self.payload_hash = self._hash_payload()

    def _hash_payload(self):
        return hashlib.sha256(
            bytearray(
                str(self.timestamp)
                + str(self.data),
                "utf-8"
            )
        ).hexdigest()

    def _hash(self):
        return hashlib.sha256(
            bytearray(
                str(self.prev_hash)
                + self.payload_hash,
                "utf-8")
        ).hexdigest()

    def seal(self):
        self.hash = self._hash()

    def validate(self):
        if self.payload_hash != self._hash_payload():
            raise Exception(
                f"Invalid Transaction: payload hash don't match. "
                f"In {str(self)}."
            )
        if self.hash != self._hash():
            raise Exception(
                f"Invalid Transaction: hash don't match. "
                f"In  {str(self)}."
            )
