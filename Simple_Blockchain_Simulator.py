#Simple Blockchain Simulator
#Adam Flick
#02/09/2025
#test

import hashlib
from datetime import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        """Constructor with defined parameters and attributes"""
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()  # Generates the block's unique hash

    def calculate_hash(self):
        """ Generates a SHA-256 hash of the block’s contents."""
        block_contents = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_contents.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [] #stores all blocks
        self.chain.append(self.create_genesis_block()) #Adds the first block

    def create_genesis_block(self):
        """A method that creates the first block (Genesis Block)."""
        return Block(0, "2025-02-07 06:00:00", "Genesis Block", "0")

    def add_block(self, data):
        """A method that adds a new block to the blockchain."""
        last_block = self.chain[-1]  # Get the last block
        new_block = Block(last_block.index + 1, datetime.now(), data, last_block.hash)
        self.chain.append(new_block)  # Append to the chain

        print(f"Block Index: {new_block.index}")
        print(f"Timestamp: {new_block.timestamp}")
        print(f"Data: {new_block.data}")
        print(f"Previous Hash: {new_block.previous_hash}")
        print(f"Hash: {new_block.hash}")  # Display the computed hash for the block

    def print_chain(self):
        """A method that prints all blocks in the blockchain."""
        print("\n========== BLOCKCHAIN ==========")
        for block in self.chain:  # Loop through the blockchain
            print("\n----------------------")
            print(f"Block Index: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print("----------------------")
        print("\n========== END OF BLOCKCHAIN ==========")

    def run_cli(self):
       """Method that runs a simple command line interface for the blockchain"""
       while True:
           print("\nSimple Blockchain Simulator")
           print("--------------------------")
           print("1. View Blockchain")
           print("2. Add New Block")
           print("3. Exit")

           choice = input("Enter Your Choice: ")

           if choice == "1":
               self.print_chain()
           elif choice == "2":
               print("\nAdding a New Block...")
               print("Enter transaction details in this format:")
               print("'Alice sent 2 BTC to Bob'")
               data = input("Transaction Data: ")
               if data.strip():
                   self.add_block(data)
           elif choice == "3":
               print("Exiting Blockchain Simulator....")
               break
           else:
               print("Invalid Choice. Please selects 1, 2, or 3.")


# Create a blockchain instance and start the CLI
my_blockchain = Blockchain()
my_blockchain.run_cli()  # Call this to start the menu

# Add some blocks
#my_blockchain.add_block("Second Block Data")
#my_blockchain.add_block("Third Block Data")

# View all transactions
#my_blockchain.print_chain()
