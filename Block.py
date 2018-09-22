import random
import hashlib

from Logger import logger
from Blockchain import Blockchain


class Block:
    index = None
    nonce = ""
    data = ""
    previousHash = ""
    hash = ""

    def __init__(self, previousHash = ""):
        self.index = len(Blockchain.blocks)
        self.data = input("Enter some data to add to the chain: ")
        self.previousHash = previousHash

        self.mine()

    def mine(self):
        logger.info("Mining block #" + str(self.index) + " at difficulty 5...")

        # if hash starts with Blockchain.difficulty number of 0's, the mining is done
        while not(self.hash[:Blockchain.difficulty].count("0") == Blockchain.difficulty):
            # Get random nonce
            self.nonce = str(random.randint(1, 100000))
            self.hash = hashlib.sha256((self.nonce + self.data).encode()).hexdigest()

        logger.info("Successfully mined block #" + str(self.index) + "!")
        print(self.hash)