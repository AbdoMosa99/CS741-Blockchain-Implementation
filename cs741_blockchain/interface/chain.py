from abc import abstractmethod
from typing import List

from cs741_blockchain.interface.block import Block


class Blockchain:
    def __init__(self, created_by):
        self.chain: List[Block] = []
        self.owner = created_by

        self.add_block(['First Transaction'])

    def add_block(self, data_transactions: list, winner=None):
        """
        Adds a block to the end of the chain
        :param block: <Block> the block object to add
        """
        if not winner:
            winner = self.owner

        block = Block(winner)

        if self.chain:
            for data_transaction in data_transactions:
                block.add_transaction(data_transaction)
            winner.n_coins += 5
            self.resolve_conflicts()
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
                self.owner.n_coins -= 5
                raise Exception(
                    f"Invalid Blockchain: at block number {i} "
                    f"caused by: {str(e)}."
                )
        return True

    @abstractmethod
    def proof(self):
        pass

    def resolve_conflicts(self):
        #longest_chain = self.chain
        for node in self.owner.network:
            if len(node.blockchain.chain) > len(self.chain):
                if node.blockchain.validate():
                    #longest_chain = node.blockchain.chain
                    self.chain = node.blockchain.chain
                    

        #self.chain = longest_chain

    def print(self):
        print(f"Blockchain:")
        print(f"\tOwned by: {self.owner.name}")
        print(f"\tchain: [")
        for block in self.chain:
            print(f"\t\tBlock:")
            print(f"\t\t\tcreation_time: {block.creation_time}")
            print(f"\t\t\tcreated_by: {block.create_by.name}")
            print(f"\t\t\tprev_hash: {block.prev_hash[:6]}")
            print(f"\t\t\thash: {block.hash[:6]}")
            print(f"\t\t\ttransactions: [")
            for transaction in block.transactions:
                print("\t\t\t\tTransaction:")
                print(f"\t\t\t\t\thash: {transaction.hash[:6]}")
                print(f"\t\t\t\t\tprev_hash: {transaction.prev_hash[:6]}")
                print(f"\t\t\t\t\tdata: {transaction.data}")
            print(f"\t\t\t]")
            print(f"\t\t\tseal_time: {block.seal_time}")
        print(f"\t]")
