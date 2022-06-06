
import random
from cs741_blockchain.interface.chain import Blockchain


class POS_Blockchain(Blockchain):

    @staticmethod
    def proof(validators, bets):
        return random.choices(validators, bets)[0]

