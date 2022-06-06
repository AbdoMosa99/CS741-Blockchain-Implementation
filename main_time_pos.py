import time
from typing import List
from cs741_blockchain.pos_consensus.pos_chain import POS_Blockchain
from cs741_blockchain import Node
import random



def main():
    # Creating network of nodes
    network: List[Node] = []
    node_Mostafa = Node('Mostafa', '0.0.0.1', 20, network)
    node_Mahrous = Node('Mahrous', '0.0.0.2', 100, network)
    node_Shahin = Node('Shahin', '0.0.0.2', 100, network)

    network.append(node_Mostafa)
    network.append(node_Mahrous)
    network.append(node_Shahin)

    node_Mostafa.blockchain = POS_Blockchain(node_Mostafa)
    node_Mahrous.blockchain = POS_Blockchain(node_Mahrous)
    node_Shahin.blockchain = POS_Blockchain(node_Shahin)

    start = time.time()    
    for i in range(0, 50000):
        tra = [x for x in range(1, random.randint(2, 101))]
        winner = POS_Blockchain.proof(validators=network, bets=[10, 20, 15])
        winner.blockchain.add_block(tra)

    end = time.time() - start
        
    print(f"The time to create 50K Block with random number of transaction (1 -> 100) is: \n{end}")



if __name__ == '__main__':
    main()
