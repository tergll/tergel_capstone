from manim import *
class MeanSquaredErrorVisualization(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1, 6, 1],
            y_range=[-1, 8, 1],
            x_length=7,
            y_length=5,
            axis_config={"color": GREY},
            tips=False,
        )
        self.play(Create(axes))
        
        # Create initial data
        points = [(-0.5, 1), (1, 2), (2, 4), (3, 5), (4, 7)]
        line = axes.plot(lambda x: 1.5 * x + 1, color=BLUE)

        self.play(Create(line))
        dots = [Dot(axes.c2p(x, y), color=YELLOW) for x, y in points]
        self.play(*[Create(dot) for dot in dots])
        
        # Calculate and show residuals
        residual_lines = []
        residual_values = []
        for x, y in points:
            pred_y = 1.5 * x + 1
            residual_line = DashedLine(
                start=axes.c2p(x, y),
                end=axes.c2p(x, pred_y),
                color=RED
            )
            residual_lines.append(residual_line)
            residual_values.append((y - pred_y) ** 2)
            
        self.play(*[Create(res_line) for res_line in residual_lines])

        # Display MSE calculation
        residual_squares = [MathTex(f"({round(res, 2)})^2") for res in residual_values]
        total_mse = MathTex("MSE = \\frac{1}{N} \\sum (y - \\hat{y})^2 = ", str(round(sum(residual_values) / len(points), 2)))

        for i, (x, y) in enumerate(points):
            residual_squares[i].next_to(dots[i], UP)
            self.play(Write(residual_squares[i]))

        total_mse.to_edge(DOWN)
        self.play(Write(total_mse))

        self.wait(3)
