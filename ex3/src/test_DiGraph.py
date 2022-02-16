from unittest import TestCase
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class TestDiGraph(TestCase):

    def test_v_size(self):
        graph = GraphAlgo()
        file = '../data/A0.json'
        graph.load_from_json(file)
        self.assertEqual(graph.my_graph.v_size(), 11)

    def test_e_size(self):
        graph= GraphAlgo()
        file= '../data/A0.json'
        graph.load_from_json(file)
        self.assertEqual(graph.my_graph.e_size(), 22)

    def test_get_all_v(self):
        graph = DiGraph()
        point1 = (1, 1, 1)
        point2 = (2, 2, 2)
        point3 = (3, 3, 3)
        point4 = (4, 4, 4)
        graph.add_node(0, point1)
        graph.add_node(1, point2)
        graph.add_node(2, point3)
        graph.add_node(3, point4)
        g_ver = graph.get_all_v()
        self.assertEqual(0, g_ver.get(0).get_key())
        self.assertEqual(1, g_ver.get(1).get_key())
        self.assertEqual(2, g_ver.get(2).get_key())
        self.assertEqual(3, g_ver.get(3).get_key())

    def test_all_in_edges_of_node(self):
        graph = GraphAlgo()
        file = '../data/A0.json'
        graph.load_from_json(file)
        temp = graph.my_graph.all_in_edges_of_node(1)
        point0 = (35.18753053591606, 32.10378225882353, 0.0)
        point2 = (35.19341035835351, 32.10610841680672, 0.0)
        self.assertTrue(temp.__contains__(0)) #contains the node id 0
        self.assertTrue(temp.__contains__(2)) #contains the node id 2

    def test_all_out_edges_of_node(self):
        graph = GraphAlgo()
        file = '../data/A0.json'
        graph.load_from_json(file)
        temp = graph.my_graph.all_out_edges_of_node(1)
        point0 = (35.18753053591606, 32.10378225882353, 0.0)
        point2 = (35.19341035835351, 32.10610841680672, 0.0)
        self.assertTrue(temp.__contains__(0))
        self.assertTrue(temp.__contains__(2))

    def test_get_mc(self):
        graph = DiGraph()
        self.assertEqual(0, graph.get_mc())
        point1 = (35.20792948668281, 32.10470908739496, 0.0)
        graph.add_node(0, point1)
        self.assertEqual(1, graph.get_mc())
        point2 = (35.20746249717514, 32.10254648739496, 0.0)
        graph.add_node(1, point1)
        self.assertEqual(2, graph.get_mc())

    def test_add_edge(self):
        graph = DiGraph()
        point1 = (35.18753053591606, 32.10378225882353, 0.0)
        point2 = (35.18958953510896, 32.10785303529412, 0.0)
        graph.add_node(0, point1)
        graph.add_node(1, point2)
        self.assertTrue(graph.add_edge(0, 1, 1.4004465106761335))

    def test_add_node(self):
        graph = DiGraph()
        point1 = (1, 2, 3)
        point2 = (3, 4, 5)
        self.assertTrue(graph.add_node(0, point1))
        self.assertTrue(graph.add_node(1, point2))
        point3 = (1, 2, 3)
        self.assertFalse(graph.add_node(0, point3))

    def test_remove_node(self):
        graph = DiGraph()
        point1 = (35.18753053591606, 32.10378225882353, 0.0)
        point2 = (35.18958953510896, 32.10785303529412, 0.0)
        graph.add_node(0, point1)
        graph.add_node(1, point2)
        self.assertTrue(graph.remove_node(0))
        self.assertTrue(graph.remove_node(1))

    def test_remove_edge(self):
        graph = DiGraph()
        point1 = (35.18753053591606, 32.10378225882353, 0.0)
        point2 = (35.18958953510896, 32.10785303529412, 0.0)
        graph.add_node(0, point1)
        graph.add_node(1, point2)
        graph.add_edge(0, 1, 1.4004465106761335)
        self.assertTrue(graph.remove_edge(0, 1))



