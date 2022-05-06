from cs741_blockchain.pos_consensus.pos_chain import POS_Blockchain


class Voting:
    def __init__(self, network, bits):
        self.network = network
        self.bits = bits
        self.Candidates = []
        self.Candidate()
        self.take_vote()

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


    def take_vote(self):
        print(f"{self.Candidates}\n")

        for node in self.network:
            print(f"\n{node.name} Vote to the best\n")
            while True:
                try:
                    vote = int(input("Enter your vote: "))
                    break
                except Exception as e: 
                    print("Enter number input!")

            winner = node.blockchain.proof(candidates=self.network, bets=self.bits)
            node.blockchain.add_block([(node.name, vote)], winner)
        print('--------------------------------------')
        winner.blockchain.print()
        print('--------------------------------------')




    def get_result(self, blockchain: POS_Blockchain):
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

