from nicegui import ui

def top_nav():
    with ui.row().classes('w-full fixed top-0 left-0 right-0 z-50 bg-blue-400 shadow py-2'):
        with ui.button(icon='menu').classes('ml-2'):
            with ui.menu() as menu:
                ui.menu_item('Plan Trip', on_click=lambda: ui.navigate.to('/planner'))
                ui.menu_item('Trip History', on_click=lambda: ui.navigate.to('/history'))
                ui.menu_item('Schedule', on_click=lambda: ui.navigate.to('/schedule'))
                ui.menu_item('User Profile', on_click=lambda: ui.navigate.to('/profile'))
                ui.separator()
                ui.menu_item('Close', menu.close)
        result = ui.label('Trip PLanner').classes('text-2xl font-bold')

def bottom_nav():
    with ui.row().classes('fixed bottom-0 left-0 right-0 justify-around bg-blue-400 shadow py-2'):
        ui.button(icon='flight', on_click=lambda: ui.navigate.to('/planner')).props('flat').classes('text-white')
        ui.button(icon='watch', on_click=lambda: ui.navigate.to('/history')).props('flat').classes('text-white')
        ui.button(icon='favorite_border', on_click=lambda: ui.notify('Feature coming soon')).props('flat').classes('text-white')
        ui.button(icon='person', on_click=lambda: ui.navigate.to('/profile')).props('flat').classes('text-white')

def background_image():
    # This creates a full-screen background image container behind all other UI
    ui.add_head_html('''
    <style>
    .bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: url("/static/background_4.png") no-repeat center center fixed;
        background-size: cover;
        z-index: -1;
    }
    </style>
    ''')
    ui.html('<div class="bg"></div>')