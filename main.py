import flet as ft
import os
import dotenv


def main(page: ft.Page):
    API_KEY = #os.getenv("OPENWEATHER_DEV_API")
    page.add(ft.SafeArea(ft.Text(API_KEY)))


ft.app(main)
