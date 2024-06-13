from sha256 import sha256

def merkle_root(transactions):
    if len(transactions) == 0:
        return None
    if len(transactions) == 1:
        return sha256(transactions[0].encode())

    new_level = []
    for i in range(0, len(transactions), 2):
        left = transactions[i]
        if i + 1 < len(transactions):
            right = transactions[i + 1]
        else:
            right = left
        new_level.append(sha256((left + right).encode()))

    return merkle_root(new_level)
