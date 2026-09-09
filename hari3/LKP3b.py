import os
import sys

sys.path.append(os.path.abspath('../aima-python'))

from aima.search import Graph, GraphProblem, breadth_first_graph_search, depth_first_graph_search, uniform_cost_search

jalurDistribusi = Graph(dict(
    Semarang=dict(Kendal=20, Ungaran=15),
    Kendal=dict(Semarang=20, Batang=25),
    Batang=dict(Kendal=25, Pekalongan=30),
    Ungaran=dict(Semarang=15, Ambarawa=10, Salatiga=20),
    Ambarawa=dict(Ungaran=10, Magelang=25),
    Salatiga=dict(Ungaran=20, Boyolali=18),
    Boyolali=dict(Salatiga=18, Solo=22),
    Solo=dict(Boyolali=22, Sragen=25, DesaA=30),
    Magelang=dict(Ambarawa=25, DesaA=40),
    Sragen=dict(Solo=25, DesaA=15),
    DesaA=dict(Magelang=40, Sragen=15, Solo=30)
), directed=False)

problem = GraphProblem('Semarang', 'DesaA', jalurDistribusi)

print("Kasus 1 - Jalur Distribusi Pupuk di Jawa Tengah")

print("1. BFS Path:", breadth_first_graph_search(problem).path(), "\nCost:", breadth_first_graph_search(problem).path_cost, "KM")
print("2. DFS Path:", depth_first_graph_search(problem).path(), "\nCost:", depth_first_graph_search(problem).path_cost, "KM")
print("3. UCS Path:", uniform_cost_search(problem).path(), "\nCost:", uniform_cost_search(problem).path_cost, "KM")

RuteKapal = Graph(dict(
    Makassar=dict(ParePare=5, Jeneponto=4),
    ParePare=dict(Makassar=5, Palopo=7),
    Palopo=dict(ParePare=7, Kolaka=6),
    Jeneponto=dict(Makassar=4, Bira=3),
    Bira=dict(Jeneponto=3, Kendari=8),
    Kolaka=dict(Palopo=6, Kendari=5),
    Kendari=dict(Kolaka=5, Bira=8, BauBau=6),
    BauBau=dict(Kendari=6, PasarB=4),
    PasarB=dict(BauBau=4)
), directed=False)

problem2 = GraphProblem('Makassar', 'PasarB', RuteKapal)

print("\n","Kasus 2 - Rute Kapal di Sulawesi Selatan")
print("1. BFS Path:", breadth_first_graph_search(problem2).path(), "\nCost:", breadth_first_graph_search(problem2).path_cost, "Jam")
print("2. DFS Path:", depth_first_graph_search(problem2).path(), "\nCost:", depth_first_graph_search(problem2).path_cost, "Jam")
print("3. UCS Path:", uniform_cost_search(problem2).path(), "\nCost:", uniform_cost_search(problem2).path_cost, "Jam")