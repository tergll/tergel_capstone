from manim import *

class CleanDecisionTreeOnly(Scene):
    def construct(self):
        # Create root node
        q1 = Text("Шаргал хэмжээ ≤ 0.55 уу?", font_size=28)
        box1 = SurroundingRectangle(q1, color=BLUE)
        node1 = VGroup(box1, q1)
        node1.move_to(UP * 2)
        self.play(Create(node1))

        # Create right branch
        leaf1 = Text("хуушуур", color=ORANGE, font_size=22)
        leaf1_box = SurroundingRectangle(leaf1, color=WHITE)
        leaf1_node = VGroup(leaf1_box, leaf1)
        leaf1_node.next_to(node1, DOWN + RIGHT, buff=1.5)

        self.play(Create(leaf1_node))

        # Create left branch
        q2 = Text("Хэмжээ ≤ 0.35 уу?", font_size=28)
        q2_box = SurroundingRectangle(q2, color=BLUE)
        node2 = VGroup(q2_box, q2)
        node2.scale(0.9)
        node2.next_to(node1, DOWN + LEFT, buff=1.5).shift(RIGHT * 3)
        self.play(Create(node2))

        # Create leaf nodes
        leaf2 = Text("банш", color=GREEN, font_size=22)
        leaf2_box = SurroundingRectangle(leaf2, color=WHITE)
        leaf2_node = VGroup(leaf2_box, leaf2)
        leaf2_node.next_to(node2, DOWN + LEFT, buff=1)

        leaf3 = Text("бууз", color=BLUE, font_size=22)
        leaf3_box = SurroundingRectangle(leaf3, color=WHITE)
        leaf3_node = VGroup(leaf3_box, leaf3)
        leaf3_node.next_to(node2, DOWN + RIGHT, buff=1)

        self.play(Create(leaf2_node), Create(leaf3_node))

        # Add connections
        lines = [
            Line(node1.get_bottom(), node2.get_top()),
            Line(node1.get_bottom(), leaf1_node.get_top()),
            Line(node2.get_bottom(), leaf2_node.get_top()),
            Line(node2.get_bottom(), leaf3_node.get_top())
        ]
        self.play(*[Create(line) for line in lines])
        self.wait(3)
