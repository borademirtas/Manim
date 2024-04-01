from manim import *

from manim_data_structures import *

GOOD_RED = "#D74D4D"
my_list = [1,1,1,1,0,0,0,0]

from manim import *

class Ending(Scene):
    
    def construct(self):
        text = MathTex(
            r"\text{You are given a binary array of } 2n \text{ integers with the first } n \text{ values }",
            r"\text{of the array being } 1 \text{ while the last } n \text{ values of the array are } 0.",
            r"\text{With the operations in the original problem:}",
            r"\text{What is the probability you will sort the array in n operations?}"
        
        )  
    
        arr = MArray(
            self,
            hide_index=True,
        )
        text.scale(1.3)
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
        arr.move_to(DOWN*1.2)
        text.set_color(GOLD)
        text.scale(0.7)
        text.arrange(DOWN)
        text.move_to(UP*1.2)
        text_1 = Tex("1. Choose two random indices $i$ and $j$ such that $i < j$.", color = GOLD)
        text_2 = Tex("2. If $a_i > a_j$, then swap elements $a_i$ and $a_j$.", color = GOLD)
        text_1.shift(DOWN*2.2)
        text_2.shift(DOWN*3.1)
        self.play(Create(text, run_time = 5), Create(arr, run_time = 5))
        self.play(Create(text_1), Create(text_2))
        self.wait(30)