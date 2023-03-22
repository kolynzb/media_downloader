import math

import flet as ft

from gui.widgets import buttons


def main(page: ft.Page):
    page.title = "Media Downloader"
    page.window_width=1000
    page.window_height=700
    page.bgcolor="#000"
    page.padding = 0
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        "Montserrat": "/fonts/Montserrat-wght.ttf",
        "mont": "https://raw.githubusercontent.com/google/fonts/master/ofl/montserrat/Montserrat[wght].ttf"
    }

    page.theme = ft.Theme(font_family="mont")
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    welc_text = ft.Text(value="Welcome To Media Download",style=ft.TextThemeStyle.DISPLAY_MEDIUM,font_family="mont",weight=ft.FontWeight.W_500)
 
    opt_row=ft.Row(controls=[
        buttons.OptBtn(btn_name="Video"),
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
    page.add(
        ft.Container(
        content = ft.Column(
        controls=[
            # TODO: Figure Out Image
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
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
        ),
    expand=True,
    margin=0,
    gradient=ft.LinearGradient(colors=["#ff24030e","#ff22133c"],begin=ft.alignment.top_left, end=ft.Alignment(0.8, 1),tile_mode=ft.GradientTileMode.MIRROR,rotation=math.pi / 3,),
    width=2000,
    height=2000,
    padding=0,
        ),
    )

ft.app(target=main, assets_dir="./assets")

def run_gui():
    ft.app(target=main, assets_dir="./assets")


if __name__ == "__main__":
    run_gui()
