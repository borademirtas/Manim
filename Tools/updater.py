    def updater(self, arr, idx, v, fill_color):

        arr.update_elem_value(index=idx, value=v, play_anim=True)

        color = WHITE

        if v in fill_color:
            color = fill_color

        self.play(
            arr.animate_elem_square(idx).set_fill(color),
        )
