
def find_min_node(weights, checked):
        min_node = None
        min_weight = float('inf')
        for name, weight in weights.items():
            if weight < min_weight and name not in checked:
                min_weight = weight
                min_node = name
        return min_node

def min_path(graph, start, end):
    checked = set()
    parents = {}
    weights = {}

    for name, weight in graph[start].items():
        parents[name] = start
        weights[name] = weight

    min_node = find_min_node(weights, checked)

    while min_node is not None:
        for name, weight in graph[min_node].items():
            new_weight = weights[min_node] + weight
            if name not in weights or weights[name] > new_weight:
                weights[name] = new_weight
                parents[name] = min_node
        checked.add(min_node)
        min_node = find_min_node(weights, checked)

    answer = [end]
    parent = parents[end]
    while parent is not None:
        answer.append(parent)
        if parent == start:
            break
        parent = parents[parent]
    answer.reverse()

    return weights


def main():
    graph = {
    "1": {"2": 6, "4": 4},
    "2": {"3": 3, "1": 6},
    "3": {"5": 4, "8": 5, "4": 5, "2": 3},
    "4": {"8": 3, "6": 2, "3": 5, "1": 4},
    "5": {"7": 4, "3": 4},
    "6": {"8": 5, "4": 2},
    "7": {"8": 3, "10": 2, "9": 2, "5": 4},
    "8": {"9": 7, "7": 3, "4": 3, "6": 5},
    "9": {"10": 1, "7": 2, "8": 7},
    "10": {"7": 2, "9": 1}
    }
    while True:  
        try:
            start = input("Введите начальную точку: ")
            end = input("Введите конечную точку: ")
            answer = min_path(graph, start, end)
            break
        except:
            print("Что-то не так, попробуйте еще раз!")

    return f"{start} --> {end} Path: {answer[end]}"



if __name__ == '__main__':
    print(main())
