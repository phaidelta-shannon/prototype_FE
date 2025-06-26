from nicegui import ui
from app.components import bottom_nav, top_nav, background_image

def trip_history_details_page():
    background_image()
    top_nav()

    trip_data = {
        'destination': 'Rajasthan',
        'date_range': '02/12/2023 – 14/12/2023',
        'total_cost': 25000,
        'num_days': 13,
        'travelers': 3,  # Only total count, no breakdown
    }

    trip_schedule = {
        'Day 1': [
            ('Hotel X Checkin', '10:00', 'hotel', 4500),
            ('Relax at beach', '11:00', 'beach_access', 0),
            ('Brunch at Restaurant X', '12:00', 'restaurant', 1200),
            ('Lunch at Restaurant Y', '13:30', 'lunch_dining', 1000),
            ('Bus to Panjim Inox', '15:00', 'directions_bus', 300),
            ('Serendipity Arts Festival', '17:30', 'palette', 2000),
            ('Sunset at indoor stadium', '19:00', 'stadium', 250),
            ('Bus to hotel', '19:30', 'directions_bus_filled', 300),
            ('Dinner at Restaurant Z', '20:00', 'dinner_dining', 1800),
            ('Relax at beach', '21:00', 'spa', 100),
        ],
        'Day 2': [
            ('Breakfast at hotel', '08:30', 'free_breakfast', 0),
            ('Visit local museum', '10:00', 'museum', 500),
            ('Lunch at Cafe Y', '13:00', 'restaurant_menu', 950),
            ('Shopping at Market', '16:00', 'store', 1200),
            ('Dinner at Food Plaza', '20:00', 'ramen_dining', 1300),
        ]
    }

    with ui.column().classes('w-full max-w-3xl mx-auto mt-16 mb-20 items-center'):

        ui.label(trip_data['destination']).classes('text-3xl font-bold')
        ui.label(trip_data['date_range']).classes('text-md text-gray-600 mb-2')

        with ui.row().classes('w-full').style('gap: 12px;'):
            card_classes = 'flex-1 bg-white/60 rounded-xl text-center flex flex-col items-center justify-center h-24'
            with ui.card().classes(card_classes):
                ui.label('Total Cost').classes('text-sm text-gray-500')
                ui.label(f"₹{trip_data['total_cost']:,}").classes('text-xl font-semibold')

            with ui.card().classes(card_classes):
                ui.label('Duration').classes('text-sm text-gray-500')
                ui.label(f"{trip_data['num_days']} Days").classes('text-xl font-semibold')

            with ui.card().classes(card_classes):
                ui.label('Travelers').classes('text-sm text-gray-500')
                ui.label(f"{trip_data['travelers']} People").classes('text-xl font-semibold')

        for i, (day, events) in enumerate(trip_schedule.items()):
            mb_class = 'mb-20' if i == len(trip_schedule) - 1 else 'mb-2'
            with ui.card().classes(f'rounded-xl w-full backdrop-blur-sm bg-white/40 {mb_class}'):
                with ui.row().classes('items-center gap-2'):
                    ui.icon('check_circle', color='green')
                    ui.label(day.upper()).classes('font-semibold text-lg')

                for title, time, icon, price in events:
                    with ui.row().classes('w-full items-center justify-between bg-white px-4 py-3 rounded'):
                        with ui.row().classes('items-center gap-2 overflow-hidden'):
                            ui.icon(icon).classes('text-blue-600')
                            ui.label(title).classes('text-sm truncate max-w-[160px] md:max-w-[300px]')
                        with ui.row().classes('items-center gap-6'):
                            ui.label(f"₹{price:,}" if price else 'FREE').classes('text-sm text-gray-600')
                            ui.label(time).classes('text-sm text-gray-500')

        bottom_nav()