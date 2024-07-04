from collections import defaultdict
graph = defaultdict(list)
def createGraph(keys, values):
    for k in range(len(keys)):
        graph[keys[k]].append(values[k])
    print(graph)

def coursePossibility(graph):
    queue = []
    allKeys = list(graph.keys())
    queue.append(allKeys)
    for i in range(len(queue)):
        prevKey = queue[i]
        for _ in range(len(queue)):
           key = queue.pop(0)
           if key in graph:
               queue.append(graph[key])
               if graph[key] == prevKey:
                   return false
                else:
                    return true
            


createGraph([1,2],[[1,2],[2,3]])



            




    
    
