from collections import deque
from stack import Stack

class TreeNode:

    # creates a Node with possible attributes of a parent, behavior, response, and children
    def __init__(self, value, response=None):
        self.behavior = value
        self.response = response
        self.parent = None
        self.children = []

    '''
    Only searches for behavior, returns dictionary containing node and number of searches.
    Appends node's children to queue, then removes first item in queue if it's not the desired item
    '''
    def breadth_search(self, behavior):
        queue = deque()
        queue.append(self)
        length = 1
        num_of_searches = 0
        while length > 0:
            num_of_searches += 1
            node = queue.popleft()
            length -= 1
            if node.behavior and node.behavior.lower() == behavior:
                queue.clear()
                return {'node': node, 'searches': num_of_searches}
            else:
                for child in node.children:
                    queue.append(child)
                    length += 1

    '''
    Only searches for behavior, returns dictionary containing node and number of searches.
    Pops node off stack, if node is not desired item then pushes its children on stack
    '''
    def depth_search(self, behavior):
        stack = Stack()
        stack.push(self)
        num_of_searches = 0
        while stack.length > 0:
            node = stack.pop()
            num_of_searches += 1
            if node.behavior and node.behavior.lower() == behavior:
                return {'node': node, 'searches': num_of_searches}
            else:
                for child in reversed(node.children):
                    stack.push(child)

    '''
    returns all possible leaves for a node.
    Appends all children of event/behavior to a queue, if the event has a response it gets added to a list of possible responses
    otherwise that node's children get appended to the queue
    '''
    def get_leaves_for_node(self, event):
        responses = []
        length = 0
        queue = deque()
        for child in event.children:
            queue.append(child)
        length += len(event.children)
        while length > 0:
            node = queue.popleft()
            length -= 1
            if node.response != None:
                responses.append(node.response)
            else:
                for child in node.children:
                    queue.append(child)
                    length += 1
        return responses


