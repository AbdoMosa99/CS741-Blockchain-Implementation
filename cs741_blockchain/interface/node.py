
from typing import List

from cs741_blockchain.interface.chain import Blockchain


class Node:
    name: str = ""
    address: str = ""
    n_coins: int = 0
    network: List['Node'] = []

    blockchain: Blockchain = None

    def __init__(
            self, name: str, address: str,
            n_coins: int, network: List['Node']) -> None:
        self.name = name
        self.address = address
        self.n_coins = n_coins
        self.network = network
