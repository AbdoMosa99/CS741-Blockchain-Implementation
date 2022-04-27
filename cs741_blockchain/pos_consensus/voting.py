from pos_chain import Blockchain
import cs741_blockchain.pos_consensus.pos_chain as pos_chain


class Voting:
    def __init__(self, validators):
        self.validators = validators
        self.votes = []
        self.Candidates = []
        self.tr = []
        self.Candidate()

    def Candidate(self):
        print("Hello in our Voting app\n")
        i = 0
        while True:
            Candidate = input("Enter the Candidate: ")
            i += 1
            self.Candidates.append((i, Candidate))
            contin = input("Do you want to enter more?(y/n): ")
            if contin.lower() == 'y':
                continue
            else:
                break
        return True


    def take_2vote(self):
        print(f"\nVote to the best\n")
        print(f"{self.Candidates}\n")
        i = 2
        while i != 0:

            #try:
            id = int(input("Enter your id: "))
            vote = int(input("Enter your vote: "))


            self.votes.append((id, vote))
            print(self.votes)

            i -= 1
            if i != 0:
                contin = input("Do you want to enter more?(y/n): ")
                if contin.lower() == 'y':
                    continue
                else:
        
                    break
        winner = pos_chain.Pos(self.validators, self.votes)
        name = winner.get_winner()

        print(f"Done and The winner to create the block is: {name.get_Address()}\n")

        print(f"\nAnd his blockchain: {name}\n\n")
        self.votes = []
        return True

            #except Exception as e:
            #	print(e)
            #	print("Enter number input!")
            



    def get_result(self, blockchain: Blockchain):
        all_data = {}
        blockchain.resolve_conflicts()
        blocks = blockchain.chain
        for block in blocks[1:]:
            transactions = block.transactions
            for transaction in transactions:
                data = transaction.data
                all_data[data[1]] = all_data.get(data[1], 0) + 1

        print(f"The result is\n{all_data}")
        print(f"the winner is: {self.Candidates[max(all_data, key=all_data.get) - 1]}")




    def __repr__(self):
        return self.tr_votes

    def __str__(self):
        return f'{self.tr_votes}'

