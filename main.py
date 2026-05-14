import networkx as nx
import pandas as pd

from src.astar import find_path
from src.csp import assign_potential
from src.minimax import run_battle
from src.trivia import ask_trivia_for_action, ask_trivia_for_move


def load_data():
    nodes = pd.read_csv("data/ust_selected_game_nodes.csv")
    edges = pd.read_csv("data/ust_building_edges.csv")

    return nodes, edges


def build_graph(edges_df):
    graph = nx.Graph()

    for _, row in edges_df.iterrows():
        graph.add_edge(row["from"], row["to"])

    return graph


def main():
    print("UST Eco Clash Starting...\n")

    # Load datasets
    nodes_df, edges_df = load_data()

    # Build graph
    graph = build_graph(edges_df)

    # Convert node dataframe into list
    buildings = list(nodes_df["building"])

    print("Buildings:")
    print(buildings)
    print()

    print("Edges:")
    print(list(graph.edges()))
    print()

    # CSP MODULE
    potential_map = assign_potential(buildings, list(graph.edges()), {})

    print("Potential Map:")
    print(potential_map)
    print()

    # A* MODULE
    path, cost = find_path(graph, buildings[0], buildings[1], potential_map, {}, None)

    print("Path:")
    print(path)

    print("Cost:")
    print(cost)
    print()

    # TRIVIA MOVE TEST
    move_modifier = ask_trivia_for_move()

    print("Move Modifier:")
    print(move_modifier)
    print()

    # TRIVIA ACTION TEST
    trivia_result = ask_trivia_for_action("solar_panel")

    print("Trivia Action Result:")
    print(trivia_result)
    print()

    # MINIMAX MODULE
    result = run_battle(
        building=buildings[1],
        potential=3,
        waste_start=2,
        importance=5,
        impact=4,
        trivia_callback=ask_trivia_for_action,
    )

    print("Battle Result:")
    print(result)


if __name__ == "__main__":
    main()
