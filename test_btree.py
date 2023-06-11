import random
import time
import matplotlib.pyplot as plt
from btree_alt import BTree

if __name__ == '__main__':

    # n_values = [i for i in range(0, 31000, 1000)]
    n_values = [i for i in range(0, 110000, 10000)]
    num_experiments = 10
    rank = 3

    # append_times_list = []
    # delete_times_list = []
    # search_times_list = []
    append_times_tree = []
    delete_times_tree = []
    search_times_tree = []

    for n in n_values:
        # insert_avg_time_list = 0
        # delete_avg_time_list = 0
        # search_avg_time_list = 0
        insert_avg_time_tree = 0
        delete_avg_time_tree = 0
        search_avg_time_tree = 0

        for k in range(num_experiments):
            b_3 = BTree(rank)
            dynamic_array = []
            elements = [_ for _ in range(n)]
            random.seed(k)

            random.shuffle(elements)
            for i, e in enumerate(elements):
                print(i, k, "insert")
                # start = time.time()
                # dynamic_array.append(e)
                # end = time.time()
                # insert_avg_time_list += (end - start) / num_experiments
                start = time.time()
                b_3.insert(e)
                end = time.time()
                insert_avg_time_tree += (end - start) / num_experiments

            random.shuffle(elements)
            for i, e in enumerate(elements):
                print(i, k, "search")
                # start = time.time()
                # dynamic_array.index(e)
                # end = time.time()
                # search_avg_time_list += (end - start) / num_experiments

                start = time.time()
                b_3.find(e)
                end = time.time()
                search_avg_time_tree += (end - start) / num_experiments

            random.shuffle(elements)
            for i, e in enumerate(elements):
                print(i, k, "delete")
                # start = time.time()
                # dynamic_array.remove(e)
                # end = time.time()
                # delete_avg_time_list += (end - start) / num_experiments

                start = time.time()
                b_3.delete(e)
                end = time.time()
                delete_avg_time_tree += (end - start) / num_experiments

        # append_times_list.append(insert_avg_time_list)
        # delete_times_list.append(delete_avg_time_list)
        # search_times_list.append(search_avg_time_list)
        append_times_tree.append(insert_avg_time_tree)
        delete_times_tree.append(delete_avg_time_tree)
        search_times_tree.append(search_avg_time_tree)

    # Plotting
    plt.figure(figsize=(10, 6))
    # plt.plot(n_values, append_times_list, label='Insert in list')
    # plt.plot(n_values, delete_times_list, label='Delete key in list')
    # plt.plot(n_values, search_times_list, label='Search in list')

    plt.plot(n_values, append_times_tree, label='Insert in tree')
    plt.plot(n_values, delete_times_tree, label='Delete key in tree')
    plt.plot(n_values, search_times_tree, label='Search in tree')

    plt.xlabel('Number of Elements (n)')
    plt.ylabel('Time (seconds)')
    plt.title(f'B-Tree t={rank} with Insert, Delete, and Search Times (with Random Elements)')
    # plt.title(f'List with Insert, Delete, and Search Times (with Random Elements)')
    # plt.title(f'List vs B-Tree t={rank} with Insert, Delete, and Search Times (with Random Elements)')

    plt.legend()
    plt.savefig(f"plots/tree_rank_{rank}_{n_values[-1]}_samples_{num_experiments}_avg.png")
    # plt.show()
