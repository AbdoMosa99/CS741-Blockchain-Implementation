from interface.block import Block


class Blockchain:
	def __init__(self):
		self.blocks = []

	def add_block(self, block:Block):
		if len(self.blocks) > 0:
			block.prev_hash = self.blocks[-1].hash
		block.seal()
		block.validate()
		self.blocks.append(block)

	def validate(self):
		for i, block in enumerate(self.blocks):
			try:
				block.validate()
			except Exception as e:
				raise Exception(f"Invalid Blockchain: at block number {i} caused by: {str(e)}.")
		return True

	def __repr__(self):
		return f"Blockchain<blocks: {self.blocks}>"
