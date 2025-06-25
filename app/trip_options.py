from nicegui import ui
from app.components import bottom_nav, top_nav, background_image

# Extracted hardcoded trip options — this will later come from FastAPI
trip_options = [
    {
        "title": "Trip Option 1",
        "summary": "A ... B ... C ... D ...",
        "budget": 25000
    },
    {
        "title": "Trip Option 2",
        "summary": "A ... B ... C ... D ...",
        "budget": 32000
    },
    {
        "title": "Trip Option 3",
        "summary": "A ... B ... C ... D ...",
        "budget": 44000
    },
    {
        "title": "Trip Option 4",
        "summary": "A ... B ... C ... D ...",
        "budget": 50000
    }
]

def trip_options_page():
    background_image()
    top_nav()
    with ui.column().classes('w-full max-w-4xl mx-auto mt-10 mb-20'):
        ui.label('Trip Results').classes('text-3xl font-bold')
        
        for option in trip_options:
            with ui.card().classes('w-full mb-2 rounded-2xl'):
                ui.label(option["title"]).classes('w-full text-xl font-semibold bg-gray-400 rounded')
                ui.label(option["summary"])
                ui.label(f'Total Budget: Rs. {option["budget"]:,}')
                ui.button('View Details', on_click=lambda: ui.navigate.to('/trip_schedule')).classes('rounded-lg')

        bottom_nav()