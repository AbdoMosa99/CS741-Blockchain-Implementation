
from cs741_blockchain.interface.chain import Blockchain


class POB_Blockchain(Blockchain):
    def proof(self, candidates, burned_coins):
        winner = None
        max_burned_coins = 0
        for candidate, coins in zip(candidates, burned_coins):
            candidate.n_coins -= coins
            if coins > max_burned_coins:
                winner = candidate
                max_burned_coins = coins
        return winner
