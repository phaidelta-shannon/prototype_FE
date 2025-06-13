from nicegui import ui
from app.components import bottom_nav, top_nav, background_image

def trip_history_details_page():
    background_image()
    top_nav()

    with ui.column().classes('w-full max-w-3xl mx-auto mt-16 mb-20 items-center'):

        ui.label('Destination').classes('text-3xl font-bold')
        ui.label('02/12/2023 – 14/12/2023').classes('text-md text-gray-600 mb-4')

        sections = {
            'Stay Options': {
                'icon': 'hotel',
                'items': {
                    'Hotel option 2': 'Rs. XX,XXX',
                }
            },
            'Food Options': {
                'icon': 'restaurant',
                'items': {
                    'Restaurant 2': 'Rs. XX,XXX',
                    'Restaurant 3': 'Rs. XX,XXX',
                }
            },
            'Sightseeing Options': {
                'icon': 'map',
                'items': {
                    'Location 1': 'Rs. XX,XXX',
                    'Location 2': 'FREE',
                    'Location 3': 'FREE',
                }
            },
            'Activity Options': {
                'icon': 'hiking',
                'items': {
                    'Trekking': 'Rs. XX,XXX',
                }
            },
            'Transport': {
                'icon': 'commute',
                'items': {
                    'Cab Service': 'Rs. XX,XXX',
                    'Bus': 'Rs. XX,XXX',
                }
            },
        }

        for section, data in sections.items():
            icon = data['icon']
            items = data['items']

            with ui.card().classes('w-full mt-2 rounded-2xl'):
                with ui.row().classes('items-center gap-2 px-2 py-1 bg-gray-300 rounded'):
                    ui.icon(icon).classes('text-lg')
                    ui.label(section).classes('text-xl font-semibold')

                for name, price in items.items():
                    with ui.row().classes('w-full justify-between items-center rounded px-3 py-2 bg-blue-100'):
                        ui.label(name).classes('text-black')
                        ui.label(price).classes('text-black font-medium')

        bottom_nav()