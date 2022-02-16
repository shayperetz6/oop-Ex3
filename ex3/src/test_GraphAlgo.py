from unittest import TestCase
from DiGraph import *
from GraphAlgo import *
class TestGraphAlgo(TestCase):

    def test_get_graph(self):
        graph = DiGraph()
        point1 = (1, 1, 1)
        point2 = (2, 2, 2)
        point3 = (3, 3, 3)
        point4 = (4, 4, 4)
        graph.add_node(0, point1)
        graph.add_node(1, point2)
        graph.add_node(2, point3)
        graph.add_node(3, point4)
        graph.add_edge(0, 1, 2)
        graph.add_edge(2, 3, 2)
        ag = GraphAlgo(graph)
        g2 = ag.get_graph()
        self.assertEqual(g2.e_size(), graph.e_size())
        self.assertEqual(g2.v_size(), graph.v_size())
        ag_ver = ag.get_graph().get_all_v()
        g2_ver = g2.get_all_v()
        for i in ag_ver.keys():
            self.assertEqual(ag_ver.get(i).get_key(), g2_ver.get(i).get_key())

    def test_load_from_json(self):
        ag = GraphAlgo()
        file = '../data/A0.json'
        ag.load_from_json(file)
        self.assertEqual(ag.my_graph.v_size(), 11)
        self.assertEqual(ag.my_graph.e_size(), 22)

    def test_save_to_json(self):
        ag = GraphAlgo()
        file = '../data/A0.json'
        self.assertTrue(ag.load_from_json(file))
        self.assertTrue(ag.save_to_json("test.json"))
        self.assertTrue(ag.load_from_json("test.json"))

    def test_shortest_path(self):
        graph = DiGraph()
        graph.add_node(0, (1, 1, 1))
        graph.add_node(1, (2, 2, 2))
        graph.add_node(2, (3, 3, 3))
        graph.add_edge(0, 1, 2)
        graph.add_edge(0, 2, 4)
        graph.add_edge(1, 2, 1)
        ag = GraphAlgo(graph)
        self.assertEqual(ag.shortest_path(0, 2), (3, [0, 1, 2]))

    def test_tsp(self):
        graph = DiGraph()
        graph.add_node(0, (1, 1, 1))
        graph.add_node(1, (2, 2, 2))
        graph.add_node(2, (3, 3, 3))
        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 2, 3)
        graph.add_edge(2, 0, 10)
        ag = GraphAlgo(graph)
        lst = [0, 1, 2]
        self.assertEqual(ag.TSP(lst), ([0, 1, 2], 4))

    def test_center_point(self):
        ag = GraphAlgo()
        file1 = '../data/A0.json'
        file2 = '../data/A1.json'
        ag.load_from_json(file1)
        self.assertEqual(ag.centerPoint(), (7, 6.806805834715163))
        ag.load_from_json(file2)
        self.assertEqual(ag.centerPoint(), (8, 9.925289024973141))



