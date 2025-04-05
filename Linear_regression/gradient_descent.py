%%manim -qm StochasticGradientDescentVisualization
import random

class StochasticGradientDescentVisualization(Scene):
    def construct(self):
        # axes
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
        dots = [Dot(axes.c2p(x, y), color=YELLOW) for x, y in points]
        
        slope = 1.0
        intercept = 0.5
        line = axes.plot(lambda x: slope * x + intercept, color=BLUE)
        
        self.play(Create(line))
        self.play(*[Create(dot) for dot in dots])

        # Setup learning parameters
        learning_rate = 0.05
        num_iterations = 5

        # Perform SGD iterations
        for i in range(num_iterations):
            batch_points = random.sample(points, k=2)
            
            residual_lines = []
            residual_values = []
            total_gradient_slope = 0
            total_gradient_intercept = 0
            
            for x, y in batch_points:
                pred_y = slope * x + intercept
                residual_line = DashedLine(
                    start=axes.c2p(x, y),
                    end=axes.c2p(x, pred_y),
                    color=RED
                )
                residual_lines.append(residual_line)
                
                residual = y - pred_y
                residual_squared = residual ** 2
                residual_values.append(residual_squared)

                gradient_slope = -2 * x * residual
                gradient_intercept = -2 * residual
                
                total_gradient_slope += gradient_slope
                total_gradient_intercept += gradient_intercept

            # Show current iteration
            self.play(*[Create(res_line) for res_line in residual_lines])
            
            batch_mse = sum(residual_values) / len(batch_points)
            mse_text = MathTex(f"\\text{{Batch MSE}} = {round(batch_mse, 2)}")
            mse_text.to_edge(DOWN)
            self.play(Write(mse_text))
            
            # Update parameters
            slope -= learning_rate * (total_gradient_slope / len(batch_points))
            intercept -= learning_rate * (total_gradient_intercept / len(batch_points))
            
            new_line = axes.plot(lambda x: slope * x + intercept, color=BLUE)
            self.play(Transform(line, new_line), run_time=1)
            
            self.play(*[FadeOut(res_line) for res_line in residual_lines], FadeOut(mse_text))

        self.wait(3)
