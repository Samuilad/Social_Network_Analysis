from pyvis.network import Network
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
        self.title = title
        self.color = color

# people/resources involved
nodes = [Node('SRT MNT'), Node('Alyssa Bradshaw UIUC'), Node('Samuil Donchev UIUC'), Node('Maya Grant UIUC'), Node('Cornell Horne UIUC'),
         Node('Jorge Jimenez UIUC'), Node('Jacob Lozano UIUC'), Node('Raefa Malik UIUC'), Node('David Medina UIUC'),
         Node('Linda Nguessan UIUC'), Node('Charmaine Nieves UIUC'), Node('Omolola Okesanjo UIUC'), Node('Diana Pham UIUC'),
         Node('Adia Radecka UIUC'), Node('Joshua Sekyere UIUC'), Node('Ilalee Harrison UIUC'), Node('Ayoub Ellouzi BH'),
         Node('Trang Nguyen BH'), Node('Dr. Golecki UIUC MNT'), Node('Professor Siggelkoe BH MNT'), Node('Jessee Grupper HAR MNT'), Node('Alex Beaudette HAR MNT'), Node('Tazzy Cole HAR MNT')]

# Displays the connection between teacher and student
edges1 = [
    # McKibbens
    Edge('SRT MNT', 'Samuil Donchev UIUC', 'McKibbens Muscle', 'blue'),
    Edge('Dr. Golecki UIUC MNT', 'Alyssa Bradshaw UIUC', 'McKibbens Muscle', 'blue'),
    Edge('Dr. Golecki UIUC MNT', 'Maya Grant UIUC', 'McKibbens Muscle', 'blue'),
    Edge('Dr. Golecki UIUC MNT', 'Cornell Horne UIUC', 'McKibbens Muscle', 'blue'),
    Edge('Dr. Golecki UIUC MNT', 'Jorge Jimenez UIUC', 'McKibbens Muscle', 'blue'),
    Edge('Dr. Golecki UIUC MNT', 'Jacob Lozano UIUC', 'McKibbens Muscle', 'blue'),
    Edge('Dr. Golecki UIUC MNT', 'Raefa Malik UIUC', 'McKibbens Muscle', 'blue'),
    Edge('Dr. Golecki UIUC MNT', 'David Medina UIUC', 'McKibbens Muscle', 'blue'),
    Edge('Dr. Golecki UIUC MNT', 'Linda Nguessan UIUC', 'McKibbens Muscle', 'blue'),
    Edge('Dr. Golecki UIUC MNT', 'Charmaine Nieves UIUC', 'McKibbens Muscle', 'blue'),
    Edge('Dr. Golecki UIUC MNT', 'Omolola Okesanjo UIUC', 'McKibbens Muscle', 'blue'),
    Edge('Samuil Donchev UIUC', 'Diana Pham UIUC', 'McKibbens Muscle', 'blue'),
    Edge('Dr. Golecki UIUC MNT', 'Adia Radecka UIUC', 'McKibbens Muscle', 'blue'),
    Edge('Omolola Okesanjo UIUC', 'Joshua Sekyere UIUC', 'McKibbens Muscle', 'blue'),
    Edge('Professor Siggelkoe BH MNT', 'Ayoub Ellouzi BH', 'McKibbens Muscle', 'blue'),
    Edge('Professor Siggelkoe BH MNT', 'Trang Nguyen BH', 'McKibbens Muscle', 'blue'),

    # Heat Sealable Fabric Brace or Folding Box
    Edge('Dr. Golecki UIUC MNT', 'Alyssa Bradshaw UIUC', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('Joshua Sekyere UIUC', 'Maya Grant UIUC', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('Dr. Golecki UIUC MNT', 'Cornell Horne UIUC', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('Diana Pham UIUC', 'Jorge Jimenez UIUC', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('Charmaine Nieves UIUC', 'Jacob Lozano UIUC', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('SRT MNT', 'Jacob Lozano UIUC', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('Diana Pham UIUC', 'David Medina UIUC', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('Diana Pham UIUC', 'Charmaine Nieves UIUC', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('Joshua Sekyere UIUC', 'Omolola Okesanjo UIUC', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('Dr. Golecki UIUC MNT', 'Diana Pham UIUC', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('Dr. Golecki UIUC MNT', 'Adia Radecka UIUC', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('Dr. Golecki UIUC MNT', 'Joshua Sekyere UIUC', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('Professor Siggelkoe BH MNT', 'Ayoub Ellouzi BH', 'Heat Sealable Fabric Brace or Folding Box', 'black'),
    Edge('Professor Siggelkoe BH MNT', 'Trang Nguyen BH', 'Heat Sealable Fabric Brace or Folding Box', 'black'),

    # SDM Finger
    Edge('Adia Radecka UIUC', 'Alyssa Bradshaw UIUC', 'SDM Finger', 'green'),
    Edge('Alyssa Bradshaw UIUC', 'Samuil Donchev UIUC', 'SDM Finger', 'green'),
    Edge('Alyssa Bradshaw UIUC', 'Maya Grant UIUC', 'SDM Finger', 'green'),
    Edge('Alyssa Bradshaw UIUC', 'Cornell Horne UIUC', 'SDM Finger', 'green'),
    Edge('Alyssa Bradshaw UIUC', 'Jorge Jimenez UIUC', 'SDM Finger', 'green'),
    Edge('Adia Radecka UIUC', 'Jorge Jimenez UIUC', 'SDM Finger', 'green'),
    Edge('Alyssa Bradshaw UIUC', 'Jacob Lozano UIUC', 'SDM Finger', 'green'),
    Edge('Adia Radecka UIUC', 'Jacob Lozano UIUC', 'SDM Finger', 'green'),
    Edge('Alyssa Bradshaw UIUC', 'Raefa Malik UIUC', 'SDM Finger', 'green'),
    Edge('Adia Radecka UIUC', 'Raefa Malik UIUC', 'SDM Finger', 'green'),
    Edge('Alyssa Bradshaw UIUC', 'David Medina UIUC', 'SDM Finger', 'green'),
    Edge('Adia Radecka UIUC', 'David Medina UIUC', 'SDM Finger', 'green'),
    Edge('Alyssa Bradshaw UIUC', 'Linda Nguessan UIUC', 'SDM Finger', 'green'),
    Edge('Adia Radecka UIUC', 'Linda Nguessan UIUC', 'SDM Finger', 'green'),
    Edge('Alyssa Bradshaw UIUC', 'Charmaine Nieves UIUC', 'SDM Finger', 'green'),
    Edge('Adia Radecka UIUC', 'Charmaine Nieves UIUC', 'SDM Finger', 'green'),
    Edge('Alyssa Bradshaw UIUC', 'Omolola Okesanjo UIUC', 'SDM Finger', 'green'),
    Edge('Adia Radecka UIUC', 'Omolola Okesanjo UIUC', 'SDM Finger', 'green'),
    Edge('Alyssa Bradshaw UIUC', 'Diana Pham UIUC', 'SDM Finger', 'green'),
    Edge('Adia Radecka UIUC', 'Diana Pham UIUC', 'SDM Finger', 'green'),
    Edge('Dr. Golecki UIUC MNT', 'Adia Radecka UIUC', 'SDM Finger', 'green'),
    Edge('Alyssa Bradshaw UIUC', 'Joshua Sekyere UIUC', 'SDM Finger', 'green'),
    Edge('Adia Radecka UIUC', 'Joshua Sekyere UIUC', 'SDM Finger', 'green'),
    Edge('Samuil Donchev UIUC', 'Ayoub Ellouzi BH', 'SDM Finger', 'green'),
    Edge('Trang Nguyen BH', 'Ayoub Ellouzi BH', 'SDM Finger', 'green'),
    Edge('Samuil Donchev UIUC', 'Trang Nguyen BH', 'SDM Finger', 'green'),
    Edge('SRT MNT', 'Trang Nguyen BH', 'SDM Finger', 'green'),

    # Motorized SDM Finger
    Edge('Alyssa Bradshaw UIUC', 'Alyssa Bradshaw UIUC', 'Motorized SDM Finger', 'red'),
    Edge('Alyssa Bradshaw UIUC', 'Samuil Donchev UIUC', 'Motorized SDM Finger', 'red'),
    Edge('Adia Radecka UIUC', 'Samuil Donchev UIUC', 'Motorized SDM Finger', 'red'),
    Edge('Adia Radecka UIUC', 'Jacob Lozano UIUC', 'Motorized SDM Finger', 'red'),
    Edge('Alyssa Bradshaw UIUC', 'Jacob Lozano UIUC', 'Motorized SDM Finger', 'red'),
    Edge('Adia Radecka UIUC', 'Adia Radecka UIUC', 'Motorized SDM Finger', 'red'),
    Edge('Professor Siggelkoe BH MNT', 'Ayoub Ellouzi BH', 'Motorized SDM Finger', 'red'),
    Edge('Professor Siggelkoe BH MNT', 'Trang Nguyen BH', 'Motorized SDM Finger', 'red'),

    # SIA Actuator
    Edge('Dr. Golecki UIUC MNT', 'Alyssa Bradshaw UIUC', 'SIA Actuator', 'purple'),
    Edge('Alyssa Bradshaw UIUC', 'Samuil Donchev UIUC', 'SIA Actuator', 'purple'),
    Edge('David Medina UIUC', 'Cornell Horne UIUC', 'SIA Actuator', 'purple'),
    Edge('Alyssa Bradshaw UIUC', 'Jorge Jimenez UIUC', 'SIA Actuator', 'purple'),
    Edge('Adia Radecka UIUC', 'Jorge Jimenez UIUC', 'SIA Actuator', 'purple'),
    Edge('Alyssa Bradshaw UIUC', 'Jacob Lozano UIUC', 'SIA Actuator', 'purple'),
    Edge('Adia Radecka UIUC', 'Jacob Lozano UIUC', 'SIA Actuator', 'purple'),
    Edge('Adia Radecka UIUC', 'David Medina UIUC', 'SIA Actuator', 'purple'),
    Edge('Alyssa Bradshaw UIUC', 'David Medina UIUC', 'SIA Actuator', 'purple'),
    Edge('Adia Radecka UIUC', 'Charmaine Nieves UIUC', 'SIA Actuator', 'purple'),
    Edge('Alyssa Bradshaw UIUC', 'Charmaine Nieves UIUC', 'SIA Actuator', 'purple'),
    Edge('Adia Radecka UIUC', 'Omolola Okesanjo UIUC', 'SIA Actuator', 'purple'),
    Edge('Alyssa Bradshaw UIUC', 'Omolola Okesanjo UIUC', 'SIA Actuator', 'purple'),
    Edge('Alyssa Bradshaw UIUC', 'Diana Pham UIUC', 'SIA Actuator', 'purple'),
    Edge('Dr. Golecki UIUC MNT', 'Adia Radecka UIUC', 'SIA Actuator', 'purple'),
    Edge('Adia Radecka UIUC', 'Joshua Sekyere UIUC', 'SIA Actuator', 'purple'),
    Edge('Alyssa Bradshaw UIUC', 'Joshua Sekyere UIUC', 'SIA Actuator', 'purple'),
    Edge('Professor Siggelkoe BH MNT', 'Ayoub Ellouzi BH', 'SIA Actuator', 'purple'),
    Edge('Professor Siggelkoe BH MNT', 'Trang Nguyen BH', 'SIA Actuator', 'purple'),

    # Capacitance Sensor
    Edge('Samuil Donchev UIUC', 'Alyssa Bradshaw UIUC', 'Capacitance Sensor', 'brown'),
    Edge('Dr. Golecki UIUC MNT', 'Samuil Donchev UIUC', 'Capacitance Sensor', 'brown'),
    Edge('Dr. Golecki UIUC MNT', 'Jorge Jimenez UIUC', 'Capacitance Sensor', 'brown'),
    Edge('Dr. Golecki UIUC MNT', 'Jacob Lozano UIUC', 'Capacitance Sensor', 'brown'),
    Edge('Dr. Golecki UIUC MNT', 'David Medina UIUC', 'Capacitance Sensor', 'brown'),
    Edge('Dr. Golecki UIUC MNT', 'Charmaine Nieves UIUC', 'Capacitance Sensor', 'brown'),
    Edge('Dr. Golecki UIUC MNT', 'Omolola Okesanjo UIUC', 'Capacitance Sensor', 'brown'),
    Edge('Samuil Donchev UIUC', 'Diana Pham UIUC', 'Capacitance Sensor', 'brown'),
    Edge('Omolola Okesanjo UIUC', 'Joshua Sekyere UIUC', 'Capacitance Sensor', 'brown'),

    # Flex Sensor
    Edge('David Medina UIUC', 'Samuil Donchev UIUC', 'Flex Sensor', 'Orange'),
    Edge('Cornell Horne UIUC', 'Maya Grant UIUC', 'Flex Sensor', 'Orange'),
    Edge('Dr. Golecki UIUC MNT', 'Cornell Horne UIUC', 'Flex Sensor', 'Orange'),
    Edge('David Medina UIUC', 'Jorge Jimenez UIUC', 'Flex Sensor', 'Orange'),
    Edge('Charmaine Nieves UIUC', 'Jacob Lozano UIUC', 'Flex Sensor', 'Orange'),
    Edge('SRT MNT', 'Jacob Lozano UIUC', 'Flex Sensor', 'Orange'),
    Edge('SRT MNT', 'Raefa Malik UIUC', 'Flex Sensor', 'Orange'),
    Edge('Dr. Golecki UIUC MNT', 'David Medina UIUC', 'Flex Sensor', 'Orange'),
    Edge('Omolola Okesanjo UIUC', 'David Medina UIUC', 'Flex Sensor', 'Orange'),
    Edge('Dr. Golecki UIUC MNT', 'Linda Nguessan UIUC', 'Flex Sensor', 'Orange'),
    Edge('Dr. Golecki UIUC MNT', 'Charmaine Nieves UIUC', 'Flex Sensor', 'Orange'),
    Edge('Dr. Golecki UIUC MNT', 'Omolola Okesanjo UIUC', 'Flex Sensor', 'Orange'),
    Edge('SRT MNT', 'Diana Pham UIUC', 'Flex Sensor', 'Orange'),
    Edge('SRT MNT', 'Joshua Sekyere UIUC', 'Flex Sensor', 'Orange'),
    Edge('Professor Siggelkoe BH MNT', 'Ayoub Ellouzi BH', 'Flex Sensor', 'Orange'),
    Edge('Professor Siggelkoe BH MNT', 'Trang Nguyen BH', 'Flex Sensor', 'Orange'),

    # Textile Bending Actuator
    Edge('Jorge Jimenez UIUC', 'Samuil Donchev UIUC', 'Textile Bending Actuator', 'pink'),
    Edge('Jacob Lozano UIUC', 'Cornell Horne UIUC', 'Textile Bending Actuator', 'pink'),
    Edge('David Medina UIUC', 'Cornell Horne UIUC', 'Textile Bending Actuator', 'pink'),
    Edge('SRT MNT', 'Cornell Horne UIUC', 'Textile Bending Actuator', 'pink'),
    Edge('Jacob Lozano UIUC', 'Jorge Jimenez UIUC', 'Textile Bending Actuator', 'pink'),
    Edge('David Medina UIUC', 'Jorge Jimenez UIUC', 'Textile Bending Actuator', 'pink'),
    Edge('SRT MNT', 'Jorge Jimenez UIUC', 'Textile Bending Actuator', 'pink'),
    Edge('SRT MNT', 'Jacob Lozano UIUC', 'Textile Bending Actuator', 'pink'),
    Edge('SRT MNT', 'David Medina UIUC', 'Textile Bending Actuator', 'pink'),
    Edge('Jacob Lozano UIUC', 'David Medina UIUC', 'Textile Bending Actuator', 'pink'),
    Edge('Jacob Lozano UIUC', 'Charmaine Nieves UIUC', 'Textile Bending Actuator', 'pink'),
    Edge('SRT MNT', 'Charmaine Nieves UIUC', 'Textile Bending Actuator', 'pink'),
    Edge('Jacob Lozano UIUC', 'Omolola Okesanjo UIUC', 'Textile Bending Actuator', 'pink'),
    Edge('SRT MNT', 'Omolola Okesanjo UIUC', 'Textile Bending Actuator', 'pink'),
    Edge('SRT MNT', 'Diana Pham UIUC', 'Textile Bending Actuator', 'pink'),
    Edge('David Medina UIUC', 'Diana Pham UIUC', 'Textile Bending Actuator', 'pink'),

    #Pneumatic Controller
    Edge('Jessee Grupper HAR MNT', 'Ilalee Harrison UIUC', "Pneumatic Controller", '#009999'),
    Edge('Jessee Grupper HAR MNT', 'David Medina UIUC', "Pneumatic Controller", '#009999'),
    Edge('Jessee Grupper HAR MNT', 'Raefa Malik UIUC', "Pneumatic Controller", '#009999'),

    #Textiles Workshop
    Edge('Tazzy Cole HAR MNT', 'Samuil Donchev UIUC', 'Textiles Workshop', '#999966'),
    Edge('Tazzy Cole HAR MNT', 'Jacob Lozano UIUC', 'Textiles Workshop', '#999966'),
    Edge('Tazzy Cole HAR MNT', 'David Medina UIUC', 'Textiles Workshop', '#999966'),
    Edge('Tazzy Cole HAR MNT', 'Linda Nguessan UIUC', 'Textiles Workshop', '#999966'),
    Edge('Tazzy Cole HAR MNT', 'Ayoub Ellouzi BH', 'Textiles Workshop', '#999966')
    Edge('Tazzy Cole HAR MNT', 'Trang Nguyen BH', 'Textiles Workshop', '#999966'),

]

edges2 = [
    #Golecki edges

    Edge('Dr.Golecki','Alyssa Bradshaw UIUC', 'McKibbens Muscle - Heat Sealable Fabric Brace/Folding Box' + '\n' + 'SIA Actuator', 'Orange'),
    Edge('Dr.Golecki','Maya Grant UIUC','McKibbens Muscle', 'Orange'),
    Edge('Dr.Golecki','Cornell Horne UIUC','McKibbens Muscle', 'Orange'),
    Edge('Dr.Golecki','Jorge Jimenez UIUC', 'McKibbens Muscle', 'Orange'),
    Edge('Dr.Golecki','Jacob Lozano UIUC', 'McKibbens Muscle', 'Orange'),
    Edge('Dr.Golecki','Raefa Malik UIUC', 'McKibbens Muscle', 'Orange'),
    Edge('Dr.Golecki','David Medina UIUC', 'McKibbens Muscle', 'Orange'),
    Edge('Dr.Golecki','Linda Nguessan UIUC', 'McKibbens Muscle', 'Orange'),
    Edge('Dr.Golecki','Charmaine Nieves UIUC', 'McKibbens Muscle', 'Orange'),
    Edge('Dr.Golecki','Omolola Okesanjo UIUC', 'McKibbens Muscle', 'Orange'),
    Edge('Dr.Golecki','Adia Radecka UIUC', 'McKibbens Muscle', 'Orange'),
    Edge('Dr.Golecki', 'Cornell Horne UIUC', 'Heat Sealable Fabric Brace/Folding Box', 'Orange'),
    Edge('Dr.Golecki', 'Diana Pham UIUC', 'Heat Sealable Fabric Brace/Folding Box', 'Orange'),
    Edge('Dr.Golecki', 'Adia Radecka UIUC', 'Heat Sealable Fabric Brace/Folding Box', 'Orange'),
    Edge('Dr.Golecki', 'Joshua Sekyere UIUC', 'Heat Sealable Fabric Brace/Folding Box', 'Orange'),

]


class Graph:
    nodes = []
    edges = []
    net = Network(directed=True, height=1500, width=1500)

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
                if 'MNT' in node.data:
                    self.net.add_node(node.data, value=14 * (1 + (node.out_going_edges_count / len(self.edges))), color = 'Red', title = str(node.out_going_edges_count), shape='diamond')
                else:
                    self.net.add_node(node.data, value=14 * (1 + (node.out_going_edges_count / len(self.edges))), color='Red', title=str(node.out_going_edges_count))

            elif 'HAR' in node.data:
                if 'MNT' in node.data:
                    self.net.add_node(node.data, value=14 * (1 + (node.out_going_edges_count / len(self.edges))), color = 'Brown', title = str(node.out_going_edges_count), shape='diamond')
                else:
                    self.net.add_node(node.data, value=14 * (1 + (node.out_going_edges_count / len(self.edges))),color='Brown', title=str(node.out_going_edges_count))

            elif 'UIUC' in node.data:
                if  'MNT' in node.data:
                    self.net.add_node(node.data, value = 14 * (1 + (node.out_going_edges_count / len( self.edges))), color = '#E84A27', borderWidth = '1', title = str(node.out_going_edges_count), shape='diamond')
                else:
                    self.net.add_node(node.data, value = 14 * (1 + (node.out_going_edges_count / len( self.edges))), color = '#E84A27', borderWidth = '1', title = str(node.out_going_edges_count))
            elif 'SRT MNT' in node.data:
                if  'MNT' in node.data:
                    self.net.add_node(node.data, value = 14 * (1 + (node.out_going_edges_count / len( self.edges))), color = 'black', borderWidth = '1', title = str(node.out_going_edges_count), shape='diamond')
                else:
                    self.net.add_node(node.data, value=14 * (1 + (node.out_going_edges_count / len(self.edges))), color='Black', title = str(node.out_going_edges_count))

        # adds each edge to graph
        for edge in self.edges:
            self.net.add_edge(edge.start, edge.end, title=edge.title, color=edge.color, smooth=True, smoothtype='dynamic')

        self.net.show_buttons(filter_=['physics', 'edges', 'nodes'])
        #self.net.show_buttons(filter_=['physics'])

        #set Physics Model
        self.net.repulsion(node_distance=160, central_gravity=0.2, spring_length=200, spring_strength=0.0025, damping=0.09)

        #make edges rounded and dynamically placed
        self.net.set_edge_smooth('continuous')

        # displays the graph
        self.net.show('basic.html')


graph = Graph(nodes, edges1)

graph.show_graph()