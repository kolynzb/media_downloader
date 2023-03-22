

import flet as ft

from .views import views_handler


def main(page: ft.Page):
    def route_change(route):
        print(page.route)
        page.views.clear()
        page.views.append(
        views_handler(page)[page.route]
        )

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


    page.on_route_change = route_change
    page.go('/videodl')

def run_gui():
    return ft.app(target=main, assets_dir="./assets")


if __name__ == "__main__":
    run_gui()
