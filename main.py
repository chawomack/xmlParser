from xmlTree import read_file, print_tree, recursively_create_tree
import random

# randomly regenerates index contained in size of responses
def select_random_response(responses):
    return responses[random.randint(0, len(responses) - 1)]


def main():
    file = read_file('tree.xml')
    tree = recursively_create_tree('', file)
    print_tree(tree)

    # gets user input for for tree searches
    while True:
        event = input(r"Event ('quit' to exit) : ").lower()
        if event.lower() == 'quit':
            return False
        else:
            try:
                breadth = tree.breadth_search(event)
                depth = tree.depth_search(event)
                print("\tbreadth first = {} searches".format(breadth.get('searches')))
                print("\tdepth first = {} searches".format(depth.get('searches')))

                responses = tree.get_leaves_for_node(breadth.get('node'))
                print("\tresponse = {}".format(select_random_response(responses)))
            except (AttributeError, IndexError):
                print("\tThat event was not found :(")

main()

