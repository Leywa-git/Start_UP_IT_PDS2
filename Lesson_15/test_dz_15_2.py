import pytest
from dz_15_2 import Tree
from dz_15_2 import nodes, root_node

n = nodes
r = root_node


def test_append_new_nodes():
    r.append_new_nodes(n)
    assert r.min_node() == 1
    assert r.max_node() == 15


def test_min_node():
    r.insert(0)
    assert r.min_node() != 1


def test_max_node():
    r.insert(25)
    assert r.max_node() == 25


def test_node_delete():
    r.node_delete(r, 25)
    assert r.max_node() != 25
