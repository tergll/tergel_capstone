class LogisticRegressionCategorization(Scene):
    def construct(self):
        # Setup axes
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[0, 1, 0.2],
            x_length=8,
            y_length=4,
            axis_config={"include_numbers": True}
        )
        axes_labels = axes.get_axis_labels(
            x_label=Text("Өгөдөл (x)", font="Arial", font_size=24),
            y_label=Text("Магадлал", font="Arial", font_size=24)
        )
        self.play(Create(axes), Write(axes_labels))
        
        # Create sigmoid curve
        sigmoid_curve = axes.plot(
            lambda x: 1 / (1 + np.exp(-x)),
            x_range=[-6, 6],
            color=BLUE
        )
        self.play(Create(sigmoid_curve))
        
        # Add threshold line
        threshold_y = 0.5
        dotted_line = DashedLine(
            start=axes.c2p(-6, threshold_y),
            end=axes.c2p(6, threshold_y),
            color=RED,
            dash_length=0.2
        )
        threshold_label = Text("Зааг = 0.5", font="Arial", font_size=24, color=RED).next_to(dotted_line, RIGHT)
        self.play(Create(dotted_line), Write(threshold_label))
        
        # Add data points
        x_coords = [-4, -2, 0, 2, 4]
        points_data = [(x, 1 / (1 + np.exp(-x))) for x in x_coords]
        points = VGroup(*[Dot(axes.c2p(x, y), color=YELLOW) for x, y in points_data])
        self.play(Create(points))
        
        # Add classifications
        categories = VGroup()
        for x, y in points_data:
            if y >= 0.5:
                category = Text("Ангилал 1", font="Arial", font_size=20, color=GREEN).next_to(
                    axes.c2p(x, y), direction=UP + RIGHT, buff=0.3
                )
            else:
                category = Text("Ангилал 0", font="Arial", font_size=20, color=ORANGE).next_to(
                    axes.c2p(x, y), direction=UP + LEFT, buff=0.3
                )
            categories.add(category)
            self.play(Write(category))
        
        self.wait(3)
