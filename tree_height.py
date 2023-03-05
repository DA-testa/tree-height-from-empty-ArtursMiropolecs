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
    # check if the input is from a file or from the keyboard
    input_type = input("Input from keyboard or file? (K/F): ")
    if input_type.lower() == "k":
        input_str = input("Enter the number of nodes and the parents of each node: ").strip()
        input_lines = input_str.split("\n")
    elif input_type.lower() == "f":
        file_name = input("Enter the file name (without the letter 'a'): ")
        while "a" in file_name:
            file_name = input("Invalid file name. Enter a valid file name (without the letter 'a'): ")
        try:
            with open('./test/'+file_name) as file:
                input_lines = file.readlines()
        except FileNotFoundError:
            print("File not found.")
            return
    else:
        print("Invalid input.")
        return

    n = int(input_lines[0])
    parents = list(map(int, input_lines[1].split()))
    height = compute_height(n, parents)
    print(height)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()