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

    
    for sku, count in counts.items():




def handle_item(sku, count):
    if sku == "A":
        offer_n =


