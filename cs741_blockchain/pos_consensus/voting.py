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
        self.Candidate()
        self.take_vote()

    def Candidate(self):
        while True:
            try:
                print("#############################################################\n")
                print("########### Hello in our Voting app [Glass App] #############\n")
                print("#############################################################\n\n")

                print("(First) let's add the candidates.\n")
                num_candidates = int(input('Number of candidates: '))
                
                print('\nEnter the Candidates:')
                for i in range(1, num_candidates+1):
                    Candidate = input(f"{i}> ")
                    self.Candidates.append({ "id_Candidate" : i, "name_Candidate": Candidate})

                print("\n#############################################################\n")

                return True
            except:
                print("\nSomething went wrong try again!\n")

    def take_vote(self):
        cities = []
        while True:
            try:
                print("\n\n(Second), let's add the cities in which the voting will occur\n")
                num_cities = int(input('Number of Cities: '))

                print("\nEnter the City")
                for i in range(1, num_cities+1):
                    city = input(f"{i}> ")
                    cities.append(city)

                print("\n#############################################################\n")

                break
            except:
                print("\nSomething went wrong try again!\n")

        while True:
            try:
                print("\n\n(Now) it's time to vote.")
                print(f"The candidates is {self.Candidates}.\n")
                for city in cities:    
                    votes = []    
                    num_voters = int(input(f'Number of the Voters in {city}: '))
            
                    print(f"\n{city} Vote to the best:")
                    for i in range(1, num_voters+1):
                        try:
                            id_voter = int(input(f"\nId ({i})> "))
                            vote = int(input("vote>  "))
                            votes.append({'id_voter': id_voter, 'vote': vote, 'city': city})

                        except Exception as e: 
                            print("Vote canceled!")

                    self.winner = POS_Blockchain.proof(validators=self.network, bets=self.bits)
                    self.winner.blockchain.add_block(votes)
                    
                    print('--------------------------------------')
                    self.winner.blockchain.print()
                    print('--------------------------------------')

                print("\n#############################################################\n")

                break
            except Exception as e:
                print(f"Something went wrong try again!\n {e}")

    

    def get_result(self):
        
        df = pd.DataFrame(columns=['id_voter', 'vote', 'city'])
        self.winner.blockchain.resolve_conflicts()

        for block in self.winner.blockchain.chain[1:]:
            transactions = block.transactions
            for transaction in transactions:
                data = transaction.data

                df = self.canceled_vote(data, df)

        print("\n\nSome of the voters voted:")
        for i, row in df.iterrows():
            print(f"{row['id_voter']} from {row['city']} is vote to {row['vote']}.")

        print("\n----------------------------")
        
        print("\nThe result to every city:")
        df_to_cities = df.groupby(['vote', 'city'])['vote'].count().to_frame(name = 'count')

        for i, row in df_to_cities.iterrows():
            print(f"In {i[1]}, {i[0]} got {row['count']} votes.")

        print("\n----------------------------")

        print("\nThe final result")
        df_total = df.groupby('vote')['vote'].count().to_frame(name = 'count')

        df_total.sort_values(by='count', ascending=False, inplace = True)

        for i, row in df_total.iterrows():
            print(f"{i} got {row['count']} votes.")

        print('\n--------------------------')

  
        winner = df_total.drop(["canceled"]).idxmax()
        print(f'The winner is {winner[0]}.')

        print("\n#############################################################\n")
        
        plt.pie(df_to_cities['count'], labels = df_to_cities.index, startangle = 90, autopct = lambda pct: self.func(pct, df_to_cities['count']))
        plt.show() 

        plt.pie(df_total['count'], labels = df_total.index, startangle = 90, autopct = lambda pct: self.func(pct, df_total['count']))
        plt.show() 

    
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
            data['vote'] = list(filter(lambda item: item['id_Candidate'] == data['vote'], self.Candidates))[0]["name_Candidate"]

        df = df.append(data, ignore_index=True)

        return df

