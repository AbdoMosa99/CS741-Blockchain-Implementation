from typing import List
from cs741_blockchain.pos_consensus.pos_chain import POS_Blockchain
from cs741_blockchain import Node
from cs741_blockchain.pos_consensus.voting import Voting


def main():
    # Creating network of nodes
    network: List[Node] = []
    node_mosa = Node('Mosa', '0.0.0.1', 20, network)
    node_amin = Node('Amin', '0.0.0.2', 100, network)
    node_ahmed = Node('Ahmed', '0.0.0.3', 100, network)
    node_shahin = Node('shahin', '0.0.0.4', 100, network)


    network.append(node_mosa)
    network.append(node_amin)
    network.append(node_ahmed)
    network.append(node_shahin)

    node_mosa.blockchain = POS_Blockchain(node_mosa)
    node_amin.blockchain = POS_Blockchain(node_amin)
    node_ahmed.blockchain = POS_Blockchain(node_ahmed)
    node_shahin.blockchain = POS_Blockchain(node_shahin)
	
    bits = [5, 15, 10, 3]
    vote = Voting(network, bits)

    vote.get_result(node_amin.blockchain)




if __name__ == '__main__':
    main()