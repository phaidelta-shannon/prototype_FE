from nicegui import ui
from app.components import bottom_nav, top_nav, background_image

def schedule_page():
    background_image()
    top_nav()
    with ui.column().classes('w-full max-w-3xl mx-auto mt-10 mb-20'):
        ui.label('Schedule').classes('text-3xl font-bold text-center mb-2')

        with ui.stepper().props('vertical').classes('w-full') as stepper:

            # === DAY 1 ===
            with ui.step('Day 1').classes('bg-gray-200'):
                with ui.card().classes('rounded-xl w-full shadow-md bg-white'):
                    ui.label('DAY 1').classes('w-full text-lg font-semibold text-700 px-4 bg-gray-400 rounded')

                    schedule_day1 = [
                        ('Hotel X Checkin', '10:00', 'hotel'),
                        ('Relax at the beach', '11:00', 'beach_access'),
                        ('Brunch at Restaurant X', '12:00', 'restaurant'),
                        ('Lunch at Restaurant Y', '13:30', 'lunch_dining'),
                        ('Bus to Panjim Inox', '15:00', 'directions_bus'),
                        ('Serendipity Arts Festival', '17:30', 'palette'),
                        ('Sunset at indoor stadium', '19:00', 'stadium'),
                        ('Bus to hotel', '19:30', 'directions_bus_filled'),
                        ('Dinner at Restaurant Z', '20:00', 'dinner_dining'),
                        ('Relax at beach', '21:00', 'spa'),
                    ]

                    for title, time, icon in schedule_day1:
                        with ui.row().classes('w-full items-center justify-between px-4 py-2 border-b last:border-none'):
                            with ui.row().classes('items-center gap-2'):
                                ui.icon(icon).classes('text-blue-600')
                                ui.label(title).classes('text-sm')
                            ui.label(time).classes('text-sm text-gray-500')

                with ui.stepper_navigation():
                    ui.button('Next', on_click=stepper.next)

            # === DAY 2 ===
            with ui.step('Day 2').classes('bg-gray-200'):
                with ui.card().classes('rounded-xl w-full shadow-md bg-white'):
                    ui.label('DAY 2').classes('w-full text-lg font-semibold text-700 px-4 bg-gray-400 rounded')

                    schedule_day2 = [
                        ('Breakfast at hotel', '08:30', 'free_breakfast'),
                        ('Visit local museum', '10:00', 'museum'),
                        ('Lunch at Cafe Y', '13:00', 'restaurant_menu'),
                        ('Shopping at Market', '16:00', 'store'),
                        ('Dinner at Food Plaza', '20:00', 'ramen_dining'),
                    ]

                    for title, time, icon in schedule_day2:
                        with ui.row().classes('w-full items-center justify-between px-4 py-2 border-b last:border-none'):
                            with ui.row().classes('items-center gap-2'):
                                ui.icon(icon).classes('text-blue-600')
                                ui.label(title).classes('text-sm')
                            ui.label(time).classes('text-sm text-gray-500')

                with ui.stepper_navigation():
                    ui.button('Next', on_click=stepper.next)
                    ui.button('Back', on_click=stepper.previous).props('flat')

            # === DAY 3 ===
            with ui.step('Day 3').classes('bg-gray-200'):
                with ui.card().classes('rounded-xl w-full shadow-md bg-white'):
                    ui.label('DAY 3').classes('w-full text-lg font-semibold text-700 px-4 bg-gray-400 rounded')

                    schedule_day3 = [
                        ('Check-out from Hotel', '09:00', 'logout'),
                        ('Travel to Airport', '10:00', 'flight_takeoff'),
                        ('Flight Departure', '12:00', 'airplane_ticket'),
                    ]

                    for title, time, icon in schedule_day3:
                        with ui.row().classes('w-full items-center justify-between px-4 py-2 border-b last:border-none'):
                            with ui.row().classes('items-center gap-2'):
                                ui.icon(icon).classes('text-blue-600')
                                ui.label(title).classes('text-sm')
                            ui.label(time).classes('text-sm text-gray-500')

                with ui.stepper_navigation():
                    ui.button('Back to Planner', on_click=lambda: ui.navigate.to('/planner')).classes('text-white bg-blue-600')
                    ui.button('Back', on_click=stepper.previous).props('flat')

        bottom_nav()