import flet as ft
import os
import dotenv as dv
import myweather as mr

dv.load_dotenv()
API_KEY = os.getenv("OPENWEATHER_DEV_API")


def city(page, city, key=API_KEY):
    weather = mr.MyWeather(api_key=API_KEY, lat=34, lon=34, setgraddegree="Grad")
    container = ft.Container(content=ft.Column(controls=[ft.Icon(name=ft.icons.CLOUD),ft.Text()]),border_radius=10,width=80, height=80,bgcolor=ft.colors.AMBER)
    return container


def main(page: ft.Page):
    page.title = "FTweather"
    page.update()
    page.appbar = ft.AppBar(title=ft.Text(page.title))

    page.add(
        ft.SafeArea(
            ft.Column(
                controls=[
                    city(page=page, city="Hattingen")
                ]  # ft.Text(weather.degreefunc()), ft.Text(weather.description())
            ),
        )
    )


ft.app(main)
