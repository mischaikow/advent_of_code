import hashlib
from collections import deque


def find_triplet(hash: str) -> str | None:
    for i in range(2, len(hash)):
        if hash[i - 2] == hash[i - 1] == hash[i]:
            return hash[i]
    return None


def find_quint(hash: str, key: str) -> bool:
    for i in range(4, len(hash)):
        if hash[i - 4] == hash[i - 3] == hash[i - 2] == hash[i - 1] == hash[i] == key:
            return True
    return False


def part1(salt: str) -> int:
    hash_list = []
    pointer = 0
    key_count = 0
    while True:
        while pointer >= len(hash_list):
            new_hash = hashlib.md5((salt + str(pointer)).encode()).hexdigest()
            # For part 1, comment out the next two lines (and the two lines below)
            for _ in range(2016):
                new_hash = hashlib.md5(new_hash.encode()).hexdigest()
            hash_list.append(new_hash)

        search_char = find_triplet(hash_list[pointer])
        if search_char is not None:
            for forward in range(1, 1001):
                while pointer + forward >= len(hash_list):
                    new_hash = hashlib.md5(
                        (salt + str(pointer + forward)).encode()
                    ).hexdigest()
                    # For part 1, comment out the next two lines (and the two lines above)
                    for _ in range(2016):
                        new_hash = hashlib.md5(new_hash.encode()).hexdigest()
                    hash_list.append(new_hash)
                if find_quint(hash_list[pointer + forward], search_char):
                    key_count += 1
                    print(key_count)
                    if key_count == 64:
                        return pointer
                    break

        pointer += 1
    return 0


TEST_INPUT = "abc"
ACTUAL_INPUT = "zpqevtbw"
print(f"Part 1: {part1(ACTUAL_INPUT)}")
