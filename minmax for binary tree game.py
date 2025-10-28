# Leaf nodes are terminal game scores
tree = { 'A':[ 'B','C' ],
         'B':[3,5],
         'C':[2,9] }

def minimax(node, isMax):
    if isinstance(node, int):
        return node
    left, right = tree[node]
    if isMax:
        return max(minimax(left, False),
                   minimax(right, False))
    else:
        return min(minimax(left, True),
                   minimax(right, True))

result = minimax('A', True)
print("Best Score for MAX:", result)
