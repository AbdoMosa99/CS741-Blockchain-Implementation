
from typing import List
from cs741_blockchain.pos_consensus.pos_chain import POS_Blockchain
from cs741_blockchain import Node


def main():
    # Creating network of nodes
    network: List[Node] = []
    node_mosa = Node('Mosa', '0.0.0.1', 20, network)
    node_amin = Node('Amin', '0.0.0.2', 100, network)

    network.append(node_mosa)
    network.append(node_amin)

    node_mosa.blockchain = POS_Blockchain(node_mosa)
    node_amin.blockchain = POS_Blockchain(node_amin)

    # initializing mosa nodes
    winner = node_mosa.blockchain.proof(candidates=network, bets=[5, 20])
    node_mosa.blockchain.add_block(['one', 'two'], winner)

    winner = node_mosa.blockchain.proof(candidates=network, bets=[10, 5])
    node_mosa.blockchain.add_block(['three', 'four'], winner)

    # amin adding
    winner = node_mosa.blockchain.proof(candidates=network, bets=[20, 20])
    node_amin.blockchain.add_block(['1', '2'], winner)

    winner = node_mosa.blockchain.proof(candidates=network, bets=[0, 50])
    node_amin.blockchain.add_block(['3', '4'], winner)

    node_amin.blockchain.print()


if __name__ == '__main__':
    main()
