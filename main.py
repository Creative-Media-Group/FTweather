import flet as ft
import os
import dotenv as dv
import myweather as mr
dv.load_dotenv()
API_KEY = os.getenv("OPENWEATHER_DEV_API")

def city(page, key=API_KEY, city):
    weather = mr.MyWeather(api_key=API_KEY, lat=34, lon=34, setgraddegree="Grad")

def main(page: ft.Page):
    page.title = "FTweather"
    page.theme = ft.Theme(color_scheme_seed="white")
    page.update()
    page.appbar = ft.AppBar(title=ft.Text(page.title))
    
    page.add(
        ft.SafeArea(
            ft.Column(
                controls=[ft.Text(weather.degreefunc()), ft.Text(weather.description())]
            ),
        )
    )


ft.app(main)
