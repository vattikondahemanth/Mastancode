#
# template file for binary tree dfs programming assignment 2
#
#   NOTE this file contains an incomplete implementation of some parts
#       of the binary tree problem
#
#
#   be sure to read the problem description on bblearn carefully
#   be sure to use your IDE (e.g. VSCode) effectively to implement your solution
#
#   you will need to add code where i've put in 'pass'
#   you may need to add code other places as well
#
#   HINTS:
#       remember to breathe
#       smile
#       find your rhythm
#
# andy cohen march 4 2021
import matplotlib.pyplot as plt


class BinaryTree:
    def __init__(self, nNodes=0):
        # initialize tree structures, build default tree
        self.nodeChildren = dict()
        self.nodeParent = dict()
        self.treeXY = dict()
        self.roots = []

        # add nodes will call set roots and dfstraverse
        self.addNodes(1)

    def addTrio(self, parent, leftChild, rightChild):
        # add leftChild,rightChild to tree
        self.nodeChildren[parent] = (leftChild, rightChild)
        self.nodeParent[leftChild] = parent
        self.nodeParent[rightChild] = parent

    def setRoots(self):
        # for this problem set, there is a single root node. sometimes trees can
        # have multiple roots though, so we keep that option here.
        #
        for p in self.nodes():
            if p not in self.nodeParent.keys() and p not in self.roots:
                self.roots.append(p)

    def dfsTraverseRecursive(self, node, dfsNodeList, xMaxLeaf=0, yNode=0):

        # traverse the tree using dfs. set x and y location as we go.
        # find my children
        if node in self.nodeChildren.keys():
            (cLeft, cRight) = self.nodeChildren[node]
            # traverse left child
            (dfsNodeList, xMaxLeaf) = self.dfsTraverseRecursive(cLeft, dfsNodeList, xMaxLeaf, yNode + 1)
            # traverse right child
            (dfsNodeList, xMaxLeaf) = self.dfsTraverseRecursive(cRight, dfsNodeList, xMaxLeaf, yNode + 1)
            # after we're done with both children, set parent x midway between children x location.
            # what do we set for parent y?
            # import pdb
            # pdb.set_trace()
            x1 = self.treeXY[self.nodeChildren[node][0]][0]
            x2 = self.treeXY[self.nodeChildren[node][1]][0]

            y1 = self.treeXY[self.nodeChildren[node][0]][1]
            y2 = self.treeXY[self.nodeChildren[node][1]][1]
            self.treeXY[node] = ((x1 + x2) / 2, y1 - 1)
        else:
            # node has no children. it's a leaf. set it's x
            self.treeXY[node] = (xMaxLeaf, yNode)
            # increment xMaxLeaf so next leaf goes exactly 1 to the right of me
            xMaxLeaf = xMaxLeaf + 1

        # node's children are done, now add node to the dfsNodeList
        dfsNodeList.append(node)
        # print(dfsNodeList, xMaxLeaf, yNode)
        return (dfsNodeList, xMaxLeaf)

    def nodes(self):
        # import pdb
        # pdb.set_trace()
        # return the set of all nodes in the tree
        nodes = set(self.nodeChildren.keys()).union(set(self.nodeParent.keys()))
        # note - if the tree is empty, return a single root node {0}
        return nodes if len(nodes) else {0}

    def leaves(self):
        # return the set of all leaves in the tree
        # a node is a leaf if it's not in self.nodeChildren.keys():
        leaves = self.nodes() - set(self.nodeChildren.keys())
        return leaves

    def dfsTraverse(self):
        self.setRoots()
        dfs = []
        # each root node will be processed to append its dfs traversal to the dfs list
        # here we will only test / use trees with a single root
        for r in self.roots:
            dfs = self.dfsTraverseRecursive(r, dfs)
        return dfs

    def render(self, node):
        # render node
        xy = self.treeXY[node]
        align = 'center'
        # all plotting with defaults unless otherwise specified
        # plot a vertical blue solid line at node.x from node.y to node.y+1
        pass
        x_values = [self.treeXY[node][0], self.treeXY[node][0]]
        y_values = [self.treeXY[node][1], self.treeXY[node][1] + 1]
        plt.plot(x_values, y_values)

        # text align right for child 0, left for child 1
        if node in self.nodeParent.keys():
            # p is node's parent
            p = self.nodeParent[node]
            # cx are node's parent's two children. node should be one of them.
            cx = self.nodeChildren[p]
            if node == cx[0]:
                align = 'right'
            elif node == cx[1]:
                align = 'left'
                # if node is the left child, align right
            # else align left
        else:
            # no parent - node is the root
            align = 'center'

        plt.xlim(0, 10)
        plt.ylim(0, 5)
        plt.gca().invert_yaxis()
        plt.text(xy[0], xy[1], str(node), horizontalalignment=align)
        # if node has children, draw a horizontal line in solid blue
        # between the two children x locations, at the children y location
        if node in self.nodeChildren.keys():
            # plot horizontal
            pass
            lf_child = self.nodeChildren[node][0]
            rt_child = self.nodeChildren[node][1]
            x_hor_values = [self.treeXY[lf_child][0], self.treeXY[rt_child][0]]
            y_hor_values = [self.treeXY[lf_child][1], self.treeXY[rt_child][1]]
            plt.plot(x_hor_values, y_hor_values)

            # now render the left child then the right child
            leftChild = self.nodeChildren[node][0]
            rightChild = self.nodeChildren[node][1]
            self.render(leftChild)
            self.render(rightChild)

    def addNodes(self, nNodes):
        # import pdb
        # pdb.set_trace()
        # add nNodes new nodes to the tree
        n0 = len(self.nodes())  # current nodes in tree
        nNodes = nNodes + n0  # target tree size
        while len(self.nodes()) + 2 <= nNodes:
            for l in self.leaves():
                if len(self.nodes()) + 2 > nNodes:
                    break
                mm = max(self.nodes())
                self.addTrio(l, mm + 1, mm + 2)
        # after we add new nodes to the tree, we reset everyone's xy locations
        # by invoking a dfsTraverse
        self.dfsTraverse()


def myNumberOfNodes(emailAddress='rp863@drexel.edu'):
    email_hash = 0
    for c in emailAddress:
        email_hash += ord(c)
        return 17 + email_hash % 15


if __name__ == "__main__":
    # test your code here
    b_tree = BinaryTree()
    print(b_tree.nodes())
    print(b_tree.leaves())
    print(b_tree.roots)
    # b_tree.addNodes(myNumberOfNodes())
    b_tree.addNodes(16)
    print(b_tree.nodes())
    print(b_tree.leaves())
    print(b_tree.roots)
    print(b_tree.treeXY)
    print(b_tree.nodeChildren)
    b_tree.render(b_tree.roots[0])
    # print(b_tree.nodes())
    # print(b_tree.leaves())
    # print(b_tree.treeXY)

    # generate your plot here self.treeXY[node]
    # you'll need to use matplotlib invert y axis so plot goes the right direction
    # set the title correctly as in the sample plot
    # set the yticks, ylabel, xticks and xlabel too
    # use ctrl+print screen to copy the matplotlib figure window, then paste it into
    # word (or use latex if you like) for your report. be sure to write your figure
    # caption carefully and follow all instructions
    #
    # plt...
    # plt.show()
    pass
