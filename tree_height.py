import sys
import threading


def compute_height(n, parents):
    # create an array to store the height of each node
    heights = [0] * n

    # find the root of the tree
    root = None
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            # update the height of the parent node
            heights[parents[i]] = max(heights[parents[i]], heights[i] + 1)

    # return the height of the root node
    return heights[root] + 1


def main():
    input_str = input().strip()
    if not input_str.isdigit():
        print("Invalid input: expected an integer")
        return
    n = int(input_str)
    parents = list(map(int, input().split()))
    height = compute_height(n, parents)
    print(height)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()