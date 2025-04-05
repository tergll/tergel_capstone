%%manim -qm DeepDecisionTreeScene

from manim import *

class DeepDecisionTreeScene(Scene):
    def construct(self):
        # Setup parameters
        depth = 4
        node_radius = 0.25
        vertical_spacing = 1.5
        horizontal_spacing = 6

        node_levels = []
        edge_group = VGroup()

        # Create node function
        def create_node():
            return Circle(radius=node_radius, color=WHITE)

        # Generate nodes by level
        for level in range(depth):
            num_nodes = 2 ** level
            level_nodes = VGroup()

            for i in range(num_nodes):
                x = (i - (num_nodes - 1) / 2) * (horizontal_spacing / (2 ** (level)))
                y = 3 - level * vertical_spacing
                node = create_node()
                node.move_to([x, y, 0])
                level_nodes.add(node)

            node_levels.append(level_nodes)

        # Add connections
        for parent_level, child_level in zip(node_levels, node_levels[1:]):
            for i, parent in enumerate(parent_level):
                left_child = child_level[2 * i]
                right_child = child_level[2 * i + 1]

                edge_left = Line(parent.get_bottom(), left_child.get_top(), color=WHITE)
                edge_right = Line(parent.get_bottom(), right_child.get_top(), color=WHITE)
                edge_group.add(edge_left, edge_right)

        # Combine nodes
        all_nodes = VGroup(*[node for level in node_levels for node in level])

        self.play(Create(all_nodes))
        self.play(Create(edge_group))
        self.wait(2)
