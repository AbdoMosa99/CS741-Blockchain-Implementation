from typing import List
from cs741_blockchain.pos_consensus.pos_chain import POS_Blockchain
from cs741_blockchain import Node
from cs741_blockchain.pos_consensus.voting_test import Voting
import random
import time
import math


def main():
    num_votes = int(input("num_votes: "))
    
    network: List[Node] = []
    node_mostafa = Node('Mostafa', '0.0.0.1', 100, network)
    node_ahmed = Node('Ahmed', '0.0.0.2', 100, network)
    node_manar = Node('manar', '0.0.0.3', 100, network)


    network.append(node_mostafa)
    network.append(node_ahmed)
    network.append(node_manar)

    node_mostafa.blockchain = POS_Blockchain(node_mostafa)
    node_ahmed.blockchain = POS_Blockchain(node_ahmed)
    node_manar.blockchain = POS_Blockchain(node_manar)

    start = time.time()

    bits = [20, 15, 10]
    vote_object = Voting(network, bits)

    vote_object.Candidate(["Ali", "Mohamed", "Gaber"])

    cities = ["Suez", "Cairo", "Alex"]
    votes = []


    for i in range(1, num_votes):
        id_voter = random.randint(1, num_votes)
        vote = random.randint(1, 3)
        city = random.choices(cities)[0]
        votes.append({'id_voter': id_voter, 'vote': vote, 'city': city})

    vote_object.take_vote(votes)

    vote_object.get_result()

    end = time.time() - start
        
    print(f"The time to create {num_votes} Votes in {math.ceil(num_votes / 5)} Blocks is: \n{end}")


if __name__ == '__main__':
    main()