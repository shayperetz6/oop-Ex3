
# Ex3 - Graph and GUI

in this project we will build a Graph object to run algorithms on
and creating a GUI to intract with the Graph , running some algorithms
usinig python.
## Authors

- [@oa1321](https://www.github.com/oa1321) 213101637
- [@shayperetz6](https://github.com/shayperetz6) 203464870


## The Problem Space
we have a few problems to solve in our case, most of the problems are conneted to the
algorithms part(what to use and how to code them) and some of them are related to the objects
we need to build like the nodes or the graph , what fiealds each object will contain
,ehat data strucure we shood use and extra...
## The Algorithmems

before the object implamantsion we we need to decide which Algorithmems to use
in the Algorithmems part the assigment.

the shrtest path problem - https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm 
we used dijkstra Algorithmem with hashmaps to solve the problem.

find the center - to find the center we used floyd warshel Algorithmem for all pairs shortest path

tsp-using floyd warshal all pairs shortest path to find shortest path, more on the Algorithmem will be in the wiki and algo part of readme




## Classes 
### the classes are gived to us by the api we implament like this 
the given class in the api were implamented by Digraph and GraphAlgo,

Digraph datastructure was implamented by saving the nodes and edges
in a dict with node_id as a key and a value of anarray of three elements
first is the node data the second is a dict of all out edges(id as akey and wight as a value) the thired is a dict of all in edges 

GraphAlgo implaments GraphAlgoInterface

GraphGui is the class of the GUI appliction , we used tkinter for the gui

Node is class to save node data in 

### fields and methods of each class

#### Node - a node in a graph:
    fields:
    x = x position in the plane
    y = y position in the plane
    z = z position in the plane
    ID = the node id 
    out_num = the amount of the edges that comes out of the node
    in_num = the amount of the edges that comes in to the node
    tag = a tag for the node
    tag2 = anouter tag for the node
    prev = anouter tag for the node(saved the save the prev node in some algo)
    method:
    __init__ - gets x,y,z value and an id
    __repr__ - retunrs a stting reprsnting the graph 

#### Digraph - a graph:

    fields:
    v_num = number of nodes
    e_num = number of edges
    graph = the datastrucer of the graph {id: [Node, out_dict{}, in_dict{}]}
    mc = the amount of modifications in the graph
    methods:
    __init__ - gets nothing just "building" the graph
    v_size() - returns the amount of nodes
    e_size() - returns the amount of edges
    get_all_v() - returns a dict of all noeds in the graph, id -> Node data
    all_in_edges_of_node(int n) - returns a dict of all the out edges of node(n)
    all_in_edges_of_node(int n) - returns a dict of all the in edges of node(n)
    get_mc() - returns the mc count of the graph
    add_node(id, (x,y,z)) - add a node with the id given and a pos of (x,y,z) returns False if succed in adding , True aouterwise
    remove_node(id) - removes the  node with the id given and returns True if succed or akse returns False
    add_edge(id1 , id2 , w) - add an edge with wighet w between node id1 to node id2
    remove_edge(id1, id2) - remove the edge from node id1 to node id2

#### GraphAlgo - graph algo class:
    fields:
    my_graph = the graph to run algo on
    methods:
    __init__ - get a graph to work on
    get_graph() - retruns the graph
    load_from_json(json_name) - loads a graph from json file given
    save_to_json(json_name) - saves a graph to json file given
    shortest_path(id1, id1) - calc the shortest path from node id1 to node id2 ans returns the path and dist
    TSP(list of id's) - calc the shortest path that goes by every node and returns dist and path
    center() - retruns the center of a graph and returns the max path and id of the node
    set_tag(data) - set all tag 1 of nodes to data
    set_tag(data) - set all tag 2 of nodes to data
    set_prev()- set all nodes prev to them self
    plot_graph() - create a plane gui and calls to GraphGui to show the things we need on that,

### also we have the GUI class

#### GraphGui:
    fields:
    my_graph = a graph to show
    methods:
    __init__ - draw the gui stuff 
    foucus1 and foucus2 = listns to an entery they were bind to and waits for an [enter] key to be
    pressed to do something
    run_sp() - run shortest path from the data given in the entery of sp
    run_tsp() - run tsp from the data given in the entery of tsp
    colored_lines(list of id's) - drawing colored lines and nodes from the nodes given and there edges
    show_graph() - shows the graph on the canvas 
    
## GUI

### About
we used tkinter for the GUI 
### How to download 

download the github repostery and folow the how to use instructions.

### How to use 
create an graphalgo instance and call plot graph OR create a GraphGUi instance and give it a graph 

note to yourself that if any promblem were occured in the gui(in the runnig algorithms part) you will see
a message box appaer with the data of the error

also the answrs will be givin via a messagebox (the paths data and id's fot an example) and then will be shown on the screen 
#### algorithms 

to run algorithms on the graph first choose wich algorithms you want after you choosed one folow his instructions - 

shortest path-

1.enter in the shortest path entery the two id's you want to check shood be int,int
1.1. if an error occured a messagebox will be shown with the promblem

2.press enter 

3.to clear press the reset button

tsp-

1.enter in the tsp entery the id's you want to check shood be int,int,int,.....
1.1. if an error occured a messagebox will be shown with the promblem

2.press enter 

3.to clear press the reset button
## Tests
cpu - amd ryzen 5000 seris with built-in amd gpu

100 nodes-

    shortest path -  0.0037876999999999997 sec
    center - 0.15819149999999998 sec
    tsp - 0.2513229 sec

1000 nodes-

    shortest path - 0.13388509999999998 sec
    center -  160.54462949999999
    tsp - 213.672673 sec

5000 nodes - 
    shortest path - 2.9019657 sec
    center - a lot
    tsp - a lot
10000 nodes-

    shortest path - 11.3092824 sec
    center - a lot
    tsp - a lot
50000 nodes-

    shortest path - 416.26432090000003 sec
    center - a lot
    tsp - a lot
100000 nodes-

    shortest path - 1302.45940003 sec
    center - a lot
    tsp - a lot
1000000 nodes-

    shortest path - a lot 
    center - a lot
    tsp - a lot

shortest path graph - look at sp.png

center graph -  look at center.png


