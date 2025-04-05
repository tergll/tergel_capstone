from manim import *

class EntropySplitScene(Scene):
    def construct(self):
        # Create parent node
        parent_circle = Circle(radius=1.2, color=WHITE).move_to(UP * 2)
        self.play(Create(parent_circle))

        # Add data points
        data_points = VGroup()
        colors = [RED, RED, RED, BLUE, BLUE, BLUE]
        for i, color in enumerate(colors):
            angle = i * 2 * PI / len(colors)
            dot = Dot(radius=0.15, color=color)
            dot.move_to(parent_circle.get_center() + 0.9 * np.array([np.cos(angle), np.sin(angle), 0]))
            data_points.add(dot)

        self.play(FadeIn(data_points))
        self.wait(0.5)

        # Show entropy calculation
        entropy_text = Text("Entropy = 0.92", font_size=28, color=WHITE)
        entropy_text.next_to(parent_circle, DOWN, buff=0.5)
        self.play(Write(entropy_text))
        self.wait(1)

        # Create child nodes
        left_circle = Circle(radius=1.2, color=WHITE).move_to(LEFT * 3 + DOWN * 1.2)
        right_circle = Circle(radius=1.2, color=WHITE).move_to(RIGHT * 3 + DOWN * 1.2)
        self.play(Create(left_circle), Create(right_circle))

        # Split points into children
        for i in range(3):
            angle = i * 2 * PI / 3
            target = left_circle.get_center() + 0.7 * np.array([np.cos(angle), np.sin(angle), 0])
            self.play(data_points[i].animate.move_to(target), run_time=0.3)

        for i in range(3, 6):
            angle = (i - 3) * 2 * PI / 3
            target = right_circle.get_center() + 0.7 * np.array([np.cos(angle), np.sin(angle), 0])
            self.play(data_points[i].animate.move_to(target), run_time=0.3)

        self.wait(0.5)

        # Show child entropies
        left_entropy = Text("Entropy = 0", font_size=24, color=WHITE)
        right_entropy = Text("Entropy = 0", font_size=24, color=WHITE)
        left_entropy.next_to(left_circle, DOWN, buff=0.4)
        right_entropy.next_to(right_circle, DOWN, buff=0.4)
        self.play(Write(left_entropy), Write(right_entropy))
        self.wait(1)

        # Show weighted entropy
        weighted_result = MathTex(
            r"H = \frac{3}{6} \cdot 0 + \frac{3}{6} \cdot 0 = 0",
            font_size=34,
            color=WHITE
        )
        weighted_result.to_edge(DOWN).shift(UP * 1.5)


        self.play(Write(weighted_result))
        self.wait(1)

        # Show information gain
        ig_text = Text(" Мэдээллийн ашиг = 0.92 - 0 = 0.92", font_size=30, color=YELLOW)
        ig_text.next_to(weighted_result, DOWN*2.3, buff=0.5)
        self.play(Write(ig_text))
        self.wait(1.5)
