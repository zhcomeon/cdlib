import unittest
from nclib import community
from nclib import readwrite
import networkx as nx
import os


class IOTests(unittest.TestCase):

    def test_read_write(self):
        g = nx.karate_club_graph()
        communities = community.louvain(g)

        readwrite.write_community_csv(communities, "coms.csv")
        communities_r = readwrite.read_community_csv("coms.csv", nodetype=int)
        self.assertListEqual(communities, communities_r)
        os.remove("coms.csv")


if __name__ == '__main__':
    unittest.main()