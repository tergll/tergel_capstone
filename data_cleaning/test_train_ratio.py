%%manim -qm GreyToColoredPoints

class GreyToColoredPoints(Scene):
    def construct(self):
        # Create points with different colors
        def create_points(num_grey, num_blue, num_green):
            points = VGroup(
                *[Dot(color=GREY) for _ in range(num_grey)],
                *[Dot(color=BLUE) for _ in range(num_blue)],
                *[Dot(color=GREEN) for _ in range(num_green)]
            )
            points.arrange_in_grid(rows=2, buff=0.5)
            points.center()
            return points
        
        # Animate transitions
        initial_points = create_points(10, 0, 0)
        self.play(Create(initial_points))
        self.wait(1)

        blue_green_points = create_points(0, 8, 2)
        self.play(Transform(initial_points, blue_green_points))
        self.wait(1)

        final_points = create_points(0, 9, 1)
        self.play(Transform(initial_points, final_points))
        self.wait(1)

        self.play(FadeOut(initial_points))