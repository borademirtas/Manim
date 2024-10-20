from manim import *
from manim_data_structures import * 



list = ['R','R','R','L','L']

class D(Scene):

    def construct_array(self, arr, vals, outer_color , fill_color, value_color) :

        fill = "#40E0D0"
        out = WHITE
        val = BLACK

        for v in vals:
            
            
            if v in fill_color:
                fill = fill_color[v]
            
            if v in outer_color:
                out = outer_color[v]
            
            if v in value_color:
                val = value_color[v]
            
            arr.append_elem(
                    value=v,
                    mob_square_args={'fill_color': fill, 'color': out},
                    mob_value_args={'color': val},
                    play_anim=False, 
                    append_anim=GrowFromCenter
                )
            arr.center()

    def updater(self, arr, idx, v, fill_color):

        arr.update_elem_value(index=idx, value=v, play_anim=True)

        color = WHITE

        if v in fill_color:
            color = fill_color[v]

        list[idx]=v

        self.play(
            arr.animate_elem_square(idx).set_fill(color),
        )


    def construct(self):
        
        arr = MArray(self,hide_index=True)
        arr2 = MArray(self,hide_index=True)
        max = MArray(self,hide_index=True)

        self.construct_array(max,[1,4,4,5,5],{},{},{})
        self.construct_array(arr,[1,4,2,5,3],{},{},{})
        self.construct_array(arr2,list,{},{'R':RED, 'L':GREEN},{'R':BLACK, 'L':BLACK})
        self.play(Create(arr))
        arr.update_mob_arr_label('permutation')
        arr2.shift(DOWN*2)
        self.play(Create(arr2))
        arr2.update_mob_arr_label('string')


        p = MArrayPointer(self,arr2, 1,'')
        self.play(Create(p))
        self.updater(arr2, 1, 'L', {'L':GREEN})
        self.play(FadeOut(p))

        arrows = []

        for i in range(5):
            pointer = MArrayPointer(self,arr,i,'')
            
            if list[i]=='L':
                arrow = ArcBetweenPoints(pointer.get_top(), pointer.get_top()+LEFT,angle=-PI/2)
            else:
                arrow = ArcBetweenPoints(pointer.get_top(), pointer.get_top()+RIGHT,angle=PI/2)
            self.play(Create(arrow))
            arrows.append(arrow)
        
        group = VGroup(*arrows)

        claim = Text("Claim: We can't swap a[i] and a[i+1] if s[i]==L and s[i+1]==R", font_size=32, color=GOLD)

        hint = Text("Hint: Try to find if a block prevents from sorting", font_size = 32, color = GOLD)

        claim.shift(UP*2)
        hint.shift(UP*2)
        self.play(Create(claim))
        self.wait(4)
        self.play(Transform(claim,hint))
        self.wait(4)
        self.play(FadeOut(claim))
        self.wait(3)

        max.shift(UP*2)
        self.play(Create(max))
        max.update_mob_arr_label('max')
        self.wait(3)

        self.play(FadeOut(arrows[1]))

        self.updater(arr2, 1, 'R', {'R':RED})

        

        pointer = MArrayPointer(self,arr,1,'')
        arrow1 = ArcBetweenPoints(pointer.get_top(), pointer.get_top()+RIGHT,angle=PI/2)
        self.play(Create(arrow1))
        self.wait(3)


        cpp_code = """
        int n,q; cin >> n >> q;
        vector<int> a(n+1); for(int i = 1; i <= n; i++){cin >> a[i];}
        string s; cin >> s;
        int cnt = 0;
 
        vector<int> pre(n+2);
        for(int i = 1; i <= n; i++){
            pre[i] = max(pre[i-1], a[i]);
        }
 
        auto check = [&](int i, bool add){
            if(s[i-1]=='L'&&s[i]=='R' && pre[i]>i){
                if(add){cnt++;}
                else{cnt--;}
            }
        };
    
        for(int i = 1; i < n; i++){
            check(i,true);
        }
    
        for(int i = 0; i < q; i++){
            int x; cin >> x;
            check(x,false); check(x-1, false);
            if(s[x-1]=='L'){s[x-1]='R';}
            else{s[x-1]='L';}
            check(x,true); check(x-1, true);
            if(cnt>0){cout << "NO" << endl;}
            else{cout << "YES" << endl;}
        }
        """

        self.play(FadeOut(*self.mobjects))

        code = Code(
            code=cpp_code,
            tab_width=4,
            background="window",
            language="C++",
            font="Monospace",
            font_size=24,
        )
        code.move_to(ORIGIN)
        code.scale(0.75)
        self.play(FadeIn(code))
        self.wait(25)
        self.play(FadeOut(code))
