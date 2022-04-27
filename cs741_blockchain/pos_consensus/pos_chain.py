import random

from cs741_blockchain.interface.chain import Blockchain


class POS_Blockchain(Blockchain):
    def proof(self, candidates, bets):
        return random.choices(candidates, bets)[0]
