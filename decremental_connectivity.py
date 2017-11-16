# jamb 2017


# input a rooted tree
# return (top tree, list of bottom trees)
def leaf_trimming(tree):
    pass

# input a rooted tree
# find a path decomposition and return a list of paths (where each path is a list)
def compress_tree(tree):
    pass


# TreeNode class points to other TreeNodes (its children) and stores some properties
class TreeNode:

    # constructor
    def __init__(self):
        self.children = []
        self.in_top = True
        self.bottom_tree_root = None
        self.top_tree_path = None

    def add_child(self, child):
        self.children.append(child)


# BottomTreeRoot is a type of TreeNode that also stores info about the bottom-tree
class BottomTreeRoot(TreeNode):

    def __init__(self):
        super()
        self.nonexistent_edges = []  # this should be a bitvector of what edges we've removed; starts empty, update as we go


# the class we've all been waiting for... i.e. the one that can do queries and deletes
class DecrementalConnectivityTree:

    # constructor
    def __init__(self, tree):
        self.top_tree, self.bottom_trees = leaf_trimming(tree)
        self.masks = {}  # map nodes to their masks
        self._preprocess_masks() 

    # set all the masks
    def _preprocess_masks(self):
        pass

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
        pass

    # inputs v and w must both be nodes in the top
    # return True if connected in compressed top tree, False otherwise
    def _query_compressed_top_connectivity(self, v, w):
        pass

    # inputs v and w must both be nodes in the top, in the same path
    # return True if connected in compressed top tree, False otherwise
    def _query_top_path_connectivity(self, v, w):
        pass
    
