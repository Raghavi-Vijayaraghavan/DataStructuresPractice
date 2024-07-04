from collections import defaultdict
def fillDictionary(keys, values):
    graph = defaultdict(list)
    for k in keys:
        for i in v:
            graph[k].append(i)
    for k in graph:
        print(graph[k])


fillDictionary([1,2,3], [[2,3,4],[3,4,5],[4,5,6]])
        
