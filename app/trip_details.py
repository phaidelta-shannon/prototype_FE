from nicegui import ui
from app.components import bottom_nav, top_nav, background_image

selected_items = {}

def trip_details_page():
    background_image()
    top_nav()

    container = ui.column().classes('w-full max-w-3xl mx-auto mt-10 mb-20')

    sections = {
        'Stay Options': {
            'icon': 'hotel',
            'items': {
                'Hotel 1': 'Rs. 12,000',
                'Hotel 2': 'Rs. 10,500',
                'Hotel 3': 'Rs. 11,200',
            }
        },
        'Food Options': {
            'icon': 'restaurant',
            'items': {
                'Restaurant 1': 'Rs. 1,500',
                'Restaurant 2': 'Rs. 2,000',
            }
        },
        'Sightseeing': {
            'icon': 'map',
            'items': {
                'Location 1': 'Rs. 500',
                'Location 2': 'FREE',
            }
        },
        'Activities': {
            'icon': 'hiking',
            'items': {
                'Surfing': 'Rs. 2,500',
                'Hiking': 'FREE',
            }
        },
        'Transport': {
            'icon': 'commute',
            'items': {
                'Cab Service': 'Rs. 800',
                'Bus': 'Rs. 150',
            }
        },
        'Casino': {
            'icon': 'casino',
            'items': {
                'Casino A': 'Entry Rs. 1,000',
                'Casino B': 'Entry Rs. 1,200',
            }
        }
    }

    def render_page():
        container.clear()

        with container:
            ui.label('Trip Option 1 Details').classes('text-3xl font-bold')

            for section, data in sections.items():
                icon = data['icon']
                items = data['items']

                with ui.card().classes('w-full mt-2 rounded-2xl'):
                    with ui.row().classes('items-center gap-2 px-2 py-1 bg-gray-300 rounded'):
                        ui.icon(icon).classes('text-lg')
                        ui.label(section).classes('text-xl font-semibold')

                    for name, price in items.items():
                        is_selected = name in selected_items.get(section, set())
                        row_classes = (
                            'w-full justify-between items-center rounded px-3 py-2 cursor-pointer transition-all duration-200'
                        )
                        row_classes += ' bg-blue-200' if is_selected else ' bg-gray-200'

                        with ui.row().classes(row_classes).on('click', lambda s=section, n=name: toggle_item(s, n)):
                            ui.label(name).classes('text-black')
                            ui.label(price).classes('text-black font-medium')

            ui.button('Select this trip', on_click=lambda: ui.navigate.to('/schedule')).classes('w-full mt-4 rounded-2xl')
            bottom_nav()

    def toggle_item(section, item):
        if section not in selected_items:
            selected_items[section] = set()
        if item in selected_items[section]:
            selected_items[section].remove(item)
        else:
            selected_items[section].add(item)
        render_page()

    render_page()