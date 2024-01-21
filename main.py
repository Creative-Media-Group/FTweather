import flet as ft
import os
import dotenv as dv


def main(page: ft.Page):
    data = dv.dotenv_values()
    API_KEY = data["OPENWEATHER_DEV_API"]  # os.getenv("OPENWEATHER_DEV_API")
    page.add(ft.SafeArea(ft.Text(API_KEY)))


ft.app(main)
