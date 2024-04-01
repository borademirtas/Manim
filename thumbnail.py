from manim import *
from manim_data_structures import *

class Thumbnail(Scene):

    def one_dice(self):
        dice_face = RoundedRectangle(corner_radius=0.2, width=2, height=2, fill_color="#40E0D0", fill_opacity=1, stroke_color=WHITE, stroke_width=2)
        
        dot1 = Dot(point=[0, 0, 0], color=BLACK).scale(2)
        
        dice_group = VGroup(dice_face, dot1)
        
        return dice_group
    
    def two_dice(self):
        dice_face = RoundedRectangle(corner_radius=0.2, width=2, height=2, fill_color="#40E0D0", fill_opacity=1, stroke_color=WHITE, stroke_width=2)
        
        dot1 = Dot(point=[-0.5, 0.5, 0], color=BLACK).scale(2)
        dot2 = Dot(point=[0.5, -0.5, 0], color=BLACK).scale(2)

        dice_group = VGroup(dice_face, dot1, dot2)

        return dice_group
   
    def three_dice(self):
        dice_face = RoundedRectangle(corner_radius=0.2, width=2, height=2, fill_color="#40E0D0", fill_opacity=1, stroke_color=WHITE, stroke_width=2)
        
        dot1 = Dot(point=[-0.5, 0.5, 0], color=BLACK).scale(2)
        dot2 = Dot(point=[0, 0, 0], color=BLACK).scale(2)
        dot3 = Dot(point=[0.5, -0.5, 0], color=BLACK).scale(2)

        dice_group = VGroup(dice_face, dot1, dot2, dot3)

        return dice_group
    
    def four_dice(self):
        dice_face = RoundedRectangle(corner_radius=0.2, width=2, height=2, fill_color="#40E0D0", fill_opacity=1, stroke_color=WHITE, stroke_width=2)
        
        dot1 = Dot(point=[-0.5, 0.5, 0], color=BLACK).scale(2)
        dot2 = Dot(point=[0.5, 0.5, 0], color=BLACK).scale(2)
        dot3 = Dot(point=[0.5, -0.5, 0], color=BLACK).scale(2)
        dot4 = Dot(point=[-0.5, -0.5, 0], color=BLACK).scale(2)
        dice_group = VGroup(dice_face, dot1, dot2,dot3,dot4)

        return dice_group
    
    def five_dice(self):
        dice_face = RoundedRectangle(corner_radius=0.2, width=2, height=2, fill_color="#40E0D0", fill_opacity=1, stroke_color=WHITE, stroke_width=2)
        
        dot1 = Dot(point=[-0.5, 0.5, 0], color=BLACK).scale(2)
        dot2 = Dot(point=[0.5, 0.5, 0], color=BLACK).scale(2)
        dot3 = Dot(point=[0.5, -0.5, 0], color=BLACK).scale(2)
        dot4 = Dot(point=[-0.5, -0.5, 0], color=BLACK).scale(2)
        dot5 = Dot(point=[0, 0, 0], color=BLACK).scale(2)
        dice_group = VGroup(dice_face, dot1, dot2,dot3,dot4,dot5)

        return dice_group
    
    def six_dice(self):
        dice_face = RoundedRectangle(corner_radius=0.2, width=2, height=2, fill_color="#40E0D0", fill_opacity=1, stroke_color=WHITE, stroke_width=2)
        
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
        
    def construct(self):
        values_list = []
        name_list = []

        values_list.append(1/6)
        name_list.append("")

        for i in range(1, 12):
            if i % 5 == 4:
                name_list.append(i + 1)
            else:
                name_list.append("")
            values_list.append((5/6) ** i * 1/6)

        chart = BarChart(
            values=values_list,
            bar_names=name_list,
            bar_colors=["#40E0D0", YELLOW],
            bar_width=1,
            y_range=[0, 0.20, 0.04]
        )

        

        chart.width  = chart.width  / 2
        chart.to_edge(UP+LEFT)
        chart.shift(DOWN*0.5+LEFT*0.25)
        vertical_line = Line(UP * config.frame_height / 2, DOWN * config.frame_height / 2, color = GOLD)

        # Create a horizontal line from left to right
        horizontal_line = Line(LEFT * config.frame_width / 2, RIGHT * config.frame_width / 2, color = GOLD)

        # Add the lines to the scene
        self.add(vertical_line, horizontal_line)
        self.add(chart)


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

        arrow = CurvedArrow(all_dice.get_left()+LEFT*0.1, all_win.get_top()+UP*0.1, color = "#40E0D0")
        arrow_2 = CurvedArrow(all_dice.get_right()+RIGHT*0.1, fail_dice.get_top()+UP*0.1, angle=-PI/2, color = "#40E0D0")
        
        uright = VGroup(arrow, arrow_2, all_win, fail_dice, all_dice)
        uright.scale(0.4)
        uright.to_edge(UP+RIGHT)
        uright.shift(LEFT*1.2+DOWN*0.4)    
        self.add(uright)
        self.wait(0.5)


        my_list = [1, 0, 1, 0, 1, 0, 0, 1, 1]

        arr = MArray(
            self,
            hide_index=True,
            stroke_color = BLACK,
            fill_color = BLACK,
            color = BLACK
        )
        for c in my_list:
            if c == 0:
                arr.append_elem(
                    value=0,
                    mob_square_args={'fill_color': BLACK, 'color': WHITE},
                    mob_value_args={'color': "#40E0D0"},
                    play_anim=False, 
                    append_anim=GrowFromCenter
                )
            else:
                arr.append_elem(
                    value=1,
                    mob_square_args={'fill_color': "#40E0D0", 'color': WHITE},
                    mob_value_args={'color': BLACK},
                    play_anim=False,
                    append_anim=GrowFromCenter
                )
        pointer1 = MArrayPointer(self, arr, 2, '')
        pointer2 = MArrayPointer(self, arr, 5, '')

        
        arrg = VGroup(arr, pointer1, pointer2)
        arrg.scale(0.65)
        arrg.to_edge(DOWN+RIGHT)
        arrg.shift(UP*0.5)
        text = Text("Array Sorting", gradient=(["#40E0D0", YELLOW]), font_size=36)
        text.move_to(RIGHT*3.5+DOWN*0.5)
        self.add(text)
        txt = Text("Markov Chains", gradient=(["#40E0D0", YELLOW]), font_size=36)
        txt.move_to(LEFT*3.5+DOWN*0.5)
        self.add(txt)
        txt = Text("Geometric Distribution", gradient=(["#40E0D0", YELLOW]), font_size=36)
        txt.move_to(LEFT*3.5+UP*3.5)
        self.add(txt)
        txt = Text("Rolling Dice", gradient=(["#40E0D0", YELLOW]), font_size=36)
        txt.move_to(RIGHT*3.5+UP*3.5)
        self.add(txt)
        self.add(arrg)

        flip = VGroup(
            Circle(stroke_color=WHITE, stroke_width=4, fill_color=BLACK, fill_opacity=1),
            Text("Roll Again", font_size=30, color = WHITE)
        )
        flip.move_to(LEFT*2.5)

        win = VGroup(
            Circle(stroke_color=WHITE, stroke_width=4, fill_color=BLACK, fill_opacity=1),
            Text("End Game", font_size=30, color = WHITE)
        )
        win.move_to(RIGHT*2.5)

        uptxt = MathTex(r"\frac{5}{6}", color = YELLOW)
        uptxt.next_to(flip, UP), uptxt.shift(LEFT)



        arrow_down = CurvedArrow(flip.get_bottom()+DOWN*0.1, win.get_bottom(), color = "#40E0D0",stroke_width=5)
        arrow_up =  ArcBetweenPoints(flip.get_top()+RIGHT*0.1, flip.get_top()+UP+LEFT*0.05, stroke_color="#40E0D0", angle = PI/2,stroke_width=5) 
        arrow_up2 =  CurvedArrow(flip.get_top()+UP, flip.get_top()+LEFT*0.1, stroke_color="#40E0D0", angle = PI/2,stroke_width=5)  

        downtxt = MathTex(r"\frac{1}{6}", color = YELLOW)
        downtxt.next_to(arrow_down, DOWN)

        all = VGroup(arrow_up, arrow_up2, uptxt, arrow_down, downtxt, flip, win)
        all.scale(0.5)
        all.to_edge(DOWN+LEFT)
        all.shift(RIGHT*1.25+DOWN*0.25)
        self.add(all)

         