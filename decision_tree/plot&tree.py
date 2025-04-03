%%manim -qm DecisionTreeBoundaryVisualization
from manim import *
import numpy as np

class DecisionTreeBoundaryVisualization(Scene):
    def construct(self):
        # Generate the dataset
        np.random.seed(42)
        n = 50  # number of samples per class

        def make_cluster(x_center, y_center, label):
            x = np.random.normal(x_center, 0.1, n)
            y = np.random.normal(y_center, 0.1, n)
            points = np.column_stack((x, y))
            # Filter to stay within [0,1]
            points = [p for p in points if 0 <= p[0] <= 1 and 0 <= p[1] <= 1]
            return np.array(points), [label] * len(points)

        # Generate filtered data
        X_buuz, y_buuz = make_cluster(0.5, 0.2, "бууз")
        X_khuushuur, y_khuushuur = make_cluster(0.8, 0.9, "хуушуур")
        X_bansh, y_bansh = make_cluster(0.2, 0.1, "банш")

        X = np.vstack([X_buuz, X_khuushuur, X_bansh])
        y = np.array(y_buuz + y_khuushuur + y_bansh)

        # Axes setup
        axes = Axes(
            x_range=[0, 1, 0.2],
            y_range=[0, 1, 0.2],
            x_length=6,
            y_length=6,
            axis_config={"include_tip": False}
        ).to_edge(LEFT)

        x_label = Text("Хоолны хэмжээ", font_size=20).next_to(axes.x_axis, DOWN, buff=0.4)
        y_label = Text("Шаргал өнгө", font_size=20).next_to(axes.y_axis, LEFT, buff=0.4)

        # Dots
        dots = VGroup()
        for label in np.unique(y):
            label_str = str(label)
            color = {
                "бууз": BLUE,
                "хуушуур": ORANGE,
                "банш": GREEN
            }[label_str]
            subset = X[y == label]
            for point in subset:
                dot = Dot(axes.c2p(point[0], point[1]), color=color, radius=0.07)
                dot.set_stroke(BLACK, width=0.7)
                dots.add(dot)

        # Decision boundaries
        horizontal_line = DashedLine(
            axes.c2p(0, 0.55), axes.c2p(1, 0.55), color=YELLOW, stroke_width=3
        )
        vertical_line = DashedLine(
            axes.c2p(0.35, 0), axes.c2p(0.35, 0.55), color=GREEN, stroke_width=3
        )

        # Region fills
        khuushuur_area = Polygon(
            axes.c2p(0, 0.55), axes.c2p(1, 0.55), axes.c2p(1, 1), axes.c2p(0, 1),
            color=ORANGE, fill_opacity=0.3
        )
        bansh_area = Polygon(
            axes.c2p(0, 0), axes.c2p(0.35, 0), axes.c2p(0.35, 0.55), axes.c2p(0, 0.55),
            color=GREEN, fill_opacity=0.3
        )
        buuz_area = Polygon(
            axes.c2p(0.35, 0), axes.c2p(1, 0), axes.c2p(1, 0.55), axes.c2p(0.35, 0.55),
            color=BLUE, fill_opacity=0.3
        )

        # Region labels
        khuushuur_label = Text("хуушуур", color=ORANGE, font_size=20).move_to(axes.c2p(0.3, 0.8))
        bansh_label = Text("банш", color=GREEN, font_size=20).move_to(axes.c2p(0.2, 0.4))
        buuz_label = Text("бууз", color=BLUE, font_size=20).move_to(axes.c2p(0.8, 0.4))

        # Decision tree nodes
        q1 = Text("Шаргал хэмжээ ≤ 0.55 уу?", font_size=20)
        box1 = SurroundingRectangle(q1, color=BLUE)
        node1 = VGroup(box1, q1)

        leaf1 = Text("хуушуур", color=ORANGE, font_size=18)
        leaf1_box = SurroundingRectangle(leaf1, color=WHITE)
        leaf1_node = VGroup(leaf1_box, leaf1)

        q2 = Text("Хэмжээ ≤ 0.35 уу?", font_size=20)
        q2_box = SurroundingRectangle(q2, color=BLUE)
        node2 = VGroup(q2_box, q2)

        leaf2 = Text("банш", color=GREEN, font_size=18)
        leaf2_box = SurroundingRectangle(leaf2, color=WHITE)
        leaf2_node = VGroup(leaf2_box, leaf2)

        leaf3 = Text("бууз", color=BLUE, font_size=18)
        leaf3_box = SurroundingRectangle(leaf3, color=WHITE)
        leaf3_node = VGroup(leaf3_box, leaf3)

        # Tree layout: close child spacing
        node1.move_to(ORIGIN + RIGHT * 2 + UP * 2)
        leaf1_node.move_to(node1.get_bottom() + DOWN * 1.0 + RIGHT * 1.2)
        node2.move_to(node1.get_bottom() + DOWN * 1.0 + LEFT * 1.2)

        leaf2_node.move_to(node2.get_bottom() + DOWN * 1.0 + LEFT * 0.6)
        leaf3_node.move_to(node2.get_bottom() + DOWN * 1.0 + RIGHT * 0.6)


        # Connection lines
        line1 = Line(node1.get_bottom(), node2.get_top())
        line2 = Line(node1.get_bottom(), leaf1_node.get_top())
        line3 = Line(node2.get_bottom(), leaf2_node.get_top())
        line4 = Line(node2.get_bottom(), leaf3_node.get_top())

        tree_group = VGroup(
            node1, node2, leaf1_node, leaf2_node, leaf3_node,
            line1, line2, line3, line4
        ).scale(0.9)

        tree_group.next_to(axes, RIGHT, buff=1.0)

        # === Animation ===
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(FadeIn(dots))

        self.play(FadeIn(node1))
        self.wait()

        self.play(Create(horizontal_line))
        self.wait()

        self.play(Create(line2), FadeIn(leaf1_node), FadeIn(khuushuur_area), Write(khuushuur_label))
        self.wait()

        self.play(Create(line1), FadeIn(node2))
        self.wait()

        self.play(Create(vertical_line))
        self.wait()

        self.play(Create(line3), FadeIn(leaf2_node), FadeIn(bansh_area), Write(bansh_label))
        self.wait()

        self.play(Create(line4), FadeIn(leaf3_node), FadeIn(buuz_area), Write(buuz_label))
        self.wait()
