from manim import *

class Markov(Scene):


    def replay(self, arrow):
        self.play(FadeOut(arrow))
        self.play(Create(arrow))

    def win(self):
        dice_face = RoundedRectangle(corner_radius=0.2, width=2, height=2, fill_color="#40E0D0", fill_opacity=1, stroke_color=WHITE, stroke_width=4)
        
        dot1 = Dot(point=[-0.5, 0.5, 0], color=BLACK).scale(2)
        dot2 = Dot(point=[0.5, 0.5, 0], color=BLACK).scale(2)
        dot3 = Dot(point=[0.5, -0.5, 0], color=BLACK).scale(2)
        dot4 = Dot(point=[-0.5, -0.5, 0], color=BLACK).scale(2)
        dot5 = Dot(point=[0.5, 0, 0], color=BLACK).scale(2)
        dot6 = Dot(point=[-0.5, 0, 0], color=BLACK).scale(2)
        dice_group = VGroup(dice_face, dot1, dot2,dot3,dot4,dot5,dot6)
        dice_group.scale(0.5)
        return dice_group

    def fail(self):
        dice = self.win()
        bbox = SurroundingRectangle(dice, color=RED, buff=0)
        cross1 = Line(start=bbox.get_corner(UL), end=bbox.get_corner(DR), color=RED)
        cross2 = Line(start=bbox.get_corner(UR), end=bbox.get_corner(DL), color=RED)
        red_cross = VGroup(bbox, cross1, cross2)
        good_dice = VGroup(dice, red_cross)
        return good_dice


    def show(self,arrows_up, arrows_down,cnt):
        fail_objects = [self.fail() for _ in range(cnt-1)]
        win_object = self.win()
        for i, fail_object in enumerate(fail_objects):
            if i == 0:
                fail_object.to_edge(UP, buff = 1)  # First fail object at the top
                fail_object.shift(LEFT*((cnt-1)/2+(cnt-1)*0.1))
                self.replay(arrows_up)
            else:
                fail_object.next_to(fail_objects[i-1], RIGHT, buff = 0.1)
                self.replay(arrows_up)
            self.play(Create(fail_object))
            self.wait(0.5)

        
        win_object.next_to(fail_objects[-1], RIGHT, buff = 0.1)
        self.replay(arrows_down)
        self.play(Create(win_object))
        self.wait(0.5)
        alldice = VGroup(*fail_objects, win_object)
        self.play(FadeOut(alldice))
        self.wait(1)
        
        
          
        


    def construct(self):
        

        flip = VGroup(
            Circle(stroke_color=WHITE, stroke_width=8, fill_color=BLACK, fill_opacity=1),
            Text("Roll Again", font_size=30, color = WHITE)
        )
        flip.move_to(LEFT*2.5)

        win = VGroup(
            Circle(stroke_color=WHITE, stroke_width=8, fill_color=BLACK, fill_opacity=1),
            Text("End Game", font_size=30, color = WHITE)
        )
        win.move_to(RIGHT*2.5)

        uptxt = MathTex(r"\frac{5}{6}", color = YELLOW)
        uptxt.next_to(flip, UP), uptxt.shift(LEFT)



        self.play(GrowFromCenter(flip), GrowFromCenter(win))
        arrow_down = CurvedArrow(flip.get_bottom()+DOWN*0.1, win.get_bottom(), color = "#40E0D0",stroke_width=10)
        arrow_up =  ArcBetweenPoints(flip.get_top()+RIGHT*0.1, flip.get_top()+UP+LEFT*0.05, stroke_color="#40E0D0", angle = PI/2,stroke_width=10) 
        arrow_up2 =  CurvedArrow(flip.get_top()+UP, flip.get_top()+LEFT*0.1, stroke_color="#40E0D0", angle = PI/2,stroke_width=10)  

        downtxt = MathTex(r"\frac{1}{6}", color = YELLOW)
        downtxt.next_to(arrow_down, DOWN)

        arrows_up = VGroup(arrow_up, arrow_up2, uptxt)
        arrows_down = VGroup(arrow_down, downtxt)

        
       

        self.play(Create(arrows_up), Create(arrows_down))
        self.wait(9)
        self.show(arrows_up, arrows_down,2)
        self.show(arrows_up, arrows_down,3)
        
        expr1 = MathTex("E(n)")
        expr2 = MathTex("E(n) = \\left(\\frac{5}{6}\\right)^{n-1}")
        expr3 = MathTex("E(n) = \\left(\\frac{5}{6}\\right)^{n-1} \\times \\frac{1}{6}")
        expr4 = MathTex("E(n) = \\left(\\frac{5}{6}\\right)^{n-1} \\times \\frac{1}{6} \\times n")
        text = MathTex(r"E(x) = \sum_{n=1}^{\infty} \left(\frac{5}{6}\right)^{n-1} \times \frac{1}{6} \times n")
        text.scale(1.5)
        expr1.move_to(UP*3)
        expr2.move_to(UP*3)
        expr3.move_to(UP*3)
        expr4.move_to(UP*3)
        self.wait(1)
        self.play(Write(expr1))
        self.wait(6)
        self.play(Transform(expr1, expr2))
        self.wait(12)
        self.play(Transform(expr1, expr3))
        self.wait(6.5)
        self.play(Transform(expr1, expr4))
        self.wait(6)
        self.play(FadeOut(flip), FadeOut(win), FadeOut(arrows_up), FadeOut(arrows_down), FadeOut(uptxt), FadeOut(downtxt))
        self.play(Transform(expr1, text))
        self.wait(17)
        self.play(FadeOut(expr1, run_time = 1.5))


        