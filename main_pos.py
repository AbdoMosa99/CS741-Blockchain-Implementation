
from typing import List
from cs741_blockchain.pos_consensus.pos_chain import POS_Blockchain
from cs741_blockchain import Node


def main():
    # Creating network of nodes
    network: List[Node] = []
    node_ali = Node('Ali', '0.0.0.1', 20, network)
    node_amin = Node('Amin', '0.0.0.2', 100, network)

    network.append(node_ali)
    network.append(node_amin)

    node_ali.blockchain = POS_Blockchain(node_ali)
    node_amin.blockchain = POS_Blockchain(node_amin)

    winner = POS_Blockchain.proof(validators=network, bets=[5, 20])
    winner.blockchain.add_block(['one', 'two'])

    winner = POS_Blockchain.proof(validators=network, bets=[10, 5])
    winner.blockchain.add_block(['three', 'four'])

    winner = POS_Blockchain.proof(validators=network, bets=[20, 20])
    winner.blockchain.add_block(['five', 'six', 'seven'])

    winner = POS_Blockchain.proof(validators=network, bets=[0, 50])
    winner.blockchain.add_block(['eight'])

    winner.blockchain.print()


if __name__ == '__main__':
    main()
