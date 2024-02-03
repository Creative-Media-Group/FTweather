import flet as ft
import os
import dotenv as dv
import myweather as mr


def main(page: ft.Page):
    page.title = "FTweather"
    page.theme = ft.Theme(color_scheme_seed="white")
    page.update()
    page.appbar = ft.AppBar(title=ft.Text(page.title))
    dv.load_dotenv()
    API_KEY = os.getenv("OPENWEATHER_DEV_API")
    weather = mr.MyWeather(api_key=API_KEY, lat=34, lon=34, setgraddegree="Grad")
    page.add(
        ft.SafeArea(
            ft.Column(
                controls=[ft.Text(weather.degreefunc()), ft.Text(weather.description())]
            ),
        )
    )


ft.app(main)
