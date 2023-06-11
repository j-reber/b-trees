from matplotlib import pyplot as plt

from btree_alt import BTree
import random

if __name__ == '__main__':
    n = 5000000
    # rank = 3
    check = 10
    btree_3 = BTree(3)
    btree_10 = BTree(10)
    btree_100 = BTree(100)
    btree_1000 = BTree(1000)

    elements = [_ for _ in range(n)]
    random.shuffle(elements)
    heights_3 = []
    heights_10 = []
    heights_100 = []
    heights_1000 = []

    idx = []

    for i, e in enumerate(elements):
        print(i)
        btree_3.insert(e)
        btree_10.insert(e)
        btree_100.insert(e)
        btree_1000.insert(e)

        if i % check == 0:
            heights_3.append(btree_3.calculate_btree_height())
            heights_10.append(btree_10.calculate_btree_height())
            heights_100.append(btree_100.calculate_btree_height())
            heights_1000.append(btree_1000.calculate_btree_height())

            idx.append(i)

    plt.figure(figsize=(10, 6))
    plt.plot(idx, heights_3, label='Height of a tree with rank 3')
    plt.plot(idx, heights_10, label='Height of a tree with rank 10')
    plt.plot(idx, heights_100, label='Height of a tree with rank 100')
    plt.plot(idx, heights_1000, label='Height of a tree with rank 1000')

    plt.xlabel('Number of Elements (n) inserted')
    plt.ylabel('Total height')

    plt.title(f'Height of different b trees while inserting {n} elements')

    plt.legend()
    plt.savefig(f"plots/height_{n}_elements")
    plt.show()
