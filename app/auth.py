from nicegui import ui
from app.components import background_image

def login_page():
    background_image()
    with ui.column().classes('w-full max-w-lg mx-auto mt-20 items-center'):
        ui.label('Login').classes('text-3xl font-bold mb-4')
        ui.input('Email').classes('w-full')
        ui.input('Password', password=True).classes('w-full')
        ui.button('Submit', on_click=lambda: ui.navigate.to('/onboarding')).classes('mt-4 w-full rounded-2xl')
        ui.button('New here? Sign Up', on_click=lambda: ui.navigate.to('/signup')).classes('mt-2 w-full rounded-2xl')

def signup_page():
    background_image()
    with ui.column().classes('w-full max-w-lg mx-auto mt-20 items-center'):
        ui.label('Create Account').classes('text-3xl font-bold mb-4')
        ui.input('First Name').classes('w-full')
        ui.input('Last Name').classes('w-full')
        ui.input('Email').classes('w-full')
        ui.input('Password', password=True).classes('w-full')
        ui.button('Sign Up', on_click=lambda: ui.navigate.to('/onboarding')).classes('mt-4 w-full rounded-2xl')
        ui.button('Already registered? Login here', on_click=lambda: ui.navigate.to('/')).classes('mt-2 w-full rounded-2xl')

def guest_page():
    background_image()

    with ui.column().classes('w-full max-w-lg mx-auto mt-44 items-center gap-4'):
        ui.label('Browse as Guest').classes('text-3xl font-bold text-center')
        ui.label('Explore available trips, experiences, and itineraries without logging in.').classes('text-center')
        ui.button('Start Browsing', on_click=lambda: ui.navigate.to('/planner')) \
            .classes('w-full bg-blue-500 text-white rounded-xl py-2 font-semibold')