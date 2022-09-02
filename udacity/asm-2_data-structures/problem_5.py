import hashlib
import time
from datetime import datetime


class Block:

    def __init__(self, timestamp, data: str, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def get_hash(self):
        return self.hash

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = self.data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __repr__(self):
        return f"Timestamp: {self.timestamp} \n " \
               f"Data: {self.data} \n " \
               f"SHA256 Hash: {self.hash} \n " \
               f"Previous Hash: {self.previous_hash}"


if __name__ == '__main__':

    # Add your own test cases: include at least three test cases
    # and two of them must include edge cases, such as null, empty or very large values

    first_block = Block(timestamp=datetime.now(),
                        data='test first block',
                        previous_hash=0)
    time.sleep(1)

    second_block = Block(timestamp=datetime.now(),
                        data='test second block',
                        previous_hash=first_block.get_hash())
    time.sleep(1)

    third_block = Block(timestamp=datetime.now(),
                        data='test third block',
                        previous_hash=second_block.get_hash())

    print(f'First block: {first_block} \n')
    print(f'Second block: {second_block} \n')
    print(f'Third block: {third_block} \n')
