# A RouteTrie will store our routes and their associated handlers
from typing import List

root_handler = 'root handler'
about_handler = 'about handler'
not_found_handler = 'not found handler'


class RouteTrieNode:
    def __init__(self, handler: str = not_found_handler):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = {}


class Router:
    def __init__(self, root_handler, not_found_handler):
    # Create a new RouteTrie for holding our routes
    # You could also add a handler for 404 page not found responses as well!
        self.root_node = RouteTrieNode(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
    # Add a handler for a path
    # You will need to split the path and pass the pass parts
    # as a list to the RouteTrie
        current_node = self.root_node
        parts = self._split_path(path)
        for part in parts:
            if part not in current_node.children:
                current_node.children[part] = RouteTrieNode()
            current_node = current_node.children[part]

        current_node.handler = handler


    def lookup(self, path: str) -> str:
    # lookup path (by parts) and return the associated handler
    # you can return None if it's not found or
    # return the "not found" handler if you added one
    # bonus points if a path works with and without a trailing slash
    # e.g. /about and /about/ both return the /about handler
        if type(path) is not str:
            print('Error: path must be a string.')
            return None

        parts = self._split_path(path)
        current_node = self.root_node

        for part in parts:
            if part not in current_node.children:
                return self.not_found_handler
            current_node = current_node.children[part]

        return current_node.handler


    def _split_path(self, path) -> List[str]:
        return list(filter(None, path.split('/')))


if __name__ == '__main__':
    # create the router and add a route
    router = Router(root_handler, not_found_handler)

    router.add_handler("/home/about", "about handler")  # add a route

    # some lookups with the expected output

    print('\n---------- Test 1 -----------')
    print("Pass" if router.lookup(None) is None else "Fail")
    print("Pass" if router.lookup('') == root_handler else "Fail")
    print("Pass" if router.lookup("/") == root_handler else "Fail")

    print('\n---------- Test 2 -----------')
    print("Pass" if router.lookup("/home") == not_found_handler else "Fail")
    print("Pass" if router.lookup("/home/about/me") == not_found_handler else "Fail")

    print('\n---------- Test 3 -----------')
    print("Pass" if router.lookup("/home/about") == about_handler else "Fail")
    print("Pass" if router.lookup("/home/about") == about_handler else "Fail")
