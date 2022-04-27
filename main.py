
from typing import List
from cs741_blockchain import Node
from cs741_blockchain.interface.chain import Blockchain


def main():
    # Creating network of nodes
    network: List[Node] = []
    node_mosa = Node('Mosa', '0.0.0.1', 20, network)
    node_amin = Node('Amin', '0.0.0.2', 100, network)

    network.append(node_mosa)
    network.append(node_amin)

    node_mosa.blockchain = Blockchain(node_mosa)
    node_amin.blockchain = Blockchain(node_amin)

    # initializing mosa nodes
    node_mosa.blockchain.add_block(['one', 'two'])
    node_mosa.blockchain.add_block(['three', 'four'])

    # amin adding
    node_amin.blockchain.add_block(['1', '2'])
    node_amin.blockchain.add_block(['3', '4'])

    node_amin.blockchain.print()


if __name__ == '__main__':
    main()
