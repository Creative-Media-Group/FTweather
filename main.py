import flet as ft
import os
import dotenv as dv


def main(page: ft.Page):
    dv.load_dotenv()
    API_KEY = os.getenv("OPENWEATHER_DEV_API")
    page.appbar
    page.add(ft.SafeArea(ft.Text(API_KEY)))


ft.app(main)
