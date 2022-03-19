import hashlib
import time


class Transaction: 
	def __init__(self, data):
		self.hash = ''
		self.prev_hash = ''
		self.timestamp = time.time()
		self.size = len(data.encode('utf-8'))   # length in bytes
		self.data = data
		self.payload_hash = self._hash_payload()

	def _hash_payload(self):
		return hashlib.sha256(bytearray(
			str(self.timestamp) 
			+ str(self.data), 
		"utf-8")).hexdigest()

	def _hash(self):
		return hashlib.sha256(bytearray(
			str(self.prev_hash) 
			+ self.payload_hash, 
		"utf-8")).hexdigest()

	def link(self, transaction):
		self.prev_hash = transaction.hash

	def seal(self):
		self.hash = self._hash()

	def validate(self):
		if self.payload_hash != self._hash_payload():
			raise Exception(f"Invalid Transaction: payload hash don't match. In {str(self)}.")
		if self.hash != self._hash():
			raise Exception(f"Invalid Transaction: hash don't match. In  {str(self)}.")

	def __repr__(self):
		return f"Transaction<hash: {self.hash}, prev_hash: {self.prev_hash}, data: {self.data}>"
		