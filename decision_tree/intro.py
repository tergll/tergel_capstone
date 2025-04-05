%%manim -qm MongolianFoodScatter

from manim import *
import numpy as np

class MongolianFoodScatter(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 1, 0.2],
            y_range=[0, 1, 0.2],
            x_length=6,
            y_length=6,
            axis_config={
                "include_tip": False,
                "include_ticks": True,
                "font_size": 20
            },
            x_axis_config={"numbers_to_include": [0, 0.5 ,1.0]},
            y_axis_config={"numbers_to_include": [0, 0.5, 1.0]},
        )

        axes.move_to(ORIGIN)

        x_label = Text("Хоолны хэмжээ", font_size=24)
        x_label.next_to(axes.x_axis, DOWN, buff=0.4)

        y_label = Text("Шаргал өнгө", font_size=24)
        y_label.next_to(axes.y_axis, LEFT, buff=0.4)

        self.play(Create(axes), Write(x_label), Write(y_label))

        # Data generation
        np.random.seed(42)
        n = 50

        def make_cluster(x_center, y_center):
            x = np.random.normal(x_center, 0.1, n)
            y = np.random.normal(y_center, 0.1, n)
            return np.column_stack((x, y))

        X_buuz = make_cluster(0.5, 0.2)
        X_khuushuur = make_cluster(0.8, 0.9)
        X_bansh = make_cluster(0.2, 0.1)

        label_colors = {
            "бууз": "#7FB3D5",
            "хуушуур": "#F5B041",
            "банш": "#D5DBDB"
        }

        # Plotting function
        def plot_points(points, color):
            dots = VGroup()
            for x, y in points:
                if 0 <= x <= 1 and 0 <= y <= 1:
                    dot = Dot(point=axes.c2p(x, y), radius=0.08, color=color)
                    dot.set_stroke(BLACK, width=0.7)
                    dots.add(dot)
            return dots

        buuz_dots = plot_points(X_buuz, label_colors["бууз"])
        khuushuur_dots = plot_points(X_khuushuur, label_colors["хуушуур"])
        bansh_dots = plot_points(X_bansh, label_colors["банш"])

        self.play(
            FadeIn(buuz_dots),
            FadeIn(khuushuur_dots),
            FadeIn(bansh_dots)
        )

        legend_items = VGroup()
        for label, color in label_colors.items():
            dot = Dot(color=color, radius=0.12)
            text = Text(label, font_size=22, color=color)
            entry = VGroup(dot, text).arrange(RIGHT, buff=0.3)
            legend_items.add(entry)

        legend_box = legend_items.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        legend_box.to_corner(UR, buff=0.7)

        legend_bg = SurroundingRectangle(legend_box, color=WHITE, buff=0.3)
        legend = VGroup(legend_bg, legend_box)

        self.play(FadeIn(legend))
        self.wait(2)
