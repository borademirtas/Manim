from manim import *
from manim_data_structures import * 

a = [2,11,14,7,1,2,98]
l = 3
r = 10

class C(Scene):

    def updater(self, arr, point, sz, time):
        window = MArraySlidingWindow(self,arr, point, sz)

        sum = 0
        for i in range(point, point+sz):
            sum += a[i]

        text = Text("Sum = " + str(sum))
        
        text.shift(UP*2)
        

        if l <= sum <= r:
            text.color = GREEN
            text2 = Text("In range", color = GREEN)
        else:
            text.color = RED
            text2 = Text("Not in range", color = RED)
        text2.shift(UP)

        self.play(Create(window))
        self.play(Create(text))
        self.play(Create(text2))
        self.wait(time)
        self.play(FadeOut(text), FadeOut(text2), FadeOut(window))
        

    def construct(self):

        

        arr = MArray(
            self,
            arr = a,
            hide_index=True,
        )

        arr.center()

        text = Text("Range: [3,10]")
        text.shift(DOWN*2)

        self.play(Create(arr),Create(text))
        
        self.updater(arr,0,3,4)

        self.updater(arr,3,3,4)
        
        #real game
        self.updater(arr,0,1,6)

        self.updater(arr,1,2,6)

        self.updater(arr,3,1,6)

        self.updater(arr,4,2,5)

        self.updater(arr,6,1,5)

        hint = Text("Hint: Don't use cards if you don't have to")
        hint.shift(UP)
        self.play(Create(hint))
        self.wait(10)
        self.play(hint.animate.shift(UP*2))

        self.updater(arr,3,1,5)

        self.updater(arr,4,2,5)
        solution = Text("Solution: Try to greedily find winning games")
        solution.shift(UP*3)
        self.play(Transform(hint,solution))
        self.wait(5)

        cpp_code = """
            ll n,l,r;
            cin >> n >> l >> r;
            vector<ll> a(n), prefix(n+1);
            for(ll i = 0; i < n; i++){cin >> a[i];}
            for(ll i = 0; i < n; i++){prefix[i+1]=prefix[i]+a[i];}
            ll ans = 0;
            for(ll i = 0; i < n; i++){
                ll x = lower_bound(prefix.begin(), prefix.end(),l+prefix[i]) 
                - prefix.begin();
                if(x>n){continue;}
                if(prefix[x]-prefix[i]<=r){
                    ans++; i=x-1;
                }
            }
            cout << ans << endl;
        """

        code = Code(
            code=cpp_code,
            tab_width=4,
            background="window",
            language="C++",
            font="Monospace",
            font_size=24,
        ).scale(0.8)
        code.move_to(ORIGIN)
        self.play(FadeIn(code))
        self.wait(30)
        self.play(FadeOut(code))