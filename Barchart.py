from manim import *

class convergence(Scene):


    def six_dice(self):
        dice_face = RoundedRectangle(corner_radius=0.2, width=2, height=2, fill_color="#40E0D0", fill_opacity=1, stroke_color=WHITE, stroke_width=4)
        
        dot1 = Dot(point=[-0.5, 0.5, 0], color=BLACK).scale(2)
        dot2 = Dot(point=[0.5, 0.5, 0], color=BLACK).scale(2)
        dot3 = Dot(point=[0.5, -0.5, 0], color=BLACK).scale(2)
        dot4 = Dot(point=[-0.5, -0.5, 0], color=BLACK).scale(2)
        dot5 = Dot(point=[0.5, 0, 0], color=BLACK).scale(2)
        dot6 = Dot(point=[-0.5, 0, 0], color=BLACK).scale(2)
        dice_group = VGroup(dice_face, dot1, dot2,dot3,dot4,dot5,dot6)

        return dice_group
    
    
    def geometric_anim(self):        
        geometric = Text("Geometric Distribution", font_size=60, color="YELLOW")
        geometric.move_to(UP*2)
        line_1 = Text("1. Trials can either succeed or fail with a probability of p and 1-p respectively", font_size=30, color="#40E0D0")
        line_1.move_to(UP*1)

        self.play(Create(geometric))
        self.wait(3)
        self.play(Create(line_1))
        self.wait(9)

        txt = MathTex(r"\frac{1}{6}", color=GOLD)
        text = Text(text="Success", color=GREEN)
        dice = self.six_dice()
        txt.next_to(dice, DOWN)
        text.next_to(dice, UP*0.75)
        dice_group = VGroup(dice, txt, text)
        dice_group.move_to(DOWN*1.5 + LEFT*2)

        txt2 = MathTex(r"\frac{5}{6}", color=GOLD)
        text2 = Text(text="Failure", color=RED)
        dice2 = self.six_dice()
        txt2.next_to(dice2, DOWN)
        text2.next_to(dice2, UP*0.75)
        dice_group2 = VGroup(dice2, txt2, text2)
        dice_group2.move_to(DOWN*1.5 + RIGHT*2)
        bbox = SurroundingRectangle(dice2, color=RED, buff=0)
        cross1 = Line(start=bbox.get_corner(UL), end=bbox.get_corner(DR), color=RED)
        cross2 = Line(start=bbox.get_corner(UR), end=bbox.get_corner(DL), color=RED)
        red_cross = VGroup(bbox, cross1, cross2)

        self.play(Create(dice_group), Create(dice_group2), Create(red_cross))
        self.wait(7)  # Introduce a delay before fading out
        self.play(FadeOut(dice_group), FadeOut(dice_group2), FadeOut(red_cross))
        line_2 = Text("2. We stop the trials once we get a successful result", font_size = 30, color = "#40E0D0")
        self.play(Create(line_2))
        self.wait(3)
        line_3 = Text("What is the expected number of trials to get a successful result?", font_size = 35, color = YELLOW)
        line_3.move_to(DOWN*1.3)
        self.play(Create(line_3))
        self.wait(6)
        self.play(FadeOut(geometric), FadeOut(line_1), FadeOut(line_2), FadeOut(line_3))

    def construct(self):

        
        values_list = []
        name_list = []

        values_list.append(1/6)
        name_list.append("")

        for i in range(1,50):
            if i%5==4:
                name_list.append(i+1)
            else:
                name_list.append("")
            values_list.append(values_list[-1] + (5/6) ** i * 1/6 * (i+1))

        chart = BarChart(
            values = values_list,
            bar_names=name_list,
            bar_colors=["#40E0D0", YELLOW],
            bar_width = 1,
            y_range = [0,10,2]
        )
        chart.shift(UP)
        text = MathTex(r"E(x) = \sum_{n=1}^{\infty} \left(\frac{5}{6}\right)^{n-1} \times \frac{1}{6} \times n")
        text.to_edge(DOWN, buff = 1)
        self.play(DrawBorderThenFill(chart, run_time = 5), Create(text))
    
        point_on_y_axis = chart.y_axis.number_to_point(6)
        right_end_of_bars = chart.x_axis.number_to_point(50)
        right_end_of_bars[1] = point_on_y_axis[1]

        line = Line(point_on_y_axis, right_end_of_bars, color=YELLOW)
        self.play(Create(line))
        self.wait(7)
        
        self.play(FadeOut(text), FadeOut(line),FadeOut(chart))
        values_list2 = []
        name_list2 = []

        self.geometric_anim()

        values_list2.append(1/10)
        name_list2.append("")
        chart.set_opacity(1)
        for i in range(1,100):
            if i%5==4:
                name_list2.append(i+1)
            else:
                name_list2.append("")
            values_list2.append(values_list2[-1] + (9/10) ** i * 1/10 * (i+1))

        chart = BarChart(
            values = values_list2,
            bar_names=name_list2,
            bar_colors=["#40E0D0", YELLOW],
            bar_width = 1,
            y_range = [0,15,5]
        )
        chart.center()
        chart.shift(UP)
        text = MathTex(r"E(x) = \sum_{n=1}^{\infty} \left(\frac{9}{10}\right)^{n-1} \times \frac{1}{10} \times n")
        text.to_edge(DOWN, buff = 1)
        self.play(DrawBorderThenFill(chart, run_time = 5), Create(text))
        point_on_y_axis = chart.y_axis.number_to_point(10)
        right_end_of_bars = chart.x_axis.number_to_point(100)
        right_end_of_bars[1] = point_on_y_axis[1]

        line = Line(point_on_y_axis, right_end_of_bars, color=YELLOW)
        self.play(Create(line))
        self.wait(2)
        self.wait(12)
        self.play(FadeOut(chart), FadeOut(text), FadeOut(line))
        