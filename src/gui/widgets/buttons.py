import flet as ft


class OptBtn(ft.UserControl):
    def __init__(self,btn_name,onclick = None):
        super().__init__()
        self.btn_name = btn_name
        self.onclick = onclick

    def build(self):
        opt_btn= ft.TextButton(text=self.btn_name,on_click=self.onclick)
        return opt_btn