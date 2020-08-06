from src.objects.table import Table
from src.struct.tree import Node

class Schema(Node):
    def __init__(self, parent, name, data):
        Node.__init__(self, parent, name)
        self._children = self._construct_children(data)

    def _construct_children(self, data):
        return self.__construct_children__(Table, 'table_name')(data)