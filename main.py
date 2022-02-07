from pyvis.network import Network
import numpy as np

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

    def __init__(self, start, end, title, color):
        self.start = start
        self.end = end
        self.title = title.upper()
        self.color = color

# people/resources involved
nodes = [Node('SRT MNT'), Node('UIUC STUDENT 1 YR 2'), Node('UIUC STUDENT 2'), Node('UIUC STUDENT 3'), Node('UIUC STUDENT 4'),
         Node('UIUC STUDENT 5'), Node('UIUC STUDENT 6'), Node('UIUC STUDENT 7'), Node('UIUC STUDENT 8'),
         Node('UIUC STUDENT 10'), Node('UIUC STUDENT 11'), Node('UIUC STUDENT 9'), Node('UIUC STUDENT 12'),
         Node('UIUC STUDENT 13 YR 2'), Node('UIUC STUDENT 14'), Node('UIUC MENTOR 1'), Node('BH STUDENT 1'),
         Node('BH STUDENT 2'), Node('UIUC MENTOR 2'), Node('BH MENTOR 1'), Node('HAR MENTOR 1'), Node('HAR MENTOR 2'), Node('HAR MENTOR 3')]

# Displays the connection between teacher and student
edges1 = [
    # McKibbens
    Edge('SRT MNT', 'UIUC STUDENT 2', 'McKibbens Muscle', 'blue'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 1 YR 2', 'McKibbens Muscle', 'blue'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 3', 'McKibbens Muscle', 'blue'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 4', 'McKibbens Muscle', 'blue'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 5', 'McKibbens Muscle', 'blue'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 6', 'McKibbens Muscle', 'blue'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 7', 'McKibbens Muscle', 'blue'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 8', 'McKibbens Muscle', 'blue'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 10', 'McKibbens Muscle', 'blue'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 11', 'McKibbens Muscle', 'blue'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 9', 'McKibbens Muscle', 'blue'),
    Edge('UIUC STUDENT 2', 'UIUC STUDENT 12', 'McKibbens Muscle', 'blue'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 13 YR 2', 'McKibbens Muscle', 'blue'),
    Edge('UIUC STUDENT 9', 'UIUC STUDENT 14', 'McKibbens Muscle', 'blue'),
    Edge('BH MENTOR 1', 'BH STUDENT 1', 'McKibbens Muscle', 'blue'),
    Edge('BH MENTOR 1', 'BH STUDENT 2', 'McKibbens Muscle', 'blue'),

    # Heat Sealable Fabric Brace or Folding Box
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 1 YR 2', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('UIUC STUDENT 14', 'UIUC STUDENT 3', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 4', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('UIUC STUDENT 12', 'UIUC STUDENT 5', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('UIUC STUDENT 11', 'UIUC STUDENT 6', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('SRT MNT', 'UIUC STUDENT 6', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('UIUC STUDENT 12', 'UIUC STUDENT 8', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('UIUC STUDENT 12', 'UIUC STUDENT 11', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('UIUC STUDENT 14', 'UIUC STUDENT 9', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 12', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 13 YR 2', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 14', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('BH MENTOR 1', 'BH STUDENT 1', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('BH MENTOR 1', 'BH STUDENT 2', 'Heat Sealable Fabric Brace or Folding Box', 'black'),

    # SDM Finger
    Edge('UIUC STUDENT 13 YR 2', 'UIUC STUDENT 1 YR 2', 'SDM Finger', 'green'),
    Edge('UIUC STUDENT 1 YR 2', 'UIUC STUDENT 2', 'SDM Finger', 'green'),
    Edge('UIUC STUDENT 1 YR 2', 'UIUC STUDENT 3', 'SDM Finger', 'green'),
    Edge('UIUC STUDENT 1 YR 2', 'UIUC STUDENT 4', 'SDM Finger', 'green'),
    Edge('UIUC STUDENT 1 YR 2', 'UIUC STUDENT 5', 'SDM Finger', 'green'),
    Edge('UIUC STUDENT 13 YR 2', 'UIUC STUDENT 5', 'SDM Finger', 'green'),
    Edge('UIUC STUDENT 1 YR 2', 'UIUC STUDENT 6', 'SDM Finger', 'green'),
    Edge('UIUC STUDENT 13 YR 2', 'UIUC STUDENT 6', 'SDM Finger', 'green'),
    Edge('UIUC STUDENT 1 YR 2', 'UIUC STUDENT 7', 'SDM Finger', 'green'),
    Edge('UIUC STUDENT 13 YR 2', 'UIUC STUDENT 7', 'SDM Finger', 'green'),
    Edge('UIUC STUDENT 1 YR 2', 'UIUC STUDENT 8', 'SDM Finger', 'green'),
    Edge('UIUC STUDENT 13 YR 2', 'UIUC STUDENT 8', 'SDM Finger', 'green'),
    Edge('UIUC STUDENT 1 YR 2', 'UIUC STUDENT 10', 'SDM Finger', 'green'),
    Edge('UIUC STUDENT 13 YR 2', 'UIUC STUDENT 10', 'SDM Finger', 'green'),
    Edge('UIUC STUDENT 1 YR 2', 'UIUC STUDENT 11', 'SDM Finger', 'green'),
    Edge('UIUC STUDENT 13 YR 2', 'UIUC STUDENT 11', 'SDM Finger', 'green'),
    Edge('UIUC STUDENT 1 YR 2', 'UIUC STUDENT 9', 'SDM Finger', 'green'),
    Edge('UIUC STUDENT 13 YR 2', 'UIUC STUDENT 9', 'SDM Finger', 'green'),
    Edge('UIUC STUDENT 1 YR 2', 'UIUC STUDENT 12', 'SDM Finger', 'green'),
    Edge('UIUC STUDENT 13 YR 2', 'UIUC STUDENT 12', 'SDM Finger', 'green'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 13 YR 2', 'SDM Finger', 'green'),
    Edge('UIUC STUDENT 1 YR 2', 'UIUC STUDENT 14', 'SDM Finger', 'green'),
    Edge('UIUC STUDENT 13 YR 2', 'UIUC STUDENT 14', 'SDM Finger', 'green'),
    Edge('UIUC STUDENT 2', 'BH STUDENT 1', 'SDM Finger', 'green'),
    Edge('BH STUDENT 2', 'BH STUDENT 1', 'SDM Finger', 'green'),
    Edge('UIUC STUDENT 2', 'BH STUDENT 2', 'SDM Finger', 'green'),
    Edge('SRT MNT', 'BH STUDENT 2', 'SDM Finger', 'green'),

    # Motorized SDM Finger
    Edge('UIUC STUDENT 1 YR 2', 'UIUC STUDENT 1 YR 2', 'Motorized SDM Finger', 'red'),
    Edge('UIUC STUDENT 1 YR 2', 'UIUC STUDENT 2', 'Motorized SDM Finger', 'red'),
    Edge('UIUC STUDENT 13 YR 2', 'UIUC STUDENT 2', 'Motorized SDM Finger', 'red'),
    Edge('UIUC STUDENT 13 YR 2', 'UIUC STUDENT 6', 'Motorized SDM Finger', 'red'),
    Edge('UIUC STUDENT 1 YR 2', 'UIUC STUDENT 6', 'Motorized SDM Finger', 'red'),
    Edge('UIUC STUDENT 13 YR 2', 'UIUC STUDENT 13 YR 2', 'Motorized SDM Finger', 'red'),
    Edge('BH MENTOR 1', 'BH STUDENT 1', 'Motorized SDM Finger', 'red'),
    Edge('BH MENTOR 1', 'BH STUDENT 2', 'Motorized SDM Finger', 'red'),

    # SIA Actuator
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 1 YR 2', 'SIA Actuator', 'purple'),
    Edge('UIUC STUDENT 1 YR 2', 'UIUC STUDENT 2', 'SIA Actuator', 'purple'),
    Edge('UIUC STUDENT 8', 'UIUC STUDENT 4', 'SIA Actuator', 'purple'),
    Edge('UIUC STUDENT 1 YR 2', 'UIUC STUDENT 5', 'SIA Actuator', 'purple'),
    Edge('UIUC STUDENT 13 YR 2', 'UIUC STUDENT 5', 'SIA Actuator', 'purple'),
    Edge('UIUC STUDENT 1 YR 2', 'UIUC STUDENT 6', 'SIA Actuator', 'purple'),
    Edge('UIUC STUDENT 13 YR 2', 'UIUC STUDENT 6', 'SIA Actuator', 'purple'),
    Edge('UIUC STUDENT 13 YR 2', 'UIUC STUDENT 8', 'SIA Actuator', 'purple'),
    Edge('UIUC STUDENT 1 YR 2', 'UIUC STUDENT 8', 'SIA Actuator', 'purple'),
    Edge('UIUC STUDENT 13 YR 2', 'UIUC STUDENT 11', 'SIA Actuator', 'purple'),
    Edge('UIUC STUDENT 1 YR 2', 'UIUC STUDENT 11', 'SIA Actuator', 'purple'),
    Edge('UIUC STUDENT 13 YR 2', 'UIUC STUDENT 9', 'SIA Actuator', 'purple'),
    Edge('UIUC STUDENT 1 YR 2', 'UIUC STUDENT 9', 'SIA Actuator', 'purple'),
    Edge('UIUC STUDENT 1 YR 2', 'UIUC STUDENT 12', 'SIA Actuator', 'purple'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 13 YR 2', 'SIA Actuator', 'purple'),
    Edge('UIUC STUDENT 13 YR 2', 'UIUC STUDENT 14', 'SIA Actuator', 'purple'),
    Edge('UIUC STUDENT 1 YR 2', 'UIUC STUDENT 14', 'SIA Actuator', 'purple'),
    Edge('BH MENTOR 1', 'BH STUDENT 1', 'SIA Actuator', 'purple'),
    Edge('BH MENTOR 1', 'BH STUDENT 2', 'SIA Actuator', 'purple'),

    # Capacitance Sensor
    Edge('UIUC STUDENT 2', 'UIUC STUDENT 1 YR 2', 'Capacitance Sensor', 'brown'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 2', 'Capacitance Sensor', 'brown'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 5', 'Capacitance Sensor', 'brown'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 6', 'Capacitance Sensor', 'brown'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 8', 'Capacitance Sensor', 'brown'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 11', 'Capacitance Sensor', 'brown'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 9', 'Capacitance Sensor', 'brown'),
    Edge('UIUC STUDENT 2', 'UIUC STUDENT 12', 'Capacitance Sensor', 'brown'),
    Edge('UIUC STUDENT 9', 'UIUC STUDENT 14', 'Capacitance Sensor', 'brown'),

    # Flex Sensor
    Edge('UIUC STUDENT 8', 'UIUC STUDENT 2', 'Flex Sensor', 'Orange'),
    Edge('UIUC STUDENT 4', 'UIUC STUDENT 3', 'Flex Sensor', 'Orange'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 4', 'Flex Sensor', 'Orange'),
    Edge('UIUC STUDENT 8', 'UIUC STUDENT 5', 'Flex Sensor', 'Orange'),
    Edge('UIUC STUDENT 11', 'UIUC STUDENT 6', 'Flex Sensor', 'Orange'),
    Edge('SRT MNT', 'UIUC STUDENT 6', 'Flex Sensor', 'Orange'),
    Edge('SRT MNT', 'UIUC STUDENT 7', 'Flex Sensor', 'Orange'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 8', 'Flex Sensor', 'Orange'),
    Edge('UIUC STUDENT 9', 'UIUC STUDENT 8', 'Flex Sensor', 'Orange'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 10', 'Flex Sensor', 'Orange'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 11', 'Flex Sensor', 'Orange'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 9', 'Flex Sensor', 'Orange'),
    Edge('SRT MNT', 'UIUC STUDENT 12', 'Flex Sensor', 'Orange'),
    Edge('SRT MNT', 'UIUC STUDENT 14', 'Flex Sensor', 'Orange'),
    Edge('BH MENTOR 1', 'BH STUDENT 1', 'Flex Sensor', 'Orange'),
    Edge('BH MENTOR 1', 'BH STUDENT 2', 'Flex Sensor', 'Orange'),

    # Textile Bending Actuator
    Edge('UIUC STUDENT 5', 'UIUC STUDENT 2', 'Textile Bending Actuator', '#F01EAA'),
    Edge('UIUC STUDENT 6', 'UIUC STUDENT 4', 'Textile Bending Actuator', '#F01EAA'),
    Edge('UIUC STUDENT 8', 'UIUC STUDENT 4', 'Textile Bending Actuator', '#F01EAA'),
    Edge('SRT MNT', 'UIUC STUDENT 4', 'Textile Bending Actuator', '#F01EAA'),
    Edge('UIUC STUDENT 6', 'UIUC STUDENT 5', 'Textile Bending Actuator', '#F01EAA'),
    Edge('UIUC STUDENT 8', 'UIUC STUDENT 5', 'Textile Bending Actuator', '#F01EAA'),
    Edge('SRT MNT', 'UIUC STUDENT 5', 'Textile Bending Actuator', '#F01EAA'),
    Edge('SRT MNT', 'UIUC STUDENT 6', 'Textile Bending Actuator', '#F01EAA'),
    Edge('SRT MNT', 'UIUC STUDENT 8', 'Textile Bending Actuator', '#F01EAA'),
    Edge('UIUC STUDENT 6', 'UIUC STUDENT 8', 'Textile Bending Actuator', '#F01EAA'),
    Edge('UIUC STUDENT 6', 'UIUC STUDENT 11', 'Textile Bending Actuator', '#F01EAA'),
    Edge('SRT MNT', 'UIUC STUDENT 11', 'Textile Bending Actuator', '#F01EAA'),
    Edge('UIUC STUDENT 6', 'UIUC STUDENT 9', 'Textile Bending Actuator', '#F01EAA'),
    Edge('SRT MNT', 'UIUC STUDENT 9', 'Textile Bending Actuator', '#F01EAA'),
    Edge('SRT MNT', 'UIUC STUDENT 12', 'Textile Bending Actuator', '#F01EAA'),
    Edge('UIUC STUDENT 8', 'UIUC STUDENT 12', 'Textile Bending Actuator', '#F01EAA'),

    #Pneumatic Controller
    Edge('HAR MENTOR 1', 'UIUC MENTOR 1', "Pneumatic Controller", '#009999'),
    Edge('HAR MENTOR 1', 'UIUC STUDENT 8', "Pneumatic Controller", '#009999'),
    Edge('HAR MENTOR 1', 'UIUC STUDENT 7', "Pneumatic Controller", '#009999'),

    #Textiles Workshop
    Edge('HAR MENTOR 3', 'UIUC STUDENT 2', 'Textiles Workshop', '#999966'),
    Edge('HAR MENTOR 3', 'UIUC STUDENT 6', 'Textiles Workshop', '#999966'),
    Edge('HAR MENTOR 3', 'UIUC STUDENT 8', 'Textiles Workshop', '#999966'),
    Edge('HAR MENTOR 3', 'UIUC STUDENT 10', 'Textiles Workshop', '#999966'),
    Edge('HAR MENTOR 3', 'BH STUDENT 1', 'Textiles Workshop', '#999966'),
    Edge('HAR MENTOR 3', 'BH STUDENT 2', 'Textiles Workshop', '#999966'),


    #Soldering cables to SIA Finger
    Edge('HAR MENTOR 1', 'BH STUDENT 1', 'Soldering cables to SIA Finger', '#05FA48'),

    #Gluing SIA finger to glove
    Edge('HAR MENTOR 1', 'BH STUDENT 1', 'Gluing SIA finger to glove', '#05FA48'),

    #Design Workshop
    Edge('UIUC MENTOR 2', 'BH STUDENT 1', 'Design Workshop', '#FA4F05'),
    Edge('UIUC MENTOR 2', 'BH STUDENT 2', 'Design Workshop', '#FA4F05'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 1 YR 2', 'Design Workshop', '#FA4F05'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 2', 'Design Workshop', '#FA4F05'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 3', 'Design Workshop', '#FA4F05'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 4', 'Design Workshop', '#FA4F05'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 5', 'Design Workshop', '#FA4F05'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 6', 'Design Workshop', '#FA4F05'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 7', 'Design Workshop', '#FA4F05'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 8', 'Design Workshop', '#FA4F05'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 9', 'Design Workshop', '#FA4F05'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 10', 'Design Workshop', '#FA4F05'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 11', 'Design Workshop', '#FA4F05'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 12', 'Design Workshop', '#FA4F05'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 13 YR 2', 'Design Workshop', '#FA4F05'),
    Edge('UIUC MENTOR 2', 'UIUC STUDENT 14', 'Design Workshop', '#FA4F05'),


]


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

    def add_nodes(self):
        for node in self.nodes:
            if 'BH' in node.data:
                if 'MENTOR' in node.data:
                    self.net.add_node(node.data, value=14 * (1 + (node.out_going_edges_count / len(self.edges))), color = 'Red', physics=True ,title = str(node.out_going_edges_count), shape='diamond')
                else:
                    self.net.add_node(node.data, value=14 * (1 + (node.out_going_edges_count / len(self.edges))), color='Red', physics=True ,title=str(node.out_going_edges_count))

            elif 'HAR' in node.data:
                if 'MENTOR' in node.data:
                    self.net.add_node(node.data, value=14 * (1 + (node.out_going_edges_count / len(self.edges))), color = '#A41034', physics=True ,title = str(node.out_going_edges_count), shape='diamond')
                else:
                    self.net.add_node(node.data, value=14 * (1 + (node.out_going_edges_count / len(self.edges))),color='#A41034', physics=True ,title=str(node.out_going_edges_count))

            elif 'UIUC' in node.data:
                if  'MENTOR' in node.data:
                    self.net.add_node(node.data, value = 14 * (1 + (node.out_going_edges_count / len( self.edges))), color = '#1F4096', borderWidth = '1', physics=True ,title = str(node.out_going_edges_count), shape='diamond')
                else:
                    self.net.add_node(node.data, value = 14 * (1 + (node.out_going_edges_count / len( self.edges))), color = '#1F4096', borderWidth = '1', physics=True ,title = str(node.out_going_edges_count))
            elif 'SRT MNT' in node.data:
                if  'MNT' in node.data:
                    self.net.add_node(node.data, value = 14 * (1 + (node.out_going_edges_count / len( self.edges))), color = 'black', physics=True ,borderWidth = '1', title = str(node.out_going_edges_count), shape='diamond')
                else:
                    self.net.add_node(node.data, value=14 * (1 + (node.out_going_edges_count / len(self.edges))), color='Black', physics=True ,title = str(node.out_going_edges_count))

    def add_edges(self):
        if self.type == 'WEIGHTED':
            for i in range(len(nodes)):
                self.indexToNameDict[nodes[i].data] = i

            for edge in self.edges:
                self.adjacencyMatrix[self.indexToNameDict[edge.start]][self.indexToNameDict[edge.end]] += 1

            for edge in self.edges:
                if edge.title == self.activity or not self.activity:
                    self.net.add_edge(edge.start, edge.end, title=edge.title, color='black', physics=True ,smooth=True, smoothtype='dynamic',
                                    width=1 + 2 * self.adjacencyMatrix[self.indexToNameDict[edge.start]][self.indexToNameDict[edge.end]])

        elif self.type == 'NORMAL':
            print('here1')
            if self.activity == '' or self.activity == 'ALL':
                print('here2')
                for edge in self.edges:
                    self.net.add_edge(edge.start, edge.end, title=edge.title, color=edge.color, physics=False, smooth=True, smoothtype='dynamic')
            else:
                for edge in self.edges:
                    if edge.title == self.activity or not self.activity:
                        self.net.add_edge(edge.start, edge.end, title=edge.title, color=edge.color, physics=True ,smooth=True, smoothtype='dynamic')


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
while val.upper() != 'END':
    print("please type weighted or normal")
    graph_type = input()
    print("Please type desired activity or leave press enter for all activities")
    activity = input()

    graph = Graph(nodes, edges1, graph_type, activity)
    graph.show_graph()
    graph.net.edges.clear()
    print("press 'enter' to select more graphs or type 'End' to finish")
    val = input()