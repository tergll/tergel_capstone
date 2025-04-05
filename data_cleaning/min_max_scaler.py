%%manim -qm FeatureScaling

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from manim import *

class FeatureScaling(Scene):
    def construct(self):
        # Create first set of axes
        axes1 = Axes(
            x_range=[0, 100, 20], 
            y_range=[100000, 1000000, 200000], 
            axis_config={"include_numbers": True}
        ).scale(0.5).shift(LEFT * 2.7)

        self.play(Create(axes1))
        
        # Generate and plot raw data
        np.random.seed(42)
        age = np.random.randint(20, 70, 20)
        salary = np.random.randint(100000, 1000000, 20)

        points1 = VGroup(*[
            Dot(axes1.c2p(a, s), color=BLUE) for a, s in zip(age, salary)
        ])
        self.play(*[FadeIn(dot) for dot in points1])

        # Create second set of axes
        axes2 = Axes(
            x_range=[0, 1, 0.2], 
            y_range=[0, 1, 0.2], 
            axis_config={"include_numbers": True}
        ).scale(0.5).shift(RIGHT * 3.7)

        self.play(Create(axes2))

        # Scale and transform data
        scaler = MinMaxScaler()
        scaled_data = scaler.fit_transform(np.column_stack((age, salary)))

        points2 = VGroup(*[
            Dot(axes2.c2p(a, s), color=RED) for a, s in scaled_data
        ])
        
        self.play(*[dot.animate.move_to(axes2.c2p(a, s)) for dot, (a, s) in zip(points1, scaled_data)], run_time=2)

        self.wait(3)
