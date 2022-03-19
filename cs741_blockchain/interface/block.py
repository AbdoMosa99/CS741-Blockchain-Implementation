from datetime import datetime
import hashlib
import time


class Block:
	def __init__(self, prev_hash):
		self.timestamp = datetime.now()
		self.transactions = []
		self.prev_hash = prev_hash
		self.hash = ''

	def _hash_block(self):
		self.hash =  hashlib.sha256(bytearray(
			str(self.prev_hash) 
			+ str(self.timestamp) 
			+ self.transactions[-1].hash, 
		"utf-8")).hexdigest()

	def add_transaction(self, transaction):
		self.transactions.append(transaction)

	def link(self, block):
		self.prev_hash = block.hash

	def seal(self):
		self.timestamp = time.time()
		self._hash_block()

	def validate(self):
		for i, transaction in enumerate(self.transactions):
			try:
				transaction.validate()
				if i > 0 and transaction.prev_hash != self.transactions[i-1].hash:
					raise Exception(f"Transaction #{i} has invalid message link.")
			except Exception as e:
				raise Exception(f"Invalid Block: {e} In block: {str(self)}")

	def __repr__(self):
		return f"Block<hash: {self.hash}, prev_hash: {self.prev_hash}, messages: {self.transactions}, time: {self.timestamp}>"
