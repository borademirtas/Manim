    def construct_array(self, arr, vals, outer_color, fill_color, value_color):
        
        fill = BLACK
        out = WHITE
        val = WHITE

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
