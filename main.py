
import time
from typing import List
from cs741_blockchain import Node
from cs741_blockchain.interface.chain import Blockchain


def main():
    # Creating network of nodes
    network: List[Node] = []
    node1 = Node('Node1', '0.0.0.1', 20, network)
    node2 = Node('Node2', '0.0.0.2', 100, network)

    network.append(node1)
    network.append(node2)

    node1.blockchain = Blockchain(node1)
    node2.blockchain = Blockchain(node2)

    # initializing node1 nodes
    node1.blockchain.add_block(['one', 'two'])
    node1.blockchain.add_block(['three', 'four'])

    # node2 adding
    node2.blockchain.add_block(['1', '2'])
    node2.blockchain.add_block(['3', '4'])

    node2.blockchain.print()


def tik():
    global start_time
    start_time = time.time()


def tok():
    global start_time
    time_interval = round(time.time() - start_time, 2)
    print("\nTook", time_interval, "seconds.")


if __name__ == '__main__':
    tik()
    main()
    tok()
