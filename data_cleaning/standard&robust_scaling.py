%%manim -qm FeatureScaling

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, RobustScaler
from manim import *

class FeatureScaling(Scene):
    def construct(self):
        # Raw Data
        np.random.seed(42)
        age = np.random.randint(20, 70, 20)
        salary = np.random.randint(100000, 1000000, 20)
        raw_data = np.column_stack((age, salary))

        axes_left = Axes(
            x_range=[0, 100, 20], 
            y_range=[100000, 1000000, 200000], 
            axis_config={"include_numbers": True}
        ).scale(0.5).shift(LEFT * 3)

        axes_right = Axes(
            x_range=[0, 100, 20], 
            y_range=[100000, 1000000, 200000], 
            axis_config={"include_numbers": True}
        ).scale(0.5).shift(RIGHT * 3)

        self.play(Create(axes_left), Create(axes_right))

        # data points
        points_left = VGroup(*[
            Dot(axes_left.c2p(a, s), color=BLUE) for a, s in zip(age, salary)
        ])
        points_right = VGroup(*[
            Dot(axes_right.c2p(a, s), color=BLUE) for a, s in zip(age, salary)
        ])

        self.play(*[FadeIn(dot) for dot in points_left + points_right])

        # Standard Scaling 
        standard_scaler = StandardScaler()
        standard_scaled = standard_scaler.fit_transform(raw_data)

        # Robust Scaling 
        robust_scaler = RobustScaler()
        robust_scaled = robust_scaler.fit_transform(raw_data)

        # New axes for scaled data
        axes_left_scaled = Axes(
            x_range=[-2, 2, 1], 
            y_range=[-2, 2, 1], 
            axis_config={"include_numbers": True}
        ).scale(0.5).shift(LEFT * 3)

        axes_right_scaled = Axes(
            x_range=[-2, 2, 1],  
            y_range=[-2, 2, 1], 
            axis_config={"include_numbers": True}
        ).scale(0.5).shift(RIGHT * 3)

        self.play(
            Transform(axes_left, axes_left_scaled),
            Transform(axes_right, axes_right_scaled),
            *[dot.animate.move_to(axes_left_scaled.c2p(a, s)) for dot, (a, s) in zip(points_left, standard_scaled)],
            *[dot.animate.move_to(axes_right_scaled.c2p(a, s)) for dot, (a, s) in zip(points_right, robust_scaled)],
            run_time=2
        )

        self.wait(3)
