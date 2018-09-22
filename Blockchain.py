class Blockchain(object):
    blocks = []
    difficulty = 3

    @staticmethod
    def add_block(block):
        Blockchain.blocks.append(block)