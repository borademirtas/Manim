from manim import *
from manim_data_structures import * 

list1 = ['1','0','0','1','0','0']

list2 = ['T', '?', 'F', '?' , 'T', '?', 'F']

list3 = ['T', '?', 'T', '=', '?']
list4 = ['T', '?', 'F', '=', '?']

list5 = ['T', '?', 'F', '?', 'F', '=', 'T']

list6 = ['F', '?', 'T', '?', 'T', '?', 'F']

class C(Scene):

    def updater(self, arr, idx, v):

        if v == 'T':
            arr.update_elem_value(index=idx, value=v, play_anim=True)
            self.play(
            arr.animate_elem_square(idx).set_fill(GREEN),
            )
        
        elif v == 'F':
            arr.update_elem_value(index=idx, value=v, play_anim=True)
            self.play(
            arr.animate_elem_square(idx).set_fill(RED),
            )
        
        else:
            arr.update_elem_value(index=idx, value=v, play_anim=True)
            self.play(
            arr.animate_elem_square(idx).set_fill(GOLD),
            )
            


    def construct(self):

        arr = MArray(self,hide_index=True)
        arr2 = MArray(self,hide_index=True)
        arr3 = MArray(self,hide_index=True)
        arr4 = MArray(self,hide_index=True)
        arr5 = MArray(self,hide_index=True)
        arr6 = MArray(self,hide_index=True)
        arr7 = MArray(self,hide_index=True)
        arr8 = MArray(self,hide_index=True)

         
        for c in list1:
            if c == '0':
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

        self.play(Create(arr), run_time=3)

        self.play(arr.animate.shift(DOWN*2))
        

        arr2.append_elem(
        value='1',
        mob_square_args={'fill_color': "#40E0D0", 'color': WHITE},
        mob_value_args={'color': BLACK},
        play_anim=False,
        append_anim=GrowFromCenter
        )
        arr2.append_elem(
        value='=',
        mob_square_args={'fill_color': BLACK, 'color': WHITE},
        mob_value_args={'color': WHITE},
        play_anim=False,
        append_anim=GrowFromCenter
        )
        arr2.append_elem(
        value='T',
        mob_square_args={'fill_color': GREEN, 'color': WHITE},
        mob_value_args={'color': WHITE},
        play_anim=False,
        append_anim=GrowFromCenter
        )
        
        arr2.center()
        self.play(Create(arr2), run_time=2)
        self.play(arr2.animate.shift(UP*2))

        arr3.append_elem(
        value=0,
        mob_square_args={'fill_color': BLACK, 'color': WHITE},
        mob_value_args={'color': "#40E0D0"},
        play_anim=False, 
        append_anim=GrowFromCenter
        )
        arr3.append_elem(
        value='=',
        mob_square_args={'fill_color': BLACK, 'color': WHITE},
        mob_value_args={'color': WHITE},
        play_anim=False,
        append_anim=GrowFromCenter
        )
        arr3.append_elem(
        value='F',
        mob_square_args={'fill_color': RED, 'color': WHITE},
        mob_value_args={'color': WHITE},
        play_anim=False,
        append_anim=GrowFromCenter
        )

        arr3.center()
        self.play(Create(arr3), run_time=2)

        for c in list2:
            if c == 'T':
                arr4.append_elem(
                    value=c,
                    mob_square_args={'fill_color': GREEN, 'color': WHITE},
                    mob_value_args={'color': WHITE},
                    play_anim=False, 
                    append_anim=GrowFromCenter
                )
            elif c == 'F':
                arr4.append_elem(
                    value=c,
                    mob_square_args={'fill_color': RED, 'color': WHITE},
                    mob_value_args={'color': WHITE},
                    play_anim=False, 
                    append_anim=GrowFromCenter
                )
            else:
                arr4.append_elem(
                    value=c,
                    mob_square_args={'fill_color': BLACK, 'color': WHITE},
                    mob_value_args={'color': WHITE},
                    play_anim=False, 
                    append_anim=GrowFromCenter
                )
        
        self.play(FadeOut(arr), FadeOut(arr3), FadeOut(arr2))

        arr4.center()

        self.play(Create(arr4))

        self.updater(arr4,1,'∨')
        self.updater(arr4,5,'∧')
        self.updater(arr4,3,'∧')


        pointer = MArrayPointer(self, arr4, 3, '')
        self.play(Create(pointer))
        self.updater(arr4,3,'F')
        self.play(FadeOut(pointer))
        arr4.remove_elem(2)
        arr4.remove_elem(3)
        self.play(arr4.animate.move_to(ORIGIN))

        pointer = MArrayPointer(self, arr4, 3, '')
        self.play(FadeIn(pointer))
        self.updater(arr4,3,'F')
        self.play(FadeOut(pointer))
        arr4.remove_elem(2)
        arr4.remove_elem(2)
        self.play(arr4.animate.move_to(ORIGIN))

        self.play(FadeOut(arr4))

        text_1 = Text("Alice wants to get True\n\n\nBob wants to get False\n\n\nWho will win?").move_to(UP*0.5)
        self.play(Create(text_1, run_time = 6))
        self.wait(3)
        self.play(FadeOut(text_1))

        hint_1 = Text("Hint 1: Look at the truth table").move_to(UP*(1.5))
        self.play(Create(hint_1))

        for c in list3:
            if c == 'T':
                arr5.append_elem(
                    value=c,
                    mob_square_args={'fill_color': GREEN, 'color': WHITE},
                    mob_value_args={'color': WHITE},
                    play_anim=False, 
                    append_anim=GrowFromCenter
                )
            elif c == 'F':
                arr5.append_elem(
                    value=c,
                    mob_square_args={'fill_color': RED, 'color': WHITE},
                    mob_value_args={'color': WHITE},
                    play_anim=False, 
                    append_anim=GrowFromCenter
                )
            else:
                arr5.append_elem(
                    value=c,
                    mob_square_args={'fill_color': BLACK, 'color': WHITE},
                    mob_value_args={'color': WHITE},
                    play_anim=False, 
                    append_anim=GrowFromCenter
                )
        for c in list4:
            if c == 'T':
                arr6.append_elem(
                    value=c,
                    mob_square_args={'fill_color': GREEN, 'color': WHITE},
                    mob_value_args={'color': WHITE},
                    play_anim=False, 
                    append_anim=GrowFromCenter
                )
            elif c == 'F':
                arr6.append_elem(
                    value=c,
                    mob_square_args={'fill_color': RED, 'color': WHITE},
                    mob_value_args={'color': WHITE},
                    play_anim=False, 
                    append_anim=GrowFromCenter
                )
            else:
                arr6.append_elem(
                    value=c,
                    mob_square_args={'fill_color': BLACK, 'color': WHITE},
                    mob_value_args={'color': WHITE},
                    play_anim=False, 
                    append_anim=GrowFromCenter
                )
        
        arr5.center()
        self.play(Create(arr5))
        self.updater(arr5,1,'∨')
        self.updater(arr5,4,'T')
        self.updater(arr5,1,'∧')
        
        self.play(arr5.animate.shift(DOWN*1.5))

        arr6.center()
        self.play(Create(arr6))
        self.updater(arr6,1,'∨')
        self.updater(arr6,4,'T')
        self.updater(arr6,1,'∧')
        self.updater(arr6,4,'F')
        self.wait(3)
        self.play(FadeOut(arr6), FadeOut(arr5), FadeOut(hint_1))
        


        for c in list5:
            if c == 'T':
                arr7.append_elem(
                    value=c,
                    mob_square_args={'fill_color': GREEN, 'color': WHITE},
                    mob_value_args={'color': WHITE},
                    play_anim=False, 
                    append_anim=GrowFromCenter
                )
            elif c == 'F':
                arr7.append_elem(
                    value=c,
                    mob_square_args={'fill_color': RED, 'color': WHITE},
                    mob_value_args={'color': WHITE},
                    play_anim=False, 
                    append_anim=GrowFromCenter
                )
            else:
                arr7.append_elem(
                    value=c,
                    mob_square_args={'fill_color': BLACK, 'color': WHITE},
                    mob_value_args={'color': WHITE},
                    play_anim=False, 
                    append_anim=GrowFromCenter
                )
        
        hint_2 = Paragraph(
            "Hint 2: Alice wins if there is a True left after",
            "all the AND operations", 
            alignment="center"
        )

        hint_2.scale(0.75)  
        hint_2.move_to(ORIGIN).shift(UP * 2) 
    
        self.play(Create(hint_2))
        
        arr7.center()
        self.play(Create(arr7, run_time = 4))
        self.updater(arr7,1,'∨')
        self.wait(2)
        self.play(FadeOut(arr7))

        for c in list6:
            if c == 'T':
                arr8.append_elem(
                    value=c,
                    mob_square_args={'fill_color': GREEN, 'color': WHITE},
                    mob_value_args={'color': WHITE},
                    play_anim=False, 
                    append_anim=GrowFromCenter
                )
            elif c == 'F':
                arr8.append_elem(
                    value=c,
                    mob_square_args={'fill_color': RED, 'color': WHITE},
                    mob_value_args={'color': WHITE},
                    play_anim=False, 
                    append_anim=GrowFromCenter
                )
            else:
                arr8.append_elem(
                    value=c,
                    mob_square_args={'fill_color': BLACK, 'color': WHITE},
                    mob_value_args={'color': WHITE},
                    play_anim=False, 
                    append_anim=GrowFromCenter
                )

        arr8.center()
        self.play(Create(arr8))
        self.wait(1)
        self.updater(arr8, 1, '∨')

        p1 = MArrayPointer(self, arr8, 3, '')
        p2 = MArrayPointer(self, arr8, 5, '')
        self.play(Create(p1), Create(p2))
        
        self.updater(arr8, 3, '∧')
        self.updater(arr8, 5, '∨')
        
        self.updater(arr8, 5, '∧')
        self.updater(arr8, 3, '∨')
        self.wait(2)
        self.play(FadeOut(arr8), FadeOut(p1), FadeOut(p2), FadeOut(hint_2))

        cpp_code = """
        int n; cin >> n;
        string s; cin >> s;
        bool flag = false;
        if(s[0]=='1'||s[n-1]=='1'){flag = true;}
        for(int i = 0; i < n-1; i++){
            if(s[i]=='1' && s[i+1]=='1'){flag = true;}
        }
        if(flag){cout << "YES" << endl;}
        else{cout << "NO" << endl;}
        """
        
        code = Code(
            code=cpp_code,
            tab_width=4,
            background="window",
            language="C++",
            font="Monospace",
            font_size=24,
        )
        code.move_to(ORIGIN)
        self.play(FadeIn(code))
        self.wait(10)
        self.play(FadeOut(code))
