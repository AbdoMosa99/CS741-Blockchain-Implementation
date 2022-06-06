from cs741_blockchain.interface.node import Node
from cs741_blockchain.pos_consensus.pos_chain import POS_Blockchain
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Voting:
    def __init__(self, network, bits):
        self.network = network
        self.bits = bits
        self.Candidates = []
        self.winner : Node = network[0]

    def Candidate(self, Candidates):
        count_id = 1
        for Candidate in Candidates:
            self.Candidates.append({ "id_Candidate" : count_id, "name_Candidate": Candidate})
            count_id += 1


    def take_vote(self, votes):
        count = 5
        votes_5 = []
        for vote in votes:
            votes_5.append(vote)
            count -= 1
            if count == 0 or vote == votes[-1]:
                self.winner = POS_Blockchain.proof(validators=self.network, bets=self.bits)
                self.winner.blockchain.add_block(votes_5)
                votes_5 = []

    def get_result(self):
        
        df = pd.DataFrame(columns=['id_voter', 'vote', 'city'])
        self.winner.blockchain.resolve_conflicts()

        for block in self.winner.blockchain.chain[1:]:
            transactions = block.transactions
            for transaction in transactions:
                data = transaction.data
                df = self.canceled_vote(data, df)
      
        print("\nThe result to every city:")
        df_to_cities = df.groupby(['vote', 'city'])['vote'].count().to_frame(name = 'count')

        for i, row in df_to_cities.iterrows():
            print(f"In {i[1]}, {i[0]} got {row['count']} votes.")

        print("\n----------------------------")

        print("\nThe final result")
        df_total = df.groupby('vote')['vote'].count().to_frame(name = 'count')

        for i, row in df_total.iterrows():
            print(f"{i} got {row['count']} votes.")

        print('\n--------------------------')

        print(df_total)

        winner = df_total.drop(["canceled"]).idxmax()

        print(f'The winner is {winner[0]}.')

        print("\n#############################################################\n")
        
        # plt.pie(df_to_cities['count'], labels = df_to_cities.index, startangle = 90, autopct = lambda pct: self.func(pct, df_to_cities['count']))
        # plt.show() 

        # plt.pie(df_total['count'], labels = df_total.index, startangle = 90, autopct = lambda pct: self.func(pct, df_total['count']))
        # plt.show() 

    
    def network_coins(self):
        print('\n------------------Network Coins------------------')
        for node_coin in self.network:
            print(f"{node_coin.name} has now: {node_coin.n_coins}")
        print('--------------------------------------------------\n')

    def func(self, pct, allvalues):
        absolute = int(pct / 100.*np.sum(allvalues))
        return "{:.1f}%\n({:d} Vote)".format(pct, absolute)

    def canceled_vote(self, data, df):
        if data["id_voter"] in df.id_voter.values or data["vote"] < 1 or data["vote"] > len(self.Candidates):
            data["vote"] = 'canceled'
        else:
            data['vote'] = list(
                                filter(lambda item: item['id_Candidate'] == data['vote'], self.Candidates)
                            )[0]["name_Candidate"]

        df = df.append(data, ignore_index=True)

        return df

