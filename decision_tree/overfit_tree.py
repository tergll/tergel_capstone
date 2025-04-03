%%manim -qm DecisionTreeOverfitting

from manim import *

class DecisionTreeOverfitting(Scene):
    def construct(self):
        # Title
        

        self.create_overfit_tree()
        self.wait(3)

    def create_overfit_tree(self):
        # === Create all nodes and structure ===
        nodes = VGroup()
        lines = VGroup()

        # Root
        q1 = Text("Шаргал хэмжээ ≤ 0.55 уу?", font_size=22)
        box1 = SurroundingRectangle(q1, color=WHITE)
        node1 = VGroup(box1, q1)
        node1.move_to(UP * 3)
        nodes.add(node1)

        # Level 2 splits
        q2 = Text("Хэмжээ ≤ 0.35 уу?", font_size=20)
        node2 = VGroup(SurroundingRectangle(q2, color=WHITE), q2).next_to(node1, DOWN + LEFT, buff=1)
        q3 = Text("Өнгө ≤ 0.8 уу?", font_size=20)
        node3 = VGroup(SurroundingRectangle(q3, color=WHITE), q3).next_to(node1, DOWN + RIGHT, buff=1)
        nodes.add(node2, node3)

        # Level 3 splits
        q4 = Text("Өнгө ≤ 0.2 уу?", font_size=18)
        node4 = VGroup(SurroundingRectangle(q4, color=WHITE), q4).next_to(node2, DOWN + LEFT, buff=0.8)

        q5 = Text("Зузаан ≤ 0.4 уу?", font_size=18)
        node5 = VGroup(SurroundingRectangle(q5, color=WHITE), q5).next_to(node2, DOWN + RIGHT, buff=0.8)

        q6 = Text("Зузаан ≤ 0.15 уу?", font_size=18)
        node6 = VGroup(SurroundingRectangle(q6, color=WHITE), q6).next_to(node3, DOWN + LEFT, buff=0.8)

        leaf1 = Text("хуушуур", font_size=18, color=ORANGE)
        leaf1_node = VGroup(SurroundingRectangle(leaf1, color=WHITE), leaf1).next_to(node3, DOWN + RIGHT, buff=0.8)

        nodes.add(node4, node5, node6, leaf1_node)

        # Level 4 leaf nodes (colored text only)
        def leaf(text, color, parent, direction):
            label = Text(text, font_size=16, color=color)
            box = SurroundingRectangle(label, color=WHITE)
            return VGroup(box, label).next_to(parent, direction, buff=0.6)

        leaf2_node = leaf("банш", GREEN, node4, DOWN + LEFT)
        leaf3_node = leaf("банш", GREEN, node4, DOWN + RIGHT)
        leaf4_node = leaf("бууз", BLUE, node5, DOWN + LEFT)
        leaf5_node = leaf("бууз", BLUE, node5, DOWN + RIGHT)
        leaf6_node = leaf("хуушуур", ORANGE, node6, DOWN + LEFT)
        leaf7_node = leaf("бууз", BLUE, node6, DOWN + RIGHT)

        leaf_nodes = VGroup(
            leaf2_node, leaf3_node,
            leaf4_node, leaf5_node,
            leaf6_node, leaf7_node
        )

        nodes.add(*leaf_nodes)

        # Connect with lines
        connections = [
            (node1, node2), (node1, node3),
            (node2, node4), (node2, node5),
            (node3, node6), (node3, leaf1_node),
            (node4, leaf2_node), (node4, leaf3_node),
            (node5, leaf4_node), (node5, leaf5_node),
            (node6, leaf6_node), (node6, leaf7_node)
        ]
        for parent, child in connections:
            line = Line(parent[0].get_bottom(), child[0].get_top(), color=WHITE)
            lines.add(line)

        # Group and scale entire tree
        tree = VGroup(nodes, lines).scale(0.8)
        tree.move_to(ORIGIN)

        # Animate
        self.play(Create(nodes))
        self.play(Create(lines))

       