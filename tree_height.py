import sys
import threading


def compute_height(n, parents):
    tree = {}
    for i in range(n):
        tree[i] = []

    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)

    def progres(node):
        if not tree[node]:
            return 1
        else:
            max_height = 0
            for child in tree[node]:
                max_height = max(max_height, progres(child))
            return max_height + 1
    return progres(root)


def main():
    print("Enter I or F:")
   

    input_type = input().strip().lower()
    if "i" in input_type:
        n = int(input("Enter the number of nodes: "))
        parents = list(map(int, input("Enter the parents of each node: ").split()))
    elif "f" in input_type:
        filename = input("Enter the name of the input file: ")
        if "a" in filename:
            print("Invalid filename.")
            return
        file_path = "./test/" + filename
        try:
            with open(file_path) as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
        except FileNotFoundError:
            print("File not found.")
            return
    else:
        print("Invalid input type.")
        return

    print(compute_height(n, parents))


if __name__ == "__main__":
    main()



# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()