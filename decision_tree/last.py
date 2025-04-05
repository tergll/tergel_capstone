%%manim -qm RealDecisionTreeSplitScene

from manim import *
import numpy as np
from sklearn.tree import DecisionTreeClassifier

class RealDecisionTreeSplitScene(Scene):
    def generate_data(self, seed=42, perturb=False):
        np.random.seed(seed)
        n = 50
        def make_cluster(xc, yc, label):
            x = np.random.normal(xc, 0.08, n)
            y = np.random.normal(yc, 0.08, n)
            return np.column_stack((x, y)), [label] * n

        X1, y1 = make_cluster(0.2, 0.2, 0)
        X2, y2 = make_cluster(0.5, 0.4, 1)
        X3, y3 = make_cluster(0.8, 0.75, 2)

        X = np.vstack([X1, X2, X3])
        y = np.array(y1 + y2 + y3)

        if perturb:
            count = int(0.05 * len(X))
            idx = np.random.choice(len(X), count, replace=False)
            X[idx] += np.random.normal(0, 0.15, size=X[idx].shape)

        return X, y

    def plot_boundaries(self, axes, clf, colors, resolution=100):
        x_vals = np.linspace(0, 1, resolution)
        y_vals = np.linspace(0, 1, resolution)

        patches = VGroup()

        for xi in range(len(x_vals)-1):
            for yi in range(len(y_vals)-1):
                x = (x_vals[xi] + x_vals[xi+1]) / 2
                y = (y_vals[yi] + y_vals[yi+1]) / 2
                pred = clf.predict([[x, y]])[0]
                poly = Polygon(
                    axes.c2p(x_vals[xi], y_vals[yi]),
                    axes.c2p(x_vals[xi+1], y_vals[yi]),
                    axes.c2p(x_vals[xi+1], y_vals[yi+1]),
                    axes.c2p(x_vals[xi], y_vals[yi+1]),
                    fill_color=colors[pred],
                    fill_opacity=0.3,
                    stroke_width=0
                )
                patches.add(poly)
        return patches

    def plot_data_points(self, axes, X, y, label_colors):
        dots = VGroup()
        for i, (x, y_val) in enumerate(zip(X, y)):
            if 0 <= x[0] <= 1 and 0 <= x[1] <= 1:
                dot = Dot(axes.c2p(x[0], x[1]), radius=0.05, color=label_colors[y_val])
                dots.add(dot)
        return dots

    def construct(self):
        label_colors = {
            0: "#58D68D",  # банш - green
            1: "#3498DB",  # бууз - blue
            2: "#F39C12"   # хуушуур - orange
        }

        titles = [
            "Original Dataset",
            "5% Perturbed Dataset #1",
            "5% Perturbed Dataset #2"
        ]
        seeds = [42, 43, 44]

        for i in range(3):
            X, y = self.generate_data(seed=seeds[i], perturb=(i > 0))

            clf = DecisionTreeClassifier(max_depth=3, random_state=0)
            clf.fit(X, y)

            axes = Axes(
                x_range=[0, 1, 0.2],
                y_range=[0, 1, 0.2],
                x_length=6,
                y_length=6,
                axis_config={"include_tip": False}
            ).to_edge(LEFT)

            x_label = Text("Хэмжээ", font_size=20).next_to(axes.x_axis, DOWN, buff=0.4)
            y_label = Text("Шаргал", font_size=20).next_to(axes.y_axis, LEFT, buff=0.4)

        
            title = Text(titles[i], font_size=28).to_edge(UP)

            class_regions = self.plot_boundaries(axes, clf, label_colors)

            points = self.plot_data_points(axes, X, y, label_colors)

            self.play(FadeIn(axes), Write(x_label), Write(y_label), Write(title))
            self.play(FadeIn(class_regions), FadeIn(points))
            self.wait(2)

            self.play(FadeOut(VGroup(axes, x_label, y_label, title, points, class_regions)))