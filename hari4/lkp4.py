import os
import sys

sys.path.append(os.path.abspath('../aima-python'))

from aima.search import *

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

koordinat = dict(
    Bandung=(30, 10), Bekasi=(10, 50), Bogor=(20, 30),
    Ciamis=(50, 20), Cianjur=(23, 20), Cirebon=(45, 30), 
    Garut=(40, 5), Indramayu=(40, 30), Karawang=(20, 50),
    Kuningan=(45, 20), Majalengka=(40, 20), Pangandaran=(50, 5),
    Purwakarta=(30, 30), Subang=(20, 40), Sukabumi=(20, 20),
    Sumedang=(35, 25), Tasikmalaya=(45, 5), WestBandung=(25, 10)
)
def euclid(x, y):
    return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5

# for i in koordinat:
#     print("Heuristic from", i, "to Pangandaran:", euclid(koordinat[i], koordinat['Pangandaran']))

problem = GraphProblem('Bogor', 'Pangandaran', jabar_map)

heuristic = lambda n: euclid(koordinat[n.state], koordinat['Pangandaran'])

hasilGreedy = best_first_graph_search(
    problem,
    heuristic
)

print("Jalur:", hasilGreedy.solution(), "Cost:", hasilGreedy.path_cost)

hasilAStar = astar_search(
    problem,
    heuristic
)

print("Jalur:", hasilAStar.solution(), "Cost:", hasilAStar.path_cost)
