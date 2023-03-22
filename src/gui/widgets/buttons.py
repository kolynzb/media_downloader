import flet as ft


class OptBtn(ft.UserControl):
    def __init__(self,btn_name,onclick = None):
        super().__init__()
        self.btn_name = btn_name
        self.onclick = onclick


    def build(self):

        opt_btn= ft.OutlinedButton(
            width=150,
            content=ft.Row(
                [
                    ft.Text(value=self.btn_name,style=ft.TextThemeStyle.LABEL_MEDIUM,font_family="Mont",weight=ft.FontWeight.W_400),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
            tooltip=f"Download {self.btn_name}",
            style=ft.ButtonStyle(
            bgcolor={
                ft.MaterialState.HOVERED: ft.colors.PURPLE_800,
                ft.MaterialState.FOCUSED: ft.colors.PURPLE_800,
                ft.MaterialState.DEFAULT: ft.colors.TRANSPARENT,
            },
            animation_duration=600,
            )
        )

        return opt_btn