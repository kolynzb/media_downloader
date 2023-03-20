import flet as ft

from gui.widgets import buttons


def main(page: ft.Page):
    page.title = "Media Downloader"
    page.window_width=1000
    page.window_height=700
    page.bgcolor="#000"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    welc_text = ft.Text(value="Welcome To Media Download",style=ft.TextThemeStyle.DISPLAY_MEDIUM)
 
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
            ft.Image(src=f"/assets/images/icon.png",        width=100,
                height=100,
                fit=ft.ImageFit.CONTAIN,
            ),
            welc_text,
            # Options
            ft.Row(
            controls=[
                    ft.Divider(height=1,thickness=1, color="white"),
                    ft.Text(value="Click Preferred Option Below",style=ft.TextThemeStyle.LABEL_MEDIUM),
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
    gradient=ft.LinearGradient(colors=["#CF0B21","#b55464"]),
    width=2000,
    height=2000,
    padding=0,
        ),
    )

ft.app(target=main)

def run_gui():
    ft.app(target=main)


if __name__ == "__main__":
    run_gui()
