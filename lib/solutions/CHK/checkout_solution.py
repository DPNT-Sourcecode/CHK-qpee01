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
    counts = defaultdict(lambda: 0)

    for sku in skus:
        counts[sku] += 1

    total = 0
    for sku, count in counts.items():
        total += handle_item(sku, count)

    return total



def handle_item(sku, count):
    if sku == "A":
        offer_n = count // 3
        remainder_n = count % 3
        return offer_n * 130 + 50 * remainder_n
    elif sku == "B":
        offer_n = count // 2
        remainder_n = count % 2
        return offer_n * 45 + 30 * remainder_n
    elif sku == "C":
        return count * 20
    elif sku == "D":
        return count * 15
    else:
        raise ValueError(f"Unexpected sku: {sku}")


