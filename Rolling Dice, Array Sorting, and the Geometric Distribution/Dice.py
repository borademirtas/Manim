from manim import *

class DiceRoll(Scene):

    def one_dice(self):
        dice_face = RoundedRectangle(corner_radius=0.2, width=2, height=2, fill_color="#40E0D0", fill_opacity=1, stroke_color=WHITE, stroke_width=4)
        
        dot1 = Dot(point=[0, 0, 0], color=BLACK).scale(2)
        
        dice_group = VGroup(dice_face, dot1)
        
        return dice_group
    
    def two_dice(self):
        dice_face = RoundedRectangle(corner_radius=0.2, width=2, height=2, fill_color="#40E0D0", fill_opacity=1, stroke_color=WHITE, stroke_width=4)
        
        dot1 = Dot(point=[-0.5, 0.5, 0], color=BLACK).scale(2)
        dot2 = Dot(point=[0.5, -0.5, 0], color=BLACK).scale(2)

        dice_group = VGroup(dice_face, dot1, dot2)

        return dice_group
   
    def three_dice(self):
        dice_face = RoundedRectangle(corner_radius=0.2, width=2, height=2, fill_color="#40E0D0", fill_opacity=1, stroke_color=WHITE, stroke_width=4)
        
        dot1 = Dot(point=[-0.5, 0.5, 0], color=BLACK).scale(2)
        dot2 = Dot(point=[0, 0, 0], color=BLACK).scale(2)
        dot3 = Dot(point=[0.5, -0.5, 0], color=BLACK).scale(2)

        dice_group = VGroup(dice_face, dot1, dot2, dot3)

        return dice_group
    
    def four_dice(self):
        dice_face = RoundedRectangle(corner_radius=0.2, width=2, height=2, fill_color="#40E0D0", fill_opacity=1, stroke_color=WHITE, stroke_width=4)
        
        dot1 = Dot(point=[-0.5, 0.5, 0], color=BLACK).scale(2)
        dot2 = Dot(point=[0.5, 0.5, 0], color=BLACK).scale(2)
        dot3 = Dot(point=[0.5, -0.5, 0], color=BLACK).scale(2)
        dot4 = Dot(point=[-0.5, -0.5, 0], color=BLACK).scale(2)
        dice_group = VGroup(dice_face, dot1, dot2,dot3,dot4)

        return dice_group
    
    def five_dice(self):
        dice_face = RoundedRectangle(corner_radius=0.2, width=2, height=2, fill_color="#40E0D0", fill_opacity=1, stroke_color=WHITE, stroke_width=4)
        
        dot1 = Dot(point=[-0.5, 0.5, 0], color=BLACK).scale(2)
        dot2 = Dot(point=[0.5, 0.5, 0], color=BLACK).scale(2)
        dot3 = Dot(point=[0.5, -0.5, 0], color=BLACK).scale(2)
        dot4 = Dot(point=[-0.5, -0.5, 0], color=BLACK).scale(2)
        dot5 = Dot(point=[0, 0, 0], color=BLACK).scale(2)
        dice_group = VGroup(dice_face, dot1, dot2,dot3,dot4,dot5)

        return dice_group
    
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


    def get_dice(self, val):

        if val == 1:
            return self.one_dice()
        elif val == 2:
            return self.two_dice()
        elif val == 3:
            return self.three_dice()
        elif val == 4:
            return self.four_dice()
        elif val == 5:
            return self.five_dice()
        else:
            return self.six_dice()

    def seq(self, rolls):
        line = Line(UP*4, DOWN*4, color = WHITE).to_corner(UL)
        line2 = Line(UP*4, DOWN*4, color = WHITE).next_to(line,RIGHT)
        line2.shift(RIGHT*1.5)
        line3 = Line(start=line.get_top() + DOWN*0.5, end=line2.get_top() + DOWN*0.5, color=WHITE)
        txt = Text(text = "  Turn \nHistory", color = YELLOW, font_size = 25)
        txt
        txt.next_to(line3.get_center(), UP, buff = 0.01)
        self.play(Create(line), Create(line2), Create(line3), Create(txt))

        last = self.one_dice()
        for i in range(len(rolls)):
            
            dice = self.get_dice(rolls[i])
            if rolls[i] == 6:
                self.play(GrowFromCenter(dice)) 
                box = SurroundingRectangle(dice, color=YELLOW, buff=MED_LARGE_BUFF, corner_radius=0.2,stroke_width=7)
                group = VGroup(dice,box)
                self.play(Create(box))
                self.play(Rotate(group,TAU))
                text = Text(text = "$" + str(len(rolls)) + " earned", color = "#2CC1A6").move_to(DOWN*2.5)
                self.play(Create(text))
                self.wait(1)
                
            elif i == 0:
                self.play(GrowFromCenter(dice))
                self.play(dice.animate.scale(0.5).next_to(line3, DOWN, buff = 0.1))
            else:
                 self.play(GrowFromCenter(dice))
                 self.play(dice.animate.scale(0.5 ).next_to(last, DOWN, buff=0.1)) 

            last = dice  

        self.clear()

    

    def construct(self):
        
        
        self.seq([3,5,2,1,4,3,6])
        self.seq([4,6])

        fail_list = []
        all_list = []
        for i in range(6):
            all_list.append(self.get_dice(i+1))
            all_list[i].scale(0.5)
            if i == 0:
                continue
            if i != 3:
                all_list[i].next_to(all_list[i-1], buff = 0)
                
            else:
                all_list[i].next_to(all_list[0], DOWN, buff = 0)
        tmp_all = VGroup(*all_list)
        bbox_all = SurroundingRectangle(tmp_all, buff=MED_SMALL_BUFF, color = YELLOW)
        all_dice = VGroup(tmp_all, bbox_all)
        all_dice.center()
        all_dice.move_to(UP*2)
        self.play(Create(all_dice, run_time = 3))   

        

        for i in range(5):
            fail_list.append(self.get_dice(i+1))
            fail_list[i].scale(0.5)
        fail_list[1].next_to(fail_list[0], buff = 0)
        fail_list[2].next_to(fail_list[1], buff = 0)
        fail_list[3].next_to(fail_list[0].get_right()+ DOWN+LEFT*0.5, buff = 0)
        fail_list[4].next_to(fail_list[3], buff = 0)
        tmp_fail = VGroup(*fail_list)
        bbox_fail = SurroundingRectangle(tmp_fail, buff=MED_SMALL_BUFF, color = YELLOW)
        txt_fail = Text("Failure", color="#40E0D0").next_to(bbox_fail, DOWN * 0.3)
        fail_dice = VGroup(tmp_fail, bbox_fail, txt_fail)
        fail_dice.center()
        fail_dice.move_to(DOWN*2+RIGHT*3)

        dice_win = self.get_dice(6)
        dice_win.scale(0.5)
        bboxw = SurroundingRectangle(tmp_fail, buff=MED_SMALL_BUFF, color = YELLOW)
        bboxw.move_to(dice_win.get_center())
        txtw = Text("Success", color="#40E0D0").next_to(bboxw, DOWN * 0.3)
        all_win = VGroup(dice_win, bboxw, txtw)
        all_win.center()
        all_win.move_to(DOWN*2+LEFT*3)
        self.play(Create(all_win, run_time = 3), Create(fail_dice, run_time = 3))

        arrow = CurvedArrow(all_dice.get_left()+LEFT*0.1, all_win.get_top()+UP*0.1, color = "#40E0D0")
        arrow_2 = CurvedArrow(all_dice.get_right()+RIGHT*0.1, fail_dice.get_top()+UP*0.1, angle=-PI/2, color = "#40E0D0")
        self.play(Create(arrow), Create(arrow_2))
        self.wait(11)
        self.play(FadeOut(arrow), FadeOut(arrow_2), FadeOut(fail_dice), FadeOut(all_win), FadeOut(all_dice))
        self.wait(0.5)

