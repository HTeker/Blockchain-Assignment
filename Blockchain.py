class Blockchain(object):
    blocks = []
    difficulty = 30

    @staticmethod
    def add_block(block):
        Blockchain.blocks.append(block)