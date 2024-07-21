import networkx as nx

class ShariahKnowledgeGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_entity(self, entity, label):
        self.graph.add_node(entity, label=label)

    def add_relationship(self, entity1, entity2, relationship):
        self.graph.add_edge(entity1, entity2, relationship=relationship)
