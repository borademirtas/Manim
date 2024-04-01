from manim import *

from manim_data_structures import *

GOOD_RED = "#D74D4D"
incomplete_list = [1, 0, 1, 1, 1, 0, 0, 0, 1]
incomplete_list2 = [1, 0, 1, 1, 1, 0, 0, 0, 1]
solved_list = [0, 0, 0, 0, 1, 1, 1, 1, 1]

class Solution(Scene):
    
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
    
    def updater(self, arr, idx, idx2,t=2):  

        pointer1 = MArrayPointer(self, arr, idx, '')
        pointer2 = MArrayPointer(self, arr, idx2, '')

        value_1 = incomplete_list[idx]
        value_2 = incomplete_list[idx2]
        
        if value_1 <= value_2:
            
            upper_text = Text(
                text = "Cannot Swap",
                color = GOOD_RED
                
            ).move_to(UP*2.25)
            self.play(
                Create(pointer1),
                Create(pointer2)
            )
            self.wait(0.25)
            self.play(
                
                Write(upper_text)
            )
            self.wait(0.25)
            self.play(
            FadeOut(upper_text, run_time = t),
            FadeOut(pointer1),
            FadeOut(pointer2)
            )   
    
            self.wait(2)
            return
        
        color_1 = BLACK
        color_2 = "#40E0D0"

        if value_1 == 0:
            color_1,color_2 = color_2,color_1

        incomplete_list[idx] = incomplete_list[idx]^1
        incomplete_list[idx2] = incomplete_list[idx2]^1

        text = Text(text= "Swap ("  + str(idx+1) + "," +str(idx2+1) + ")",  font_size = 40).move_to(UP*1.25)
        text.move_to(UP*2.25)
        self.play( Create(pointer1),Create(pointer2))   
        self.wait(0.5)
        self.play(Write(text), run_time = 2)
        self.play(
            arr.animate_elem_square(idx).set_fill(color_1),
            arr.animate_elem_square(idx2).set_fill(color_2)
        )
        arr.update_elem_value(index=idx, value=value_2, play_anim=False)
        arr.update_elem_value(index=idx2, value=value_1, play_anim=False)
        
        self.play(
            arr.animate_elem_value(idx).set_fill(color_2),
            arr.animate_elem_value(idx2).set_fill(color_1)
        )

        self.play(
            FadeOut(text),
            FadeOut(pointer1),
            FadeOut(pointer2)
        )

    def construct(self):
        
        
        
        incomplete = MArray(
            self,
            hide_index=True,
        )
        incomplete2 = MArray(
            self,
            hide_index=True,
        )
        solved = MArray(
            self,
            hide_index=True,
        )


        for c in incomplete_list2:
            if c == 0:
                incomplete2.append_elem(
                    value=0,
                    mob_square_args={'fill_color': BLACK, 'color': WHITE},
                    mob_value_args={'color': "#40E0D0"},
                    play_anim=False, 
                    append_anim=GrowFromCenter
                )
            else:
                incomplete2.append_elem(
                    value=1,
                    mob_square_args={'fill_color': "#40E0D0", 'color': WHITE},
                    mob_value_args={'color': BLACK},
                    play_anim=False,
                    append_anim=GrowFromCenter
                )
        incomplete2.center()   

        for c in incomplete_list:
            if c == 0:
                incomplete.append_elem(
                    value=0,
                    mob_square_args={'fill_color': BLACK, 'color': WHITE},
                    mob_value_args={'color': "#40E0D0"},
                    play_anim=False, 
                    append_anim=GrowFromCenter
                )
            else:
                incomplete.append_elem(
                    value=1,
                    mob_square_args={'fill_color': "#40E0D0", 'color': WHITE},
                    mob_value_args={'color': BLACK},
                    play_anim=False,
                    append_anim=GrowFromCenter
                )
                
        incomplete.center()



        for c in solved_list:
            if c == 0:
                solved.append_elem(
                    value=0,
                    mob_square_args={'fill_color': BLACK, 'color': WHITE},
                    mob_value_args={'color': "#40E0D0"},
                    play_anim=False, 
                    append_anim=GrowFromCenter
                )
            else:
                solved.append_elem(
                    value=1,
                    mob_square_args={'fill_color': "#40E0D0", 'color': WHITE},
                    mob_value_args={'color': BLACK},
                    play_anim=False,
                    append_anim=GrowFromCenter
                )
        
        solved.center()
        solved.move_to(DOWN)
        self.play(Create(incomplete, run_time=2))
        self.play(incomplete.animate.shift(UP))
        self.play(Create(solved, run_time=2))
        target = MArraySlidingWindow(self, solved, 4, 5, 'Target Range', stroke_color = DARK_BLUE, fill_color = DARK_BLUE, color = DARK_BLUE)
        target.color = GOLD

        self.play(Create(target))
        self.wait(3)
        self.updater(incomplete, 0, 1,0.5) 
        self.wait(6)
        front_window = MArraySlidingWindow(self, incomplete, 1, 3, 'To be Moved')
        self.wait(5)
        front_window.color = GOLD
        self.play(Create(front_window))
        self.wait(1)
        back_window = MArraySlidingWindow(self, incomplete, 5, 3, 'Open Spots')
        back_window.color = GOLD
        self.play(Create(back_window))
        self.wait(12)
        self.play(FadeOut(solved), incomplete.animate.move_to(DOWN*2), FadeOut(target))
        line_1 = MathTex(r'\# \text{ good pairs} &= 3 \times 3 = 9', color=GOLD)
        line_2 = MathTex(r'\# \text{ possible pairs} &= {9 \choose 2} = 45', color=GOLD)
        line_3 = MathTex(r'P(\text{good pair}) = \frac{9}{45}', color=GOLD)
        line_4 = MathTex(r'E[x] = \frac{1}{p}', color = GOLD)
        line_5 = MathTex(r'E[x] = \frac{45}{9}', color = GOLD)
        line_6 = MathTex(r'E[x] = 5', color = GOLD)
        line_1.shift(UP*2)
        line_2.shift(UP*0.8)
        line_3.shift(DOWN*0.4)
        self.play(Create(line_1))
        self.wait(9)
        self.play(Create(line_2))
        self.wait(7)
        self.play(Create(line_3))
        self.wait(7)
        self.play(FadeOut(line_1), FadeOut(line_2))
        self.play(line_3.animate.move_to(UP*2))
        dice = self.six_dice()
        self.play(Create(dice))
        self.wait(8)
        self.play(FadeOut(dice))
        self.play(Create(line_4))
        self.play(Transform(line_4, line_5))
        self.play(Transform(line_4, line_6))
        self.wait(6)
        self.play(FadeOut(line_4), FadeOut(line_3), FadeOut(front_window), FadeOut(back_window), incomplete.animate.move_to(ORIGIN))
        self.updater(incomplete, 3,5, 0.5)
        self.wait(4)
        line_3 = MathTex(r'P(\text{good pair}) = \frac{4}{45}', color=GOLD)
        line_5 = MathTex(r'E[x] = \frac{45}{4}', color = GOLD)
        line_3.shift(UP*2.2)
        line_5.shift(UP*1.2)
        self.play(Create(line_3), Create(line_5))
        self.wait(4)
        self.play(FadeOut(line_5), FadeOut(line_3))
        self.updater(incomplete, 1,7, 0.5)
        self.wait(2)
        line_3 = MathTex(r'P(\text{good pair}) = \frac{1}{45}', color=GOLD)
        line_5 = MathTex(r'E[x] = 45', color = GOLD)
        line_3.shift(UP*2.2)
        line_5.shift(UP*1.2)
        self.play(Create(line_3), Create(line_5))
        self.wait(3)
        self.play(FadeOut(line_5), FadeOut(line_3))
        self.updater(incomplete, 2,6, 0.5)
        self.wait(2)
        self.play(FadeOut(incomplete))
        line_ans = MathTex("45 + \\frac{45}{4} + 4 = \\frac{241}{4}", color = GOLD)
        self.play(Write(line_ans))
        self.wait(12)
        self.play(FadeOut(line_ans))
        code = '''
        def solve():
            num_ones = get_number_of_ones()
            spots_to_fill = number of 0's in last num_one elements
            n_choose_2 = n * (n-1) / 2 
            ans = 0
            for i in range(1, spots_to_fill+1):
                ans += n_choose_2  / (i*i)
        '''
        rendered_code = Code(code=code, tab_width=4, background="window",
                            language="Python", font="Monospace")
        rendered_code.shift(UP*1.5)
        incomplete2.shift(DOWN*1.5)
        self.play(Create(rendered_code), Create(incomplete2))
        target = MArraySlidingWindow(self, incomplete2, 4, 5, 'Target Range', stroke_color = DARK_BLUE, fill_color = DARK_BLUE, color = DARK_BLUE)
        self.play(Create(target))
        self.wait(120)
        self.play(FadeOut(rendered_code))
        

        
        