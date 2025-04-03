%%manim -qm MinimumSamplesTreeScene
class MinimumSamplesTreeScene(Scene):
    def construct(self):
        # Create a decision tree with nodes containing data points
        tree_root = Circle(radius=0.6, color=WHITE)
        tree_root.shift(UP * 2.5)
        
        # Level 1 nodes
        l1_left = Circle(radius=0.6, color=WHITE)
        l1_left.shift(UP * 1 + LEFT * 2)
        l1_right = Circle(radius=0.6, color=WHITE)
        l1_right.shift(UP * 1 + RIGHT * 2)
        
        # Level 2 nodes - focus on just two that don't qualify
        l2_ll = Circle(radius=0.6, color=RED, stroke_width=3)
        l2_ll.shift(DOWN * 0.5 + LEFT * 3)
        l2_lr = Circle(radius=0.6, color=RED, stroke_width=3)
        l2_lr.shift(DOWN * 0.5 + LEFT * 1)
        
        # Connect nodes with edges
        edges = VGroup(
            Line(tree_root.get_bottom(), l1_left.get_top()),
            Line(tree_root.get_bottom(), l1_right.get_top()),
            Line(l1_left.get_bottom(), l2_ll.get_top()),
            Line(l1_left.get_bottom(), l2_lr.get_top()),
        )
        
        # Create data points for the two unqualified leaf nodes
        l2_ll_data = VGroup()  # This will have only 3 samples (below min threshold)
        for i in range(3):
            angle = i * 2 * PI / 3
            radius = 0.3
            pos = radius * np.array([np.cos(angle), np.sin(angle), 0])
            dot = Dot(point=l2_ll.get_center() + pos, color=BLUE, radius=0.05)
            l2_ll_data.add(dot)
            
        l2_lr_data = VGroup()  # This will have only 2 samples (below min threshold)
        for i in range(2):
            angle = i * PI
            radius = 0.3
            pos = radius * np.array([np.cos(angle), np.sin(angle), 0])
            dot = Dot(point=l2_lr.get_center() + pos, color=BLUE, radius=0.05)
            l2_lr_data.add(dot)
        
        # Add tree structure
        self.play(Create(tree_root))
        self.wait(0.5)
        
        self.play(Create(edges[0:2]))
        self.play(
            Create(l1_left),
            Create(l1_right),
        )
        self.wait(0.5)
        
        self.play(Create(edges[2:]))
        self.play(
            Create(l2_ll),
            Create(l2_lr),
        )
        self.wait(0.5)
        
        # Add data points to the unqualified leaf nodes
        self.play(
            FadeIn(l2_ll_data),
            FadeIn(l2_lr_data),
        )
        self.wait(1)
        
        # Add counters to show sample counts
        l2_ll_counter = Integer(0).next_to(l2_ll, UP * 0.2)
        l2_ll_counter.scale(0.6)
        l2_lr_counter = Integer(0).next_to(l2_lr, UP * 0.2)
        l2_lr_counter.scale(0.6)
        
        self.play(
            FadeIn(l2_ll_counter),
            FadeIn(l2_lr_counter)
        )
        
        # Count samples in first node
        for i in range(1, 4):
            self.play(l2_ll_counter.animate.set_value(i), run_time=0.3)
        
        # Count samples in second node
        for i in range(1, 3):
            self.play(l2_lr_counter.animate.set_value(i), run_time=0.3)
        
        self.wait(0.5)
        
        
        
        self.wait(2)