from nicegui import ui
from app.components import bottom_nav, top_nav, background_image

def trip_options_page():
    background_image()
    top_nav()
    with ui.column().classes('w-full max-w-4xl mx-auto mt-10 mb-20'):
        ui.label('Trip Results').classes('text-3xl font-bold')
        for i, budget in enumerate([25000, 32000, 44000, 50000], 1):
            with ui.card().classes('w-full mb-2 rounded-2xl'):
                ui.label(f'Trip Option {i}').classes('w-full text-xl font-semibold bg-gray-400 rounded')
                ui.label('A ... B ... C ... D ...')
                ui.label(f'Total Budget: Rs. {budget:,}')
                ui.button('View Details', on_click=lambda: ui.navigate.to('/trip-details')).classes('rounded-lg')
                bottom_nav()