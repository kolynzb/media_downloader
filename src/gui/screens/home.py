import math

import flet as ft

from ..widgets import buttons


class Home(ft.UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page
    
    def build(self):
        
        welc_text = ft.Text(value="Welcome To Media Downloader",style=ft.TextThemeStyle.DISPLAY_MEDIUM,font_family="mont",weight=ft.FontWeight.W_500)
 
        opt_row=ft.Row(controls=[
            buttons.OptBtn(btn_name="Video",onclick= lambda _: self.page.go('/videodl')),
            buttons.OptBtn(btn_name="Audio"),
            buttons.OptBtn(btn_name="Video Playlist"),
            buttons.OptBtn(btn_name="Subtitle"),
            buttons.OptBtn(btn_name="Audio Playlist"),
            buttons.OptBtn(btn_name="Trimmed Audio"),
            buttons.OptBtn(btn_name="Trimmed Video"),
        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,vertical_alignment=ft.CrossAxisAlignment.CENTER,wrap=True,width=500)


        btn_row=ft.Row(controls=[
            ft.IconButton(icon=ft.icons.HISTORY,tooltip="Download History"),
            ft.IconButton(icon=ft.icons.SETTINGS,tooltip="Settings"),
            ft.IconButton(icon=ft.icons.CODE,tooltip="Github Link"),
        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,width=100)

        return ft.Container(
        content = ft.Column(
        controls=[
            ft.Image(
                # src=f"/images/icon.png",
                src="https://res.cloudinary.com/kolynz-b/image/upload/v1679497275/icon_gqdmib.png",
                width=150,
                height=150,
                fit=ft.ImageFit.CONTAIN,
            ),
            welc_text,
            # Options
            ft.Row(
            controls=[
                    ft.Divider(height=1,thickness=1, color="white"),
                    ft.Text(value="Click Preferred Option Below",style=ft.TextThemeStyle.LABEL_MEDIUM,font_family="Mont"),
                    ft.Divider(height=1,thickness=1, color="white"),
            ],
            alignment= ft.MainAxisAlignment.CENTER,
            ),
            opt_row,
            btn_row
            ],
            # alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            spacing=30,
        ),
        expand=True,
        margin=0,
        gradient=ft.LinearGradient(colors=["#ff24030e","#ff22133c"],begin=ft.alignment.top_left, end=ft.Alignment(0.8, 1),tile_mode=ft.GradientTileMode.MIRROR,rotation=math.pi / 3,),
        width=2000,
        height=2000,
        padding=0,
        )
    

         
    


