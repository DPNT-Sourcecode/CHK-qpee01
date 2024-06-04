from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    +------+-------+----------------+
    | Item | Price | Special offers |
    +------+-------+----------------+
    | A    | 50    | 3A for 130     |
    | B    | 30    | 2B for 45      |
    | C    | 20    |                |
    | D    | 15    |                |
    +------+-------+----------------+
    """
    skus = skus.lower()

    counts = defaultdict(lambda: 0)

    valid_skus = "abcd"

    for sku in skus:
        if sku in valid_skus:
            counts[sku] += 1

    total = 0
    for sku, count in counts.items():
        total += handle_item(sku, count)

    return total



def handle_item(sku, count):
    if sku == "a":
        offer_n = count // 3
        remainder_n = count % 3
        return offer_n * 130 + 50 * remainder_n
    elif sku == "b":
        offer_n = count // 2
        remainder_n = count % 2
        return offer_n * 45 + 30 * remainder_n
    elif sku == "c":
        return count * 20
    elif sku == "d":
        return count * 15
    else:
        raise ValueError(f"Unexpected sku: {sku}")




