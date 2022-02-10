from pyvis.network import Network
import numpy as np
import csv
import json



class Node:
    data = ''
    out_going_edges_count = 0

    def __init__(self, data):
        self.data = data

class Edge:
    start = ''
    end = ''
    title = ''
    color = ''

    def __init__(self, start, end, title, color='black'):
        self.start = start
        self.end = end
        self.title = title.upper()
        self.color = color

class Parser:
    edge_header = []
    node_header = []
    edge_first = True
    node_first = True
    def __init__(self, edge_file_name, node_file_name):
        # Reads data csv edge data
        edge_file = open(edge_file_name)
        edge_csv_reader = csv.reader(edge_file)
        self.edge_header = edge_csv_reader
        for row in self.edge_header:
            if self.edge_first:
                self.edge_first = False
                continue
            edges.append(Edge(row[1],row[2],row[0]))
        # Reads data csv node data
        node_file = open(node_file_name)
        node_csv_reader = csv.reader(node_file)
        self.node_header = node_csv_reader
        for row in self.node_header:
            if self.node_first:
                self.node_first = False
                continue
            nodes.append(Node(row[0]))

class Graph:
    nodes = []
    edges = []
    net = Network(directed=True, height=1500, width=1500)
    type = ''
    adjacencyMatrix = 0
    indexToNameDict = {}
    activity = ''

    def __init__(self, nodes_list, edges_list, graph_type, activity = None):
        self.nodes = nodes_list
        self.edges = edges_list
        self.type = graph_type.upper()
        self.activity = activity.upper()
        print(self.type)
        if self.type == 'WEIGHTED':
            self.adjacencyMatrix = np.zeros((len(nodes), len(nodes)))
            self.indexToNameDict = {}
            self.net = Network(directed=False, height=1500, width=1500)

        for edge in self.edges:
            for node in self.nodes:
                if node.data == edge.start:
                    node.out_going_edges_count += 1
        print(len(self.edges))
    def add_nodes(self):
        for node in self.nodes:
            if 'BH' in node.data:
                if 'MENTOR' in node.data:
                    self.net.add_node(node.data, value=14 * (1 + (node.out_going_edges_count / len(self.edges))), color = '#ff7f0e', physics=True ,title = str(node.out_going_edges_count), shape='diamond')
                else:
                    self.net.add_node(node.data, value=14 * (1 + (node.out_going_edges_count / len(self.edges))), color='#ffbb78', physics=True ,title=str(node.out_going_edges_count))

            elif 'HAR' in node.data:
                if 'MENTOR' in node.data:
                    self.net.add_node(node.data, value=14 * (1 + (node.out_going_edges_count / len(self.edges))), color = '#d62728', physics=True ,title = str(node.out_going_edges_count), shape='diamond')
                elif 'SRT' in node.data:
                    self.net.add_node(node.data, value=14 * (1 + (node.out_going_edges_count / len(self.edges))),
                                  color='#ff9896', physics=True, borderWidth='1', title=str(node.out_going_edges_count),
                                  shape='diamond')

            elif 'UIUC' in node.data:
                if  'MENTOR' in node.data:
                    self.net.add_node(node.data, value = 14 * (1 + (node.out_going_edges_count / len( self.edges))), color = '#1f77b4', borderWidth = '1', physics=True ,title = str(node.out_going_edges_count), shape='diamond')
                elif "YR 2" in node.data:
                    self.net.add_node(node.data, value=14 * (1 + (node.out_going_edges_count / len(self.edges))),color='#5e96e0', physics=True ,title=str(node.out_going_edges_count))
                else:
                    self.net.add_node(node.data, value=14 * (1 + (node.out_going_edges_count / len(self.edges))),color='#aec7e8', physics=True, title=str(node.out_going_edges_count))

    def edge_colors(self, edge):
        physics_bool = True
        if self.activity == '' or self.activity == 'ALL':
            physics_bool = False

        if "UIUC" in edge.start:
            if "MENTOR" in edge.start:
                self.net.add_edge(edge.start, edge.end, title=edge.title, color='#1f77b4', physics=physics_bool, smooth=True,
                                  smoothtype='dynamic')
            elif "YR 2" in edge.start:
                self.net.add_edge(edge.start, edge.end, title=edge.title, color='#5e96e0', physics=physics_bool, smooth=True,
                                  smoothtype='dynamic')
            elif "YR 1" in edge.start:
                self.net.add_edge(edge.start, edge.end, title=edge.title, color='#aec7e8', physics=physics_bool, smooth=True,
                                  smoothtype='dynamic')
        if 'HAR' in edge.start:
            if 'MENTOR' in edge.start:
                self.net.add_edge(edge.start, edge.end, title=edge.title, color='#d62728', physics=physics_bool,
                                  smooth=True, smoothtype='dynamic')
            elif 'SRT' in edge.start:
                self.net.add_edge(edge.start, edge.end, title=edge.title, color='#ff9896', physics=physics_bool,
                                  smooth=True, smoothtype='dynamic')

        if 'BH' in edge.start:
            if 'MENTOR' in edge.start:
                self.net.add_edge(edge.start, edge.end, title=edge.title, color='#ff7f0e', physics=physics_bool,
                                  smooth=True, smoothtype='dynamic')
            elif 'YR 1' in edge.start:
                self.net.add_edge(edge.start, edge.end, title=edge.title, color='#ffbb78', physics=physics_bool,
                                  smooth=True, smoothtype='dynamic')

    def add_edges(self):
        if self.type == 'WEIGHTED':
            for i in range(len(nodes)):
                self.indexToNameDict[nodes[i].data] = i

            for edge in self.edges:
                self.adjacencyMatrix[self.indexToNameDict[edge.start]][self.indexToNameDict[edge.end]] += 1

            for edge in self.edges:
                if edge.title == self.activity or not self.activity:
                    self.net.add_edge(edge.start, edge.end, title=edge.title, physics = False, color='gray',smooth=True, smoothtype='dynamic',
                                    width=1 + 1.7 ** self.adjacencyMatrix[self.indexToNameDict[edge.start]][self.indexToNameDict[edge.end]])

        elif self.type == 'NORMAL':
            if self.activity == '' or self.activity == 'ALL':
                for edge in self.edges:
                    self.edge_colors(edge)
            else:
                for edge in self.edges:
                    if edge.title == self.activity or not self.activity:
                        self.edge_colors(edge)


    #Dispays the graph
    def show_graph(self):

        self.add_nodes()

        self.add_edges()

        #shows customization menu
        self.net.show_buttons(filter_=['physics', 'edges', 'nodes'])

        #set Physics Model
        self.net.repulsion(node_distance=160, central_gravity=0.01, spring_length=200, spring_strength=0.0025, damping=0.09)

        #make edges rounded and dynamically placed
        self.net.set_edge_smooth('continuous')

        # displays the graph
        self.net.show('basic.html')

val = ''
edges = []
nodes = []
parser = Parser('Social_Network_Analysis/Social_Network_Edges.csv','Social_Network_Analysis/Social_Network_Nodes.csv')


while val.upper() != 'END':

    print("please type weighted or normal")
    graph_type = input()
    print("Please type desired activity or leave press enter for all activities")
    activity = input()

    graph = Graph(nodes, edges, graph_type, activity)
    graph.show_graph()
    graph.net.edges.clear()
    print("press 'enter' to select more graphs or type 'End' to finish")
    val = input()