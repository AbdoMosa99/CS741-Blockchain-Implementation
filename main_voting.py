from typing import List
from cs741_blockchain.pos_consensus.pos_chain import POS_Blockchain
from cs741_blockchain import Node
from cs741_blockchain.pos_consensus.voting import Voting


def main():
    network: List[Node] = []
    node_mostafa = Node('Mostafa', '0.0.0.1', 100, network)
    node_ahmed = Node('Ahmed', '0.0.0.3', 100, network)
    node_shahin = Node('shahin', '0.0.0.4', 100, network)


    network.append(node_mostafa)
    network.append(node_ahmed)
    network.append(node_shahin)

    node_mostafa.blockchain = POS_Blockchain(node_mostafa)
    node_ahmed.blockchain = POS_Blockchain(node_ahmed)
    node_shahin.blockchain = POS_Blockchain(node_shahin)

    bits = [20, 15, 10]
    vote = Voting(network, bits)

    vote.get_result()

    vote.network_coins()




if __name__ == '__main__':
    main()