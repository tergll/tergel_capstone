%%manim -qm ImpurityThresholdTreeScene

from manim import *

import numpy as np

class ImpurityThresholdTreeScene(Scene):
    def construct(self):
        # Tree nodes
        tree_root = Circle(radius=0.6, color=WHITE).shift(UP * 2.5)

        # Level 1
        l1_left = Circle(radius=0.6, color=WHITE).shift(UP * 1 + LEFT * 2)
        l1_right = Circle(radius=0.6, color=WHITE).shift(UP * 1 + RIGHT * 2)

        # Level 2 (leaf nodes)
        l2_ll = Circle(radius=0.6, color=WHITE).shift(DOWN * 0.5 + LEFT * 3)
        l2_lr = Circle(radius=0.6, color=WHITE).shift(DOWN * 0.5 + LEFT * 1)

        # Edges
        edges = VGroup(
            Line(tree_root.get_bottom(), l1_left.get_top()),
            Line(tree_root.get_bottom(), l1_right.get_top()),
            Line(l1_left.get_bottom(), l2_ll.get_top()),
            Line(l1_left.get_bottom(), l2_lr.get_top()),
        )

        # Data points only for leaf nodes
        l2_ll_data = VGroup()
        for i in range(4):
            angle = i * 2 * PI / 4
            radius = 0.3
            pos = radius * np.array([np.cos(angle), np.sin(angle), 0])
            dot = Dot(point=l2_ll.get_center() + pos, color=BLUE, radius=0.05)
            l2_ll_data.add(dot)

        l2_lr_data = VGroup()
        colors = [BLUE, RED]
        for i in range(2):
            angle = i * PI
            radius = 0.3
            pos = radius * np.array([np.cos(angle), np.sin(angle), 0])
            dot = Dot(point=l2_lr.get_center() + pos, color=colors[i], radius=0.05)
            l2_lr_data.add(dot)

        # --- Animate the tree structure ---
        self.play(Create(tree_root))
        self.play(Create(edges[0:2]))
        self.play(Create(l1_left), Create(l1_right))
        self.wait(0.5)

        self.play(Create(edges[2:]))
        self.play(Create(l2_ll), Create(l2_lr))
        self.wait(0.5)

        # Show only data in leaf nodes
        self.play(FadeIn(l2_ll_data), FadeIn(l2_lr_data))
        self.wait(1)

        # Highlight pure node (green)
        self.play(l2_ll.animate.set_stroke(color=GREEN, width=4))
        self.wait(0.5)

        # Highlight impure node (red)
        self.play(l2_lr.animate.set_stroke(color=RED, width=4))
        self.wait(0.5)
