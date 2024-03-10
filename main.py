import flet as ft
import os
import dotenv as dv
import myweather as mr

dv.load_dotenv()
API_KEY = os.getenv("OPENWEATHER_DEV_API")
weather = mr.MyWeather(api_key=API_KEY, lat=34, lon=34, setgraddegree="Grad")


def main(page: ft.Page):
    def i(e):
        print(e)

    def city(city, key=API_KEY):
        container = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon(name=ft.icons.CLOUD),
                    ft.Text(value=weather.degreefunc()),
                    ft.Text(city),
                ],
                alignment="center",
                spacing=6,
            ),
            alignment=ft.alignment.center,
            border_radius=10,
            width=80,
            height=90,
            bgcolor=ft.colors.AMBER,
            on_click=lambda e: i(e=e),
        )

        return container

    page.title = "FTweather"
    page.update()
    page.appbar = ft.AppBar(title=ft.Text(page.title), center_title=True)

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
