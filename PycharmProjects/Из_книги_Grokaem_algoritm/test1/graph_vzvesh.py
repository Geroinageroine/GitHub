graph={}

#print(graph)

graph["start"] = {}
graph["start"]["A"]=10

#print(graph)
#print(graph["start"].keys())
#print(graph["start"]["a"])
#print(graph["start"]["b"])
#print(graph.keys())

graph["A"]={}
graph["A"]["B"] = 20


graph["B"]={}
graph["B"]["C"]=1
graph["B"]["end"]=30

graph["C"]={}
graph["C"]["A"] = 1

graph["end"]={}
#print(graph) # Sozdali graph

infinity = float("inf")
#print(infinity)
costs={}
costs["A"]=10
costs["B"]=infinity
costs["C"]=infinity
costs["end"]=infinity
#print(costs)

parents = {}
parents["A"] = "start"
parents["B"] = None
parents["C"] = None
parents["end"] = None
#print(parents)

processed = []


def find_lowest_cost_node(costs):
    lowest_cost=float("inf")
    lowest_cost_node=None
    for node in costs:
        cost=costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost=cost
            lowest_cost_node = node
    return lowest_cost_node

node=find_lowest_cost_node(costs)
while node is not None:
    cost=costs[node]
    neighbors=graph[node]
    for n in neighbors.keys():
        new_cost=cost+neighbors[n]
        if costs[n] > new_cost:
            costs[n]=new_cost
            parents[n]=node
    processed.append(node)
    node=find_lowest_cost_node(costs)

print(costs)
print(parents)