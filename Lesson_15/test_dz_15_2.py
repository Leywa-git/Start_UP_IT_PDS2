import pytest
from dz_15_2 import Tree
from dz_15_2 import nodes, root_node


def test_append_new_nodes():
    root_node.append_new_nodes(nodes)
    assert root_node.min_node() == 1


def test_min_node():
    root_node.insert(0)
    assert root_node.min_node() != 1


def test_max_node():
    root_node.insert(25)
    assert root_node.max_node() == 25


def test_node_delete():
    root_node.node_delete(root_node, 25)
    assert root_node.max_node() != 25
