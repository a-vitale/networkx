"""Shortest paths and path lengths using the Greedy algorithm.
"""
from heapq import heappush, heappop
from itertools import count

import networkx as nx
from networkx.algorithms.shortest_paths.weighted import _weight_function

def greedy_path(G, source, target, heuristic = None, weight = "weight"):

    #if source or target is not in G -> error msg
    if source not in G or target not in G:
        msg = f"Either source {source} or target {target} is not in G"
        raise nx.NodeNotFound(msg)

    #if heuristic is none -> define the default heuristic function: h = 0
    if heuristic is None:
        def heuristic(u, v):
            return 0

    #assegno a push la funzione heappush e a pop la funzione heappop. 
    #A wieght invece assegno la funzione _weight_function(G, weight)
    #passando come parametro G e weight (input della funzione greedy_search)
    push = heappush
    pop = heappop
    getWeight = _weight_function(G, weight)

    #variabile di gestione dell'euristica nell'ordinamento (in caso di parità)
    c = count()

    #la fringe mantiene: priorità, nodo corrente (nel caso base è la radice), varibaile di gestione e il parent 
    fringe = [(0, next(c), source, None)]

    #struttura dati che memorizza i parent dei nodi visitati 
    explored = {}

    #struttura che mantiene i pesi dei cammini parziali 
    weights = {}

    while queue:
        _, __, curNode, parent = pop(fringe)
        
        #caso base: target raggiunto. Costruzione del path tramite i parent
        if curNode == target:
            path = [curNode]
            node = parent
            while node is not None:
                path.append(node)
                node = explored[node]
            path.reverse()
            return path
        
        curWeight = weights[parent] + getWeight(parent, curNode, weight)
        if curNode in explored:
            if explored[curNode] is None:
                continue
            if curWeight > weights[curNode]:
                continue 
        
        explored[curNode] = parent
        weights[curNode] = curWeight

        for neighbor, _ in G[curNode].items():
            if neighbor not in explored:
                weights[neighbor] = weights[curNode] + getWeight(curnNode, neighbor, weight)
            heuristicValue = heuristic(neighbor, target)
            push(fringe, (heuristicValue, next(c), neighbor, curNode))