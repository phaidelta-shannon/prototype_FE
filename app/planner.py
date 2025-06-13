from nicegui import ui
from app.components import bottom_nav, top_nav, background_image

def parse_date_range(inp: str):
    start_date, _sep, end_date = inp.partition(" - ")
    if _sep == "":
        return
    return {
        "from": start_date.strip(),
        "to": end_date.strip(),
    }

def planner_page():
    background_image()
    top_nav()
    with ui.column().classes('w-full max-w-4xl mx-auto mt-16'):
        ui.label('Plan Your Trip').classes('text-3xl font-bold')
        
        # Destination input with map icon
        with ui.card().classes('w-full rounded-2xl'):
            options = ["Goa", "Hyderabad", "Singapore"]
            with ui.input(
                label="Destination",
                placeholder="Country, City, Landmark...",
                # autocomplete=options,  # Uncomment when supported
            ).classes('w-full') as destination:
                with destination.add_slot("append"):
                    ui.icon("search").on(
                        "click", lambda: ui.notify("TODO: Show a map to choose.")
                    ).classes("cursor-pointer")
        
        # Date Range Card (Replacing start/end cards)
        with ui.card().classes('mt-4 w-full rounded-2xl'):
            ui.label("Duration")

            with ui.input("Select date range").classes("w-full") as date_range:
                with ui.menu().props("no-parent-event") as menu:
                    with ui.date().props("range").bind_value(
                        date_range,
                        forward=lambda x: f'{x["from"]} - {x["to"]}' if x else None,
                        backward=parse_date_range,
                    ):
                        # "Done" button
                        with ui.row().classes("justify-end"):
                            ui.button("Done", on_click=menu.close).props("flat")

                # Calendar icon trigger
                with date_range.add_slot("append"):
                    ui.icon("edit_calendar").on("click", menu.open).classes("cursor-pointer")

        currency_symbol = 'Rs. '

        with ui.card().classes('mt-4 w-full rounded-2xl'):
            ui.label(f"Budget Range")
            budget_range = ui.range(min=1000, max=100000, step=1000, value={"min": 20000, "max": 50000})
            
            ui.label().bind_text_from(
                budget_range,
                'value',
                backward=lambda v: f"{currency_symbol}{v['min']:,.0f} - {currency_symbol}{v['max']:,.0f}"
            )
        
        with ui.card().classes('mt-4 w-full rounded-2xl'):
            ui.label('Trip Type').classes('w-full')

            with ui.row().classes('w-full justify-evenly'):
                ui.radio(
                    {'solo': 'Solo', 'family': 'Family', 'friends': 'Friends'},
                    value='solo'
                ).props('inline flat').classes('w-full')

        ui.button('Find Best Results', on_click=lambda: ui.navigate.to('/trip-options')).classes('mt-4 w-full rounded-2xl mb-20')
        bottom_nav()