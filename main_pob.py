
from datetime import datetime
from random import randint
import time
from typing import List
from cs741_blockchain import Node
from cs741_blockchain.pob_consensus.pob_chain import POB_Blockchain
from cs741_blockchain.pob_consensus.post import Post


def main():
    # Creating network of nodes
    network: List[Node] = []
    node1 = Node('Node1', '0.0.0.1', 70, network)
    node2 = Node('Node2', '0.0.0.2', 100, network)

    network.append(node1)
    network.append(node2)

    node1.blockchain = POB_Blockchain(node1)
    node2.blockchain = POB_Blockchain(node2)

    # initializing node1 nodes
    post = Post(
        author="Nelson Mandela",
        content="The greatest glory in living lies not in never falling, \
            but in rising every time we fall.",
        time=str(datetime(1918, 7, 18)),
        tags=['life', 'motivation'],
    )
    winner = node1.blockchain.proof(network, [randint(0, 5) for _ in network])
    node1.blockchain.add_block([post], winner)

    post = Post(
        author="Walt Disney",
        content="The way to get started is to quit talking and begin doing.",
        time=str(datetime(1901, 12, 5)),
        tags=['wisdom', 'motivation'],
    )
    winner = node1.blockchain.proof(network, [randint(0, 5) for _ in network])
    node1.blockchain.add_block([post], winner)

    # node2 adding
    post = Post(
        author="Steve Jobs",
        content="Your time is limited, so don't waste it living someone \
            else's life.",
        time=str(datetime(1955, 2, 24)),
        tags=['life', 'motivation'],
    )
    winner = node2.blockchain.proof(network, [randint(0, 5) for _ in network])
    node2.blockchain.add_block([post], winner)

    post = Post(
        author="John Lennon",
        content="Life is what happens when you're busy making other plans.",
        time=str(datetime(1940, 10, 9)),
        tags=['life', 'unmotivation '],
    )
    winner = node2.blockchain.proof(network, [randint(0, 5) for _ in network])
    node2.blockchain.add_block([post], winner)

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
