from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    +------+-------+------------------------+
    | Item | Price | Special offers         |
    +------+-------+------------------------+
    | A    | 50    | 3A for 130, 5A for 200 |
    | B    | 30    | 2B for 45              |
    | C    | 20    |                        |
    | D    | 15    |                        |
    | E    | 40    | 2E get one B free      |
    +------+-------+------------------------+
    """
    counts = defaultdict(lambda: 0)

    for sku in skus:
        counts[sku] += 1

    for 


    total = 0
    for sku, count in counts.items():
        try:
            total += handle_item(sku, count)
        except ValueError:
            return -1

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

