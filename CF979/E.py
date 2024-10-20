from manim import *
from manim_data_structures import * 

import itertools



class E(Scene):

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

    def updater(self, arr, idx, v, color):

        self.play(
            arr.animate_elem_square(idx).set_fill(color),
        )


    def construct(self):
        
        
        mex = MArray(self,hide_index=True)
        b = MArray(self,hide_index=True)
        example = MArray(self,hide_index=True)
        c = MArray(self,hide_index=True)

        self.construct_array(mex, [0,1,1,4,5], {},{},{})
        self.construct_array(b, [0,0,0,1,1,2], {},{},{})
        self.construct_array(example, [0,0,0,1,1,1,1,2,4], {},{},{})
        self.construct_array(c, [0,0,1,2,2], {},{},{})
        
        text = Text("What is MEX?", color = GOLD)
        text.shift(UP*1.5)

        self.play(Create(mex))
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(mex), FadeOut(text))
        
        self.play(Create(b))

        self.updater(b,0,0,GREEN)
        self.updater(b,1,0,BLUE)
        self.updater(b,2,0,RED)
        self.updater(b,3,0,GREEN)
        self.updater(b,4,0,BLUE)
        self.updater(b,5,0,GREEN)

        score = Text("Score: 3 + 2 + 1 = 6")
        score.shift(DOWN*1.5)
        self.play(Write(score))
        self.wait(3)

        question = Text("Find the score of all the subsets of an array.", font_size = 32, color = GOLD)
        question.shift(UP*1.5)
        self.play(Write(question))
        self.wait(3)
        question2 = Text("Subproblem: Find the score of an array", font_size = 32, color = GOLD)
        question2.shift(UP*1.5)
        self.play(Transform(question, question2))
        self.play(FadeOut(score), FadeOut(b))
        self.play(Create(example))
        self.wait(3)
        self.updater(example,0,0,GREEN)
        self.updater(example,1,0,BLUE)
        self.updater(example,2,0,RED)
        self.wait(5)
        self.updater(example,3,0,GREEN)
        self.updater(example,4,0,BLUE)
        self.updater(example,5,0,RED)
        self.wait(5)
        self.updater(example,6,0,BLACK)
        self.wait(5)
        self.updater(example,7,0,GREEN)
        self.wait(5)
        self.updater(example,8,0,BLACK)
        self.wait(3)
        self.play(FadeOut(*self.mobjects))


        claim = MathTex(r"\text{Claim: The } i\text{-th occurrence of a number } x \text{ increases the score }", r"\\\text{if all previous numbers have appeared at least } i \text{ times.} ")
        self.play(Create(claim))
        self.wait(3)
        self.play(FadeOut(*self.mobjects))
        self.play(Create(c))
        self.wait(3)

        hint = Text("Hint: Find the contribution of the zeros", font_size = 32, color = GOLD)
        question3 = Text("How many ways can we choose a subset that has one zero?", font_size = 32, color = GOLD)
        question4 = Text("How many ways can we choose a subset that has two zeros?", font_size = 32, color = GOLD)
        contrib = MathTex(r"2^{2} - 1 = 3")
        contrib.shift(DOWN*1.5)
        
        contrib2 = MathTex(r"3 \times 2^{3} = 24")
        contrib2.shift(DOWN*1.5)

        contrib4 = MathTex(r"3 - \binom{2}{1}")
        contrib4.shift(DOWN*1.5)
        contrib5 = MathTex(r"3 - 2 = 1")
        contrib5.shift(DOWN*1.5)

        hint.shift(UP*1.5)
        self.play(Write(hint))
        self.wait(5)
        question3.shift(UP*1.5)
        question4.shift(UP*1.5)
        self.play(Transform(hint,question3))
        self.wait(3)
        self.play(Write(contrib))

        window = MArraySlidingWindow(self, c, 2,3)
        self.play(Create(window))
        self.wait(3)
        self.play(Transform(contrib, contrib2))
        self.wait(3)
        self.play(FadeOut(window), FadeOut(contrib))
        self.play(Transform(hint, question4))
        self.wait(3)
        self.play(Write(contrib4))
        self.wait(1)
        self.play(Transform(contrib4,contrib5))
        self.wait(3)

        self.play(FadeOut(*self.mobjects))
        
        ways = Text("Ways[i][j] = the number of ways to select j occurences of the value i", color = GOLD, font_size =32)
        self.play(Write(ways))
        self.wait(3)
        ways2 = MathTex(r"\text{Ways}[i][j] = 2^n - \sum_{k=0}^{j-1} \binom{n}{k}")
        ways2.shift(DOWN*1.5)
        self.play(Write(ways2))
        self.wait(3)
        self.play(FadeOut(*self.mobjects))

        self.play(Create(c))
        self.wait(10)
        self.play(FadeOut(*self.mobjects))

        totalways = Text("Total_Ways[i][j] = \nthe number of ways to select j subsets that have the numbers {0,1,...,i-1,i}", color = GOLD, font_size =28)
        self.play(Write(totalways))
        self.wait(10)
        totalways2 = MathTex(r"\text{Total\_Ways}[i][j] = \text{Ways}[i][j] \times \text{Total\_Ways}[i-1][j]", color = GOLD)
        totalways2.shift(DOWN*1.5)
        self.play(Write(totalways2))
        self.wait(10)
        self.play(FadeOut(*self.mobjects))

        cpp_code1 = """
        ll mod = 998244353;
        vll invt, inv,fac,powers;
        void precalc(ll n){
            invt.resize(n+5); fac.resize(n+5);
            inv.resize(n+5); powers.resize(n+5); 
            invt[1] = 1; fac[0] = 1; inv[0]=1; inv[1]=1; powers[0]=1;
            for(ll i = 1; i <= n; i++){
                powers[i]=powers[i-1]*2%mod;
            }
            for(ll i = 1; i < fac.size(); i++){
                fac[i] = fac[i-1] * i; fac[i] %= mod;
            }
            for(ll i=2; i<=n; i++){ 
                invt[i] = (mod - ((mod/i)*invt[mod%i])%mod)%mod;
            }
            for(ll i = 1; i <= n; i++){
                inv[i]=invt[i]*inv[i-1]%mod;
            }
        }
        ll ncr(ll n, ll k) { 
            return fac[n] * inv[n-k] % mod * inv[k] % mod;
        }
        """


        code1 = Code(
            code=cpp_code1,
            tab_width=4,
            background="window",
            language="C++",
            font="Monospace",
            font_size=24,
        )
        code1.move_to(ORIGIN)
        self.play(FadeIn(code1))
        self.wait(10)
        self.play(FadeOut(code1))

        cpp_code2 = """
    ll n; cin >> n;
    vll cnt(n);
    vector<vll> ways(n);
    vector<vll> total_ways(n);
 
    for(ll i = 0; i < n; i++){ll x; cin >> x; cnt[x]++;}
 
    vll larger_than(n);
    larger_than[0] = n-cnt[0];
 
    ways[0].resize(cnt[0]+1);
    total_ways[0].resize(cnt[0]+1);
 
    for(ll i = 1; i < n; i++){
        ways[i].resize(min(cnt[i]+1,(ll)ways[i-1].size()));
        total_ways[i].resize(min(cnt[i]+1,(ll)total_ways[i-1].size()));
        larger_than[i] = larger_than[i-1]-cnt[i];
    }
        """

        code2 = Code(
            code=cpp_code2,
            tab_width=4,
            background="window",
            language="C++",
            font="Monospace",
            font_size=24,
        )
        code2.move_to(ORIGIN)
        self.play(FadeIn(code2))
        self.wait(25)
        self.play(FadeOut(code2))


        cpp_code3 = """
    ll ans = 0;
 
    for(ll i = 0; i < n; i++){
        ways[i][0]=powers[cnt[i]];
        for(ll j = 1; j < ways[i].size(); j++){
            ways[i][j]=ways[i][j-1]-ncr(cnt[i],j-1);
            if(ways[i][j]<0){ways[i][j]+=mod;}
        }
        if(i==0){total_ways[i] = ways[i];}
        else{
            for(ll j = 0; j < ways[i].size(); j++){
                total_ways[i][j]=ways[i][j]*total_ways[i-1][j];
                total_ways[i][j]%=mod;
            }
        }
        for(ll j = 1; j < ways[i].size(); j++){
            ans += total_ways[i][j]*powers[larger_than[i]]; ans%=mod;
        }
    }
 
    cout << ans << endl;
        """

        code3= Code(
            code=cpp_code3,
            tab_width=4,
            background="window",
            language="C++",
            font="Monospace",
            font_size=24,
        )
        code3.move_to(ORIGIN)
        self.play(FadeIn(code3))
        self.wait(25)
        self.play(FadeOut(code3))
        
