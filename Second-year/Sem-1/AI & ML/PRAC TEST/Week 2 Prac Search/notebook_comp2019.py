import time
from inspect import getsource

import ipywidgets as widgets
import matplotlib.pyplot as plt
import networkx as nx
from IPython.display import HTML
from IPython.display import display
from matplotlib import lines

from search import GraphProblem, romania_map


# ______________________________________________________________________________
# Magic Words


def pseudocode(algorithm):
    """Print the pseudocode for the given algorithm."""
    from urllib.request import urlopen
    from IPython.display import Markdown

    algorithm = algorithm.replace(' ', '-')
    url = "https://raw.githubusercontent.com/aimacode/aima-pseudocode/master/md/{}.md".format(algorithm)
    f = urlopen(url)
    md = f.read().decode('utf-8')
    md = md.split('\n', 1)[-1].strip()
    md = '#' + md
    return Markdown(md)


def psource(*functions):
    """Print the source code for the given function(s)."""
    source_code = '\n\n'.join(getsource(fn) for fn in functions)
    try:
        from pygments.formatters import HtmlFormatter
        from pygments.lexers import PythonLexer
        from pygments import highlight

        #WM: using full=True messes with VSCode's cell rendering.
        #display(HTML(highlight(source_code, PythonLexer(), HtmlFormatter(full=True))))
        formatter = HtmlFormatter()
        display(HTML(f'<style>{ formatter.get_style_defs(".highlight") }</style>'))
        display(HTML(highlight(source_code, PythonLexer(), formatter)))

    except ImportError:
        print(source_code)



############################################################################################################

#####################           Functions to assist plotting in search.ipynb            ####################

############################################################################################################

def animate_search(graph_data, all_node_colors):
    """Display a visualisation of the map graph showing which nodes are visited, in frontier, explored.
    `graph_data` defined the map layout and appearance, and `all_node_colors` contains a list of
    dictionary objects, where each dictionary maps all nodes in the graph to their colors."""

    def slider_callback(iteration):
        # don't show graph for the first time running the cell calling this function
        try:
            show_map(graph_data, node_colors=all_node_colors[iteration])
        except:
            pass

    def visualize_callback(visualize):
        if visualize:
            button.value = False

            for i in range(slider.max + 1):
                slider.value = i
                # time.sleep(.5)

    slider = widgets.IntSlider(min=0, max=len(all_node_colors) - 1, step=1, value=0)
    slider_visual = widgets.interactive(slider_callback, iteration=slider)
    display(slider_visual)

    button = widgets.ToggleButton(value=False)
    button_visual = widgets.interactive(visualize_callback, visualize=button)
    display(button_visual)


class GraphSearchRecorder:
    """Records the nodes that are visited, added to the frontier, and expanded during search."""

    def __init__(self, graph_problem):
        self.problem = graph_problem
        self.reset()
    
    def reset(self):
        """Initialise all node colors to white, and clear the records"""
        self.node_colors = {k : 'white' for k in self.problem.graph.nodes()}
        self.all_node_colors = []
        self.visited_paths = []

    def visited(self, node):
        """Record the path do `node` and mark the node as currently being visited"""
        self.visited_paths.append((len(self.all_node_colors),node.solution()))
        self.node_colors[node.state] = "red"
        self.all_node_colors.append(dict(self.node_colors))
    
    def added_to_frontier(self, nodes):
        """Record that `nodes` were added to the frontier"""
        nodes = nodes if isinstance(nodes, list) else [nodes]
        for node in nodes:
            self.node_colors[node.state] = "orange"
        self.all_node_colors.append(dict(self.node_colors))

    def explored(self, node):
        """Record that `node` has been explored"""
        self.node_colors[node.state] = "grey"
        self.all_node_colors.append(dict(self.node_colors))        

    def goal_found(self, node, initial_node_colors=None, record_path=False):
        """Record that a path to goal `node` has been found."""
        if record_path:
            self.visited_paths.append((len(self.all_node_colors),node.solution()))
        self.node_colors[self.problem.initial] = "green"
        final_colors = final_path_colors(initial_node_colors or self.node_colors, self.problem, node.solution())
        self.all_node_colors.append(final_colors)

    def print_visited_paths(self):
        """Print the sequence of paths explored by the algorithm, 
        along with the iteration in the node color sequence where that
        is being explored. The node color sequence is more detailed as it
        distinguishes among the different events (visited, added, explored, goal) 
        that may occur while exploring one path. """

        print("Explored path at iterations:")
        for iteration, path in self.visited_paths:
            print(f"{iteration}: {'-'.join(path)}")

    def visualise_search_progress(self, graph_data):
        """Display a visualisation of the map graph showing which nodes are visited, in frontier, explored."""
        animate_search(graph_data, all_node_colors=self.all_node_colors)


def show_map(graph_data, node_colors=None, figsize=(18, 13)):
    G = nx.Graph(graph_data['graph_dict'])
    node_colors = node_colors or graph_data['node_colors']
    node_positions = graph_data['node_positions']
    node_label_pos = graph_data['node_label_positions']
    edge_weights = graph_data['edge_weights']

    # set the size of the plot
    plt.figure(figsize=figsize)
    # draw the graph (both nodes and edges) with locations from romania_locations
    nx.draw(G, pos={k: node_positions[k] for k in G.nodes()},
            node_color=[node_colors[node] for node in G.nodes()], linewidths=0.3, edgecolors='k')

    # draw labels for nodes
    node_label_handles = nx.draw_networkx_labels(G, pos=node_label_pos, font_size=14)

    # add a white bounding box behind the node labels
    [label.set_bbox(dict(facecolor='white', edgecolor='none')) for label in node_label_handles.values()]

    # add edge lables to the graph
    nx.draw_networkx_edge_labels(G, pos=node_positions, edge_labels=edge_weights, font_size=14)

    # add a legend
    white_circle = lines.Line2D([], [], color="white", marker='o', markersize=15, markerfacecolor="white")
    orange_circle = lines.Line2D([], [], color="orange", marker='o', markersize=15, markerfacecolor="orange")
    red_circle = lines.Line2D([], [], color="red", marker='o', markersize=15, markerfacecolor="red")
    gray_circle = lines.Line2D([], [], color="gray", marker='o', markersize=15, markerfacecolor="gray")
    green_circle = lines.Line2D([], [], color="green", marker='o', markersize=15, markerfacecolor="green")
    plt.legend((white_circle, orange_circle, red_circle, gray_circle, green_circle),
               ('Un-explored', 'Frontier', 'Currently Exploring', 'Explored', 'Final Solution'),
               numpoints=1, prop={'size': 16}, loc=(.8, .75))

    # show the plot. No need to use in notebooks. nx.draw will show the graph itself.
    plt.show()


# helper functions for visualisations

def final_path_colors(initial_node_colors, problem, solution):
    "Return a node_colors dict of the final path provided the problem and solution."

    # get initial node colors
    final_colors = dict(initial_node_colors)
    # color all the nodes in solution and starting node to green
    final_colors[problem.initial] = "green"
    for node in solution:
        final_colors[node] = "green"
    return final_colors