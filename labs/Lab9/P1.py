import subprocess


# C:\Users\batuh\Desktop\Lab PCLP2\pythonProjects\labs\Lab9\knapsack.txt

subprocess.run("cls", shell=True)
file_path = input("Enter the file path: ")


def load_data():
    with open(file_path, "r") as file:
        data = file.readline().strip().split("|")
        n, V, p, v = (
            int(data[0]),
            int(data[1]),
            list(map(int, data[2].split(","))),
            list(map(int, data[3].split(","))),
        )
    return n, V, p, v


def knapsack(n, V, p, v):
    ratio_sorted_indices = sorted(range(n), key=lambda i: p[i] / v[i], reverse=True)
    x = [0] * n
    i = 0
    total_volume = total_price = 0
    while total_volume < V and i < n:
        if total_volume + v[ratio_sorted_indices[i]] <= V:
            x[ratio_sorted_indices[i]] = 1
            total_price += p[ratio_sorted_indices[i]]
            total_volume += v[ratio_sorted_indices[i]]
        else:
            x[ratio_sorted_indices[i]] = (V - total_volume) / v[ratio_sorted_indices[i]]
            total_volume = V
            total_price += p[ratio_sorted_indices[i]] * x[ratio_sorted_indices[i]]
        i += 1
    subprocess.run("cls", shell=True)
    print(
        f"Total price of items in the knapsack = {total_price}\nTotal volume occupied = {total_volume}"
    )
    print("\nItems included in the knapsack (price | volume):", end="\n\n")
    for i in range(n):
        if x[i] > 0:
            print(
                f"- Item {i+1}: {p[i]*x[i]:^7.2f}|{v[i]*x[i]:^8.2f}| ratio = {x[i]:.2f}"
                if x[i] != 1.00
                else f"- Item {i+1}: {p[i]*x[i]:^7.2f}|{v[i]*x[i]:^8.2f}"
            )
    print()


if __name__ == "__main__":
    n, V, p, v = load_data()
    knapsack(n, V, p, v)
