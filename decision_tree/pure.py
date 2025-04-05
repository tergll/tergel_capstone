%%manim -qm DataPointsInCircle
import random

class DataPointsInCircle(Scene):
    def construct(self):
        # Create boundary
        circle = Circle(radius=1, color=WHITE)
        self.play(Create(circle))

        # Generate points
        num_points = 10
        radius = 1
        red_points = VGroup()
        blue_points = VGroup()

        for _ in range(num_points):
            while True:
                x = random.uniform(-radius, radius)
                y = random.uniform(-radius, radius)
                if x**2 + y**2 <= radius**2:
                    break

            point_color = RED 
            dot = Dot(point=[x, y, 0], radius=0.1, color=point_color)
            if point_color == RED:
                red_points.add(dot)
            else:
                blue_points.add(dot)

        # Display points
        all_points = VGroup(red_points, blue_points)
        all_points.move_to(ORIGIN)
        self.play(FadeIn(red_points), FadeIn(blue_points))
        self.wait(2)
