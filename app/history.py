from nicegui import ui
from app.components import bottom_nav, top_nav, background_image

def history_page():
    background_image()
    top_nav()
    with ui.column().classes('w-full max-w-4xl mx-auto mt-10 mb-20'):
        ui.label('Trip History').classes('text-3xl font-bold')
        trips = [
            ('Goa', '10/01/2025 - 23/01/2025', 25000),
            ('Manali', '15/11/2024 - 19/11/2024', 32000),
            ('Kerala', '04/05/2024 - 21/05/2024', 44000),
            ('Rajasthan', '02/12/2023 - 14/12/2023', 50000)
        ]
        for dest, dates, budget in trips:
            with ui.card().classes('w-full mb-2 rounded-2xl'):
                ui.label(f'{dest}').classes('w-full text-xl font-semibold bg-gray-400 rounded')
                ui.label(f'{dates}')
                ui.label(f'Total Budget: Rs. {budget:,}')
                ui.button('View Destination', on_click=lambda: ui.navigate.to('/trip-history-details'))
                bottom_nav()