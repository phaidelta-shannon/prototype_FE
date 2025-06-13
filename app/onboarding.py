from nicegui import ui
from app.components import bottom_nav, top_nav, background_image

def onboarding_page():
    background_image()
    top_nav()
    with ui.column().classes('w-full max-w-2xl mx-auto mt-20 items-center'):
        ui.label('Welcome User!').classes('text-2xl font-bold')
        ui.label('Let\'s curate your preferences')
        ui.image('https://cdn-icons-png.flaticon.com/512/8608/8608769.png').classes('w-48')
        ui.button('Begin', on_click=lambda: ui.navigate.to('/onboarding-questions')).classes('mt-4 w-1/3 rounded-2xl')
        ui.button('Skip', on_click=lambda: ui.navigate.to('/planner')).classes('mt-2 w-1/3 rounded-2xl')
        bottom_nav()