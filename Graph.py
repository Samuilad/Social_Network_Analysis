from pyvis.network import Network
from Edge import Edge
from Node import Node


class Graph:
    nodes = []
    edges = []
    net = Network(directed=True)

    def __init__(self, nodes_list, edges_list):
        self.nodes = nodes_list
        self.edges = edges_list

    def show_graph(self):

        for edge in self.edges:
            for node in self.nodes:
                if (node.data == edge.start):
                    node.out_going_edges_count += 1

        # adds each node to graph
        for node in self.nodes:
            self.net.add_node(node.data, value = 5  * (1 + (node.out_going_edges_count / len(self.edges))))

        # adds each edge to graph
        for edge in self.edges:
            self.net.add_edge(edge.start, edge.end, title=edge.title, color=edge.color)

        # displays physics menu which allows you to alter the position of nodes and other similar things
        self.net.show_buttons(filter_=['physics'])

        # displays the graph
        self.net.show('basic.html')
