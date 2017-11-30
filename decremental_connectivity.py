# jamb 2017


# input a rooted tree
# return (top tree, list of bottom trees)
def leaf_trimming(tree):
    pass
    return None, []

# input a rooted tree
# find a path decomposition and return a list of paths (where each path is a list)
def compress_tree(tree):
    path_decomp = []
    path_queue = [[tree]]
    while (len(path_queue) > 0):
        path = path_queue.pop(0)
        node = path[-1]
        if len(node.children) == 0:
            path_decomp.append(path)
        elif len(node.children) == 1:
            path_queue.append(path + node.children)
        else:
            path_queue.append(path + [node.children[0]])
            for i in range(1, len(node.children)):
                path_queue.append([node.children[i]])
    return path_decomp


# TreeNode class points to other TreeNodes (its children) and stores some properties
class TreeNode:

    # constructor
    def __init__(self, value):
        self.value = value
        self.children = []
        self.in_top = True
        self.bottom_tree_root = None
        self.top_tree_path = None

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return self.stringify(0)

    def stringify(self, indent):
        ret = "--"*indent + str(self.value) + "\n"
        for child in self.children:
            ret += child.stringify(indent + 1)
        return ret


# BottomTreeRoot is a type of TreeNode that also stores info about the bottom-tree
class BottomTreeRoot(TreeNode):

    def __init__(self, value):
        super(value)
        self.nonexistent_edges = 0  # this should be a bitvector of what edges we've removed; starts empty, update as we go


# the class we've all been waiting for... i.e. the one that can do queries and deletes
class DecrementalConnectivityTree:

    # constructor
    def __init__(self, tree):
        self.N = self._get_N(tree)
        self.top_tree, self.bottom_trees = leaf_trimming(tree)
        self.masks = {}  # map nodes to their masks
        self._preprocess_masks()


    # figure out how many nodes are in the tree total
    def _get_N(self, tree):
        count = 0
        count_queue = [tree]
        while (count_queue):
            node = count_queue.pop(0)
            count += 1
            count_queue += node.children
        return count
            

    # set all the masks
    def _preprocess_masks(self):
        for tree_root in self.bottom_trees:
            self.masks[tree_root] = 1
            nodes_processed = 1
            assign_mask_queue = [(c, 1) for c in tree_root.children]  # pairs of child, parent-mask
            while (assign_mask_queue):
                node, parent_mask = assign_mask_queue.pop(0)
                node_mask = parent_mask + (1 << nodes_processed)
                self.masks[node] = node_mask
                nodes_processed += 1
                assign_mask_queue += [(c, node_mask) for c in node.children]
        return

    # return True if nodes v and w are connected in the tree, False otherwise
    def query_connectivity(self, v, w):
        pass

    # remove the edge directly connecting v and w (v must be the parent and w the child)
    # return True if succeeded and False if failed (i.e. there wasn't an edge there); no modifications occur if False
    def delete_edge(self, v, w):
        pass

    # inputs v and w must be nodes in the same bottom tree
    # (so if you want to query about two things that aren't, query v to root(v's bottom tree), etc.
    # return True if connected in bottom tree, False otherwise
    def _query_bottom_connectivity(self, v, w):
        assert (v.bottom_tree_root is w.bottom_tree_root)
        original_path = v ^ w
        deleted_edges = v.bottom_tree_root.nonexistent_edges
        deleted_on_path = original_path & deleted_edges
        return deleted_on_path == 0
        

    # inputs v and w must both be nodes in the top
    # return True if connected in compressed top tree, False otherwise
    def _query_compressed_top_connectivity(self, v, w):
        pass

    # inputs v and w must both be nodes in the top, in the same path
    # return True if connected in compressed top tree, False otherwise
    def _query_top_path_connectivity(self, v, w):
        pass




def test_tree_compression():
    root = TreeNode(5)
    c1 = TreeNode(4)
    root.add_child(c1)
    c2 = TreeNode(4)
    root.add_child(c2)
    c3 = TreeNode(0)
    root.add_child(c3)
    c1.add_child(TreeNode(6))
    print(root)
    print(compress_tree(root))
    d = DecrementalConnectivityTree(root)
    print(d.N)

test_tree_compression()
    
