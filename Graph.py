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
                if node.data == edge.start:
                    node.out_going_edges_count += 1

        # adds each node to graph
        for node in self.nodes:
            if 'BH' in node.data:
                self.net.add_node(node.data, value=14 * (1 + (node.out_going_edges_count / len(self.edges))), color = 'red', title = str(node.out_going_edges_count))
            elif node.data == "SRT":
                self.net.add_node(node.data, value=14 * (1 + (node.out_going_edges_count / len(self.edges))), color='Black', title = str(node.out_going_edges_count))
            else:
                self.net.add_node(node.data, value=14 * (1 + (node.out_going_edges_count / len(self.edges))), color='Orange', title = str(node.out_going_edges_count))

        # adds each edge to graph
        for edge in self.edges:
            self.net.add_edge(edge.start, edge.end, title=edge.title, color=edge.color)

        # displays physics menu which allows you to alter the position of nodes and other similar things
        self.net.show_buttons(filter_=['nodes'])

        # displays the graph
        self.net.show('basic.html')
