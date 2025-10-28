graph = {
 'A':['B','C'],
 'B':['A','C','D'],
 'C':['A','B','D'],
 'D':['B','C']
}

colors = ['Red','Green','Blue']
result = {}

def color_map(node):
    for color in colors:
        if all(result.get(n) != color for n in graph[node]):
            result[node] = color
            break

for node in graph:
    color_map(node)

print("Region Colors:", result)
