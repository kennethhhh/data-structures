class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def get_key(self): # return key of node
        return self.key

    def get_data(self): # return data of node
        return self.data

class BinarySearchTree:

    def __init__(self): # Returns empty BST
        self.root = None

    def is_empty(self): #returns True if tree is empty, else False
        if self.root==None:
            return True
        return False

    def search(self, key): # returns True if key is in a node of the tree, else False
        if self.is_empty():
            return False
        return (self.search_helper(self.root,key))

    #helper method for search
    def search_helper(self,root,key):
        if root==None:
            return False
        if root.key==key:
            return True
        if key>root.key:
            return self.search_helper(root.right,key)
        if key<root.key:
            return self.search_helper(root.left,key)




    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # Example creation of node: temp = TreeNode(key, data)
        if self.is_empty():
            self.root=TreeNode(key,data)
        else:
            self.insert_helper(self.root,key,data)

    def insert_helper(self,node,key,data):
        temp=TreeNode(key,data)
        if node.key==key:
            node.data=data
        elif key > node.key:
            if node.right == None:
                node.right = temp
            else:
                self.insert_helper(node.right,key,data)
        else:
            if node.left==None:
                node.left=temp
            else:
                self.insert_helper(node.left,key,data)




    def find_min(self): # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        root=self.root
        while root.left!=None:
            root=root.left
        return (root.key,root.data)

    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        root=self.root
        while root.right!=None:
            root=root.right
        return (root.key,root.data)

    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        if self.is_empty():
            return None
        return (self.height_helper(self.root)-1)

    def height_helper(self,node):
        if node==None:
            return (0)
        right_tree=self.height_helper(node.right)
        left_tree=self.height_helper(node.left)
        if right_tree>left_tree:
            return 1+right_tree
        return 1+left_tree


    def inorder_list(self): # return Python list of BST keys representing in-order traversal of BST
        return (self.inorder_helper(self.root))

    def inorder_helper(self,node):
        python_list = []
        if node:
            python_list = self.inorder_helper(node.left)
            python_list.append(node.key)
            python_list = python_list+ self.inorder_helper(node.right)
        return python_list



    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        return (self.pre_helper(self.root,[]))

    def pre_helper(self, node, python_list):
        if node != None:
            python_list.append(node.key)
            self.pre_helper(node.left,python_list)
            self.pre_helper(node.right,python_list)
        return python_list



    def delete(self,key):# deletes node containing key
        # Will need to consider all cases
        # This is the most difficult method - save it for last, so that
        # if you cannot get it to work, you can still get credit for
        # the other methods
        # Returns True if the item was deleted, False otherwise
        if not self.search(key):
            return False
        elif key==self.root.key and self.root.right==None and self.root.left==None:
            self.root=None
            return True
        elif key==self.root.key:
            if self.root.right==None and self.root.left!=None:
                self.root=self.root.left
            elif self.root.right!=None and self.root.left==None:
                self.root=self.root.right
            elif self.root.right!=None and self.root.left!=None:
                replacement_node=self.delete_find_min(self.root.right)
                replacement_node_parent=self.find_min_parent(replacement_node.key,self.root.right)
                if replacement_node_parent.left==None:
                    replacement_node.left = self.root.left
                    self.root=replacement_node
                else:
                    replacement_node.right=self.root.right
                    replacement_node.left=self.root.left
                    self.root=replacement_node
                    replacement_node_parent=self.find_min_parent(replacement_node.key,replacement_node.right)
                    replacement_node_parent.left=None
            return True

        elif self.search(key):
            parent=self.delete_helper(key,self.root)
            if parent.right!=None:
                #removing right leaf
                if parent.right.key==key and parent.right.right==None and parent.right.left==None:
                    parent.right=None

                #removing right leaf with one child
                elif parent.right.key==key and parent.right.right!=None and parent.right.left==None:
                    parent.right=parent.right.right
                elif parent.right.key==key and parent.right.right==None and parent.right.left!=None:
                    parent.right=parent.right.left

                #removing right leaf with 2 children
                elif parent.right.key==key and parent.right.right!=None and parent.right.left!=None:
                    new_node=self.delete_find_min(parent.right.right)
                    parent_min = self.find_min_parent(new_node.key, parent.right.right)
                    if parent_min.left==None:
                        parent_min.left=parent.right.left
                        parent.right=parent_min
                    else:
                        new_node.left = parent.right.left
                        new_node.right = parent.right.right
                        parent.right=new_node
                        parent_min = self.find_min_parent(new_node.key, parent.right.right)
                        parent_min.left = None


            if parent.left!=None:
                #removing left leaf
                if parent.left.key==key and parent.left.right==None and parent.left.left==None:
                    parent.left=None

                #removing left leaf with one child
                elif parent.left.key==key and parent.left.right!=None and parent.left.left==None:
                    parent.left=parent.left.right
                elif parent.left.key==key and parent.left.right==None and parent.left.left!=None:
                    parent.left=parent.left.left

                #removing left leaf with 2 children
                elif parent.left.key==key and parent.left.right!=None and parent.left.left!=None:
                    new_node=self.delete_find_min(parent.left.right)
                    parent_min = self.find_min_parent(new_node.key, parent.left.right)
                    if parent_min.left==None:
                        parent_min.left=parent.left.left
                        parent.left=parent_min
                    else:
                        new_node.left=parent.left.left
                        new_node.right=parent.left.right
                        parent.left=new_node
                        parent_min=self.find_min_parent(new_node.key,parent.left.right)
                        parent_min.left=None
            return True

    def delete_helper(self,key,node):
        if node.right!=None:
            if node.right.key==key:
                return (node)
        if node.left!=None:
            if node.left.key==key:
                return (node)
        if key>node.key:
            return self.delete_helper(key,node.right)
        if key<node.key:
            return self.delete_helper(key,node.left)

    def delete_find_min(self,node):
        while node.left!=None:
            node=node.left
        return node

    def find_min_parent(self,key,node):
        if node.left!=None:
            if node.left.key==key:
                return node
        if key==node.key:
            return node




    # def delete(self, key): # deletes node containing key
    #     # Will need to consider all cases
    #     # This is the most difficult method - save it for last, so that
    #     # if you cannot get it to work, you can still get credit for
    #     # the other methods
    #     # Returns True if the item was deleted, False otherwise
    #     node=self.root
    #     if self.search(key)==False:
    #         return False
    #     while node.key!=key:
    #         if node.right!=None:
    #             if node.right.key==key:
    #                 if node.right.right==None and node.right.left==None:
    #                     node.right=None
    #                     return True
    #                 break
    #         if node.left!=None:
    #             if node.left.key==key:
    #                 if node.left.left==None and node.left.right==None:
    #                     node.left=None
    #                     return True
    #                 break
    #         if key>node.key:
    #             node=node.right
    #         if key<node.key:
    #             node=node.left
    #     if node.right.key == key and (node.right.right !=None and node.right.left==None):
    #         node.right=node.right.right
    #         return True
    #     if node.right.key == key and (node.right.right==None and node.right.left != None):
    #         node.right=node.right.left
    #         return True
    #     if node.left.key == key and (node.left.right != None and node.left.left == None):
    #         node.left=node.left.right
    #         return True
    #     if node.left.key == key and (node.left.right == None and node.left.left != None):
    #         node.left=node.left.left
    #         return True
    #
    #     if node.right.key==key and (node.right.right != None and node.right.left != None):
    #         min_node=node.right.right
    #         while min_node.left!=None:
    #             min_node=min_node.left
    #         node.right=min_node
    #     if node.left.key==key and (node.left.right != None and node.left.left != None):
    #         min_node=node.left.right
    #         while min_node.left!=None:
    #             min_node=min_node.left
    #         node.left=min_node
    #     pass
    # def delete(self,key):# deletes node containing key
    #     # Will need to consider all cases
    #     # This is the most difficult method - save it for last, so that
    #     # if you cannot get it to work, you can still get credit for
    #     # the other methods
    #     # Returns True if the item was deleted, False otherwise
    #     node=self.root
    #     parent_node=self.root
    #     if self.search(key)==False:
    #         return False
    #     while key!=node.key:
    #         if key>node.key:
    #             node=node.right
    #         if key<node.key:
    #             node=node.left
    #     while key!=parent_node.key:
    #         if parent_node.right!=None or parent_node.left!=None:
    #             if parent_node.right.key==key or parent_node.left.key==key:
    #                 break
    #         if key>parent_node.key:
    #             parent_node=parent_node.right
    #         if key<parent_node.key:
    #             parent_node=parent_node.left
    #     if parent_node.right.key==node.key==key and node.right==node.left==None:
    #         parent_node.right=None
    #     elif parent_node.left.key==node.key==key and node.right==node.left==None:
    #         parent_node.left=None
    #
    #     elif node.key==key and node.right==None and node.left!=None:
    #         parent_node.right=node.left
    #     elif node.key==key and node.right!=None and node.left==None:
    #         parent_node.left=node.right
    #
    #     elif parent_node.right==node.key==key and node.right!=None and node.left!=None:
    #         node_min=node.right
    #         while node_min.left!=None:
    #             node_min=node_min.left
    #         parent_node.right=node_min
    #         node_min.left=node.left
    #         node_min.right=node.right
    #         self.delete(key)
    #
    #     elif parent_node.left==node.key==key and node.right!=None and node.left!=None:
    #         node_min=node.right
    #         while node_min.left!=None:
    #             node_min=node_min.left
    #         parent_node.left=node_min
    #         node_min.left=node.left
    #         node_min.right=node.right
    #         self.delete(key)
    #     return True



