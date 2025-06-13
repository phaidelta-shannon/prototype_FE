from nicegui import ui
from app.components import top_nav, bottom_nav, background_image

def profile_page():
    top_nav()
    background_image()
    with ui.column().classes('w-full max-w-3xl mx-auto mt-16 mb-20 items-center text-black'):

        # Greeting
        ui.label('Good day User!').classes('text-3xl font-bold')
        ui.label('Joined on 28 May 2025').classes('text-sm text-gray-600 mb-2')

        # Avatar
        ui.image(
            'https://cdn-icons-png.flaticon.com/512/8608/8608769.png'
        ).classes('w-40 rounded-full mb-2')

        # Preferences title
        ui.label('Preferences:').classes('text-lg font-semibold mb-2')

        # Preference Buttons Grid
        with ui.row().classes('justify-center flex-wrap gap-4 mb-6'):
            preferences = [
                ('Stay', 'hotel'),
                ('Budget', 'savings'),
                ('Sightseeing', 'photo_camera'),
                ('Food', 'restaurant'),
                ('Transport', 'commute'),
                ('Activities', 'hiking'),
            ]
            for label, icon in preferences:
                with ui.button(on_click=lambda l=label: ui.notify(f'{l} clicked')) \
                        .classes('w-24 h-24 rounded-xl shadow bg-white text-black'):
                    with ui.column().classes('items-center justify-center'):
                        ui.icon(icon).classes('text-3xl')
                        ui.label(label).classes('text-sm text-center')

        # Plan Trip Button
        ui.button('Plan Your Trip', on_click=lambda: ui.navigate.to('/planner')) \
            .classes('mt-2 rounded-xl px-6 py-2 bg-blue-500 text-white')

    bottom_nav()