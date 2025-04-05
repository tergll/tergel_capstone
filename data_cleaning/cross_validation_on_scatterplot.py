%%manim -qm LinearPattern
from manim import *

class LinearPattern(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-1, 11, 1],
            y_range=[-1, 11, 1],
            axis_config={"include_numbers": True},
        )
        self.play(Create(axes))

        # Define data points
        points = [
            (0, 0), (3, 1), (2, 2.1), (3, 5), (4, 4),
            (5, 5), (6, 8.1), (6, 7), (9, 8.3), (7, 9)
        ]

        # Plot points
        point_dots = VGroup()
        for x, y in points:
            dot = Dot(axes.coords_to_point(x, y), color=RED)
            point_dots.add(dot)
        
        self.play(Create(point_dots))

        # Animate point pairs
        pairs = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
        for i, j in pairs:
            self.play(
                point_dots[i].animate.set_color(YELLOW),
                point_dots[j].animate.set_color(YELLOW)
            )
            self.wait(0.5)

            self.play(
                point_dots[i].animate.set_color(RED),
                point_dots[j].animate.set_color(RED)
            )

        self.wait(2)
