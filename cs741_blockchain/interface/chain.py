from typing import List, Set

from interface.block import Block


class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.nodes: Set = {}

        initial_block = Block(0)
        self.add_block(initial_block)

    def add_block(self, block: Block):
        """
        Adds a block to the end of the chain
        :param block: <Block> the block object to add
        """
        if len(self.chain) > 0:
            block.prev_hash = self.chain[-1].hash
        block.seal()
        block.validate()
        self.chain.append(block)

    def validate(self) -> bool:
        """
        validate all blocks inside the chain
        :return: <bool> True when succeeded
        """
        for i, block in enumerate(self.chain):
            try:
                block.validate()
            except Exception as e:
                raise Exception(
                    f"Invalid Blockchain: at block number {i} "
                    f"caused by: {str(e)}."
                )
        return True

    def proof(self):
        pass

    def resolve_conflicts(self):
        pass

    def __repr__(self):
        return f"<Blockchain(chain: {self.chain})"
