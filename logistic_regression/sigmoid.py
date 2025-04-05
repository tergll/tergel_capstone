from manim import *
import numpy as np

class LogisticRegressionVisualization(Scene):
    def construct(self):
        # Create title
        title = Text("Logistic Regression Visualization", font_size=36, color=YELLOW)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # Setup axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 1.1, 0.1],
            x_length=10,
            y_length=5,
            tips=False,
            axis_config={"color": WHITE, "stroke_width": 2},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="P(y=1|x)")
        self.play(Create(axes), Write(axes_labels))
        
        # Create sigmoid curve
        logistic_curve = axes.plot(
            lambda x: 1 / (1 + np.exp(-x)),
            color=RED,
            stroke_width=3,
        )
        self.play(Create(logistic_curve))
        
        # Add reference point
        y_value = 0.6
        x_value = -np.log((1 / y_value) - 1)
        
        dot = Dot(axes.c2p(x_value, y_value), color=YELLOW)
        self.play(FadeIn(dot))
        
        # Add reference lines
        vertical_line = axes.get_vertical_line(axes.c2p(x_value, y_value), color=WHITE, stroke_width=2)
        horizontal_line = DashedLine(
            start=axes.c2p(x_value, y_value), 
            end=axes.c2p(x_value, 0), 
            color=WHITE, 
            dashed_ratio=0.5
        )
        self.play(Create(vertical_line), Create(horizontal_line))
        
        # Add labels
        annotation_text = MathTex(
            rf"P(y=1 \,|\, x={x_value:.2f})", 
            rf"\\ \sigma(x={x_value:.2f})={y_value:.2f}",
            font_size=30,
        ).next_to(dot, UP + RIGHT, buff=0.5)
        
        equation = MathTex(
            r"\sigma(1.00x) = \frac{1}{1 + e^{-1.00x}}",
            font_size=30,
        ).to_edge(DOWN, buff=0.5)
        
        self.play(Write(annotation_text))
        self.play(Write(equation))

        self.wait(2)
