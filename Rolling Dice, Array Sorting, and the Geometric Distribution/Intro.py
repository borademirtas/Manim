from manim import *
from manim_data_structures import * 

GOOD_RED = "#D74D4D"
my_list = [1, 0, 1, 0, 1, 0, 0, 1, 1]

class Intro(Scene):
    def construct(self):
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
         
        arr.center()
        self.play(Create(arr), run_time=5)
        text_1 = Tex("1. Choose two random indices $i$ and $j$ such that $i < j$.").move_to(UP*2)
        text_2 = Tex("2. If $a_i > a_j$, then swap elements $a_i$ and $a_j$.").move_to(UP)

        self.play(arr.animate.shift(DOWN *0.75))
        self.play(Create(text_1), run_time = 1.5)
        self.wait(12)
        self.play(Create(text_2), run_time = 1.5)
        self.wait(4)
        self.play(arr.animate.shift(UP*0.75), FadeOut(text_1), FadeOut(text_2)) 
        self.wait(2.5)

        