%%manim -qm FeatureScaling

class FeatureScaling(Scene):
    def construct(self):
        # Create initial grid
        grid_points = VGroup()
        for col in range(7):
            for row in range(8):
                if col == 6 and row > 2:
                    continue
                point = Dot(radius=0.1)
                point.move_to(np.array([col - 3, row - 3.5, 0]))
                grid_points.add(point)

        grid_points.scale(0.8)
        grid_points.center()

        # Create reference point
        yellow_point = Dot(color=YELLOW, radius=0.15)
        yellow_point.move_to(ORIGIN)

        # Animate convergence
        self.play(Create(grid_points))
        self.play(FadeIn(yellow_point))
        converge_animations = [point.animate.move_to(yellow_point.get_center()) for point in grid_points]
        self.play(*converge_animations, run_time=2)

        # Recreate grid
        self.play(FadeOut(grid_points))
        recreated_grid = VGroup()
        for col in range(7):
            for row in range(8):
                if col == 6 and row > 2:
                    continue
                point = Dot(radius=0.1)
                point.move_to(np.array([col - 3, row - 3.5, 0]))
                recreated_grid.add(point)

        recreated_grid.scale(0.8).center()
        self.play(FadeIn(recreated_grid), run_time=1)

        # Fill missing positions
        empty_positions = [np.array([6 - 3, row - 3.5, 0]) for row in range(3, 8)]
        filling_points = VGroup()
        for pos in empty_positions:
            new_yellow_point = yellow_point.copy()
            filling_points.add(new_yellow_point)
            self.play(FadeIn(new_yellow_point), new_yellow_point.animate.move_to(pos), run_time=0.5)

        self.wait(3)
