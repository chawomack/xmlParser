import re
from treeNode import TreeNode


# Matches a grouping with open caret followed by 0 or more of any character and looks ahead for closing caret
open_tag = '(<.*?>)'

# Looks for similar pattern as above but looks ahead for />
single_tag = '(<.*?/>)'

# Looks for pattern that matches '</' followed by one or more letters, followed by '>'
close_tag = '(</[a-z]+>)'

# Looks ahead for an ending caret followed by one or more whitespace character followed by opening caret
spaces_btw_tags = '(?<=>)\s+(?=<)'

# ignores all patterns that match a tag and matches one or more whitespace characters
spaces_btw_tags2 = '[^<(a-z)(0-9).>]\s+[^<(a-z)(0-9).>]'


def read_file(file_name):
    file = open(file_name).read().replace("\n", "")

    # these regex remove whitespace characters to prevent issues in recursion later on
    no_whitespace = re.sub(spaces_btw_tags, "", file)
    return re.sub(spaces_btw_tags2, "", no_whitespace)


'''
    Grabs first tag in file and creates a node from this tag, then depending on the type of tag
    it will make a recursive call with the current_node/parent_node and the rest of the file after
    this tag. Tags will be 'removed' from file one by one until only tag remains, which is the base case.
'''
def recursively_create_tree(current_node, file):
    # looks for pattern that would match first tag in file
    tag = re.search(open_tag, file).group()

    # gets everything inside the tag and ignores the carets
    tag_name = re.search('[^<](.*)[^>]', tag).group()

    # base case where only one tag remains in file
    if len(file) == len(tag):
        return current_node

    # creates root node because node has not been passed in
    elif (current_node == ''):
        return recursively_create_tree(TreeNode(tag_name), file[len(tag):len(file)])

    # if tag is a closing tag, sets current node to parent node and passes file without the closing tag
    elif re.match(close_tag, tag):
        current_node = current_node.parent
        return recursively_create_tree(current_node, file[len(tag):len(file)])

    # if tag is a single tag, appends it as child to current node
    elif tag[len(tag) - 2] == '/':
        response = re.search('response="(.*)[^/]', tag_name).group(1)
        new_node = TreeNode(None, response)
        current_node.children.append(new_node)
        return recursively_create_tree(current_node, file[len(tag):len(file)])

    # gets value of behavior from first tag and creates as a child node of the current node,
    # then calls functions with node created from behavior
    else:
        behavior = re.search('behavior="(.*)"[\s]', tag_name).group(1)
        new_node = TreeNode(behavior)
        new_node.parent = current_node
        current_node.children.append(new_node)
        return recursively_create_tree(new_node, file[len(tag):len(file)])

'''
    Recursively prints tree by printing child nodes,
    if another recursive call is made it increases the tab size for the new call
'''
def print_tree(node, tab=1):
    if node.behavior == 'root':
        print("behavior = ", node.behavior)

    # prints all children of node passed in
    for child in node.children:
        print("\t" * tab, end="")

        '''if child has behavior then it prints behavior and increases tab. It then passes this child in
        for a recursive call, it then decrements the tab value so that sibling does not have additional tab'''
        if child.behavior:
            print("behavior = ", child.behavior)
            tab += 1
            print_tree(child, tab)
            tab -= 1
        else:
            print("response = ", child.response)
