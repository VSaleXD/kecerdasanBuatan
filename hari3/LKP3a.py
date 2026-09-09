import sys
import os

sys.path.append(os.path.abspath('../aima-python'))

from aima.search import Graph, GraphProblem, breadth_first_graph_search, depth_first_graph_search, uniform_cost_search

jabar_map = Graph(dict(
    Bekasi=dict(Bogor=10, Karawang=10),
    Bogor=dict(Bekasi=10, Sukabumi=15, Cianjur=8),
    Sukabumi=dict(Bogor=15, Cianjur=15),
    Karawang=dict(Bekasi=10, Subang=8, Purwakarta=8),
    Purwakarta=dict(Karawang=8, Subang=8, Cianjur=8),
    Subang=dict(Karawang=8, Purwakarta=8, Indramayu=10, Sumedang=10),
    Cianjur=dict(Bogor=8, Sukabumi=15, Bandung=8, WestBandung=8),
    WestBandung=dict(Cianjur=8, Bandung=5),
    Bandung=dict(WestBandung=5, Sumedang=10, Garut=8, Cianjur=8),
    Sumedang=dict(Subang=10, Bandung=10, Majalengka=5),
    Indramayu=dict(Subang=10, Cirebon=8),
    Majalengka=dict(Sumedang=5, Kuningan=10),
    Cirebon=dict(Indramayu=8, Kuningan=8),
    Kuningan=dict(Cirebon=8, Majalengka=10, Ciamis=8),
    Garut=dict(Bandung=8, Tasikmalaya=8),
    Tasikmalaya=dict(Garut=8, Ciamis=5, Pangandaran=8),
    Ciamis=dict(Kuningan=8, Tasikmalaya=5, Pangandaran=5),
    Pangandaran=dict(Tasikmalaya=8, Ciamis=5)
), directed=False)

problem = GraphProblem('Bogor', 'Pangandaran', jabar_map)

hasilBFS = breadth_first_graph_search(problem)
print("1.BFS Path:", hasilBFS.path(), "\nCost:", hasilBFS.path_cost)

hasilDFS = depth_first_graph_search(problem)
print("2.DFS Path:", hasilDFS.path(), "\nCost:", hasilDFS.path_cost)

hasilUCS = uniform_cost_search(problem)
print("3.UCS Path:", hasilUCS.path(), "\nCost:", hasilUCS.path_cost)