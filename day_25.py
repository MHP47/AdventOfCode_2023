from utils import *
import networkx as nx


def part_1(p_Input):
    graph_mappings = {y: z.split() for y,z in [x.split(': ') for x in p_Input.strip().splitlines()]}
    graph = nx.DiGraph()
    for k,v in graph_mappings.items():
        for i in v:
            graph.add_edge(k, i, capacity = 1.0)
            graph.add_edge(i, k, capacity = 1.0)

    for node in graph_mappings:
        if node == k: continue
        cuts, (group1, group2) = nx.minimum_cut(graph, k, node)
        if cuts == 3:
            return len(group1) * len(group2)


example_input_1 = """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
"""
challenge_input = Input(25)

assert(part_1(example_input_1) == 54)
print(f"Part 1: {part_1(challenge_input)}")
