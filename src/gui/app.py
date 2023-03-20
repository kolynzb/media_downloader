import flet as ft

def main(page: ft.Page):
    page.title = "Media Downloader"
    page.window_width=1000
    page.window_height=600
    page.bgcolor="#000"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    welc_text = ft.TextField(value="Welcome To Media Download",text_style=ft.TextStyle(20))
    opt_btn= ft.TextButton(text="Youtube Download")
    btm_btn= ft.IconButton(icon=ft.icons.HISTORY)
    btn_row=ft.Row(controls=[opt_btn,btm_btn],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,width=500)
    page.add(
        welc_text,
        btn_row,
    )

ft.app(target=main)

def run_gui():
    ft.app(target=main)


if __name__ == "__main__":
    run_gui()