import sys
import threading


def compute_height(n, parents):
    
    root = None
    tree = {}
    for i in range(n):
        tree[i] = []

    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)

    def progress(Node):
        
        height = 1
        if not tree[Node]:
            return height
        else:
            for child in tree[Node]:
                height = max(height, progress(child))
            
            return height + 1
    return progress(root)


def main():
    # take input
    input_type = input("Enter I for manual input or F for file input: ").strip().lower()
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
   
    sys.setrecursionlimit(10**7)
    threading.stack_size(2**27)
    threading.Thread(target=main).start()