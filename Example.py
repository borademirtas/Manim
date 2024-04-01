from manim import *
from manim_data_structures import * 

GOOD_RED = "#D74D4D"
my_list = [1, 0, 1, 0, 1, 0, 0, 1, 1]

class MyScene(Scene):
    def updater(self, arr, idx, idx2,t):  

        pointer1 = MArrayPointer(self, arr, idx, '')
        pointer2 = MArrayPointer(self, arr, idx2, '')

        value_1 = my_list[idx]
        value_2 = my_list[idx2]
        
        if value_1 <= value_2:
            text = Text(
                text = "a[" + str(idx+1) + "] = " + "a[" + str(idx2+1) + "]",
                font="LM Roman",
                color = GOOD_RED,
                font_size = 40
                ).move_to(DOWN*1.75)
            
                
            if value_1 < value_2:
                text = Text(
                text = "a[" + str(idx+1) + "] < " + "a[" + str(idx2+1) + "]",
                font="LM Roman",
                color = GOOD_RED,
                font_size = 40
                ).move_to(DOWN*1.75) 

            upper_text = Text(
                text = "Cannot Swap",
                color = GOOD_RED
                
            ).move_to(UP*1.25)
            self.play(
                Create(pointer1),
                Create(pointer2)
            )
            self.wait(0.5)
            self.play(
                Write(text),
                Write(upper_text)
            )
            self.wait(t)
            self.play(
            FadeOut(text),
            FadeOut(upper_text),
            FadeOut(pointer1),
            FadeOut(pointer2)
            )   
    
            self.wait(0.5)
            return
        
        color_1 = BLACK
        color_2 = "#40E0D0"

        if value_1 == 0:
            color_1,color_2 = color_2,color_1

        my_list[idx] = my_list[idx]^1
        my_list[idx2] = my_list[idx2]^1

        text = Text(text= "Swap ("  + str(idx+1) + "," +str(idx2+1) + ")",  font_size = 40).move_to(UP*1.25)
        bottom_text = Text(
                text = "a[" + str(idx+1) + "] < " + "a[" + str(idx2+1) + "]",
                font="LM Roman",
                color = "#2CC1A6"
                ).move_to(DOWN*1.75)
        self.play( Create(pointer1),Create(pointer2))   
        self.wait(0.5)
        self.play(Write(text),Write(bottom_text))
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
        self.wait(t)
        self.play(
            FadeOut(text),
            FadeOut(bottom_text),
            FadeOut(pointer1),
            FadeOut(pointer2)
        )

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
        self.add(arr)

        label = Text("Turn Count: ", color=WHITE).to_edge(DL, buff=0.5)
        counter = Integer(0, color=YELLOW).next_to(label, RIGHT).scale(1.5)
        counter_group = VGroup(label, counter)
        counter_group.to_edge(DOWN, buff=1)
        self.play(Create(counter_group))


        self.play(counter.animate.set_value(1), run_time = 0.5)
        self.updater(arr, 2, 3,4) 
        self.play(counter.animate.set_value(2), run_time = 0.5)
        self.updater(arr, 1, 7,3) 
        self.play(counter.animate.set_value(3), run_time = 0.5)
        self.updater(arr, 1, 6,3) 
        self.play(counter.animate.set_value(4), run_time = 0.5)
        self.updater(arr, 0, 6,0.5)
        self.play(counter.animate.set_value(5), run_time = 0.3)
        self.updater(arr, 3, 5,0.5)  
        self.wait(1.75)
        self.play(FadeOut(arr), FadeOut(counter), FadeOut(label))