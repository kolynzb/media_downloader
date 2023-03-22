from flet import *
from .screens.home import Home
from .screens.video_dl import VideoDlScreen


def views_handler(page):
  return {
    '/':View(
        route='/',
        controls=[
          Home(page)
        ]
      ),
    '/videodl':View(
        route='/videodl',
        controls=[
          VideoDlScreen(page)
        ]
      ),
  }