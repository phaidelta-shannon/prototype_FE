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

        # Destination input
        with ui.card().classes('w-full rounded-2xl'):
            options = ["Goa", "Hyderabad", "Singapore"]
            with ui.input(
                label="Destination",
                placeholder="Country, City, Landmark...",
            ).classes('w-full') as destination:
                with destination.add_slot("append"):
                    ui.icon("search").on(
                        "click", lambda: ui.notify("TODO: Show a map to choose.")
                    ).classes("cursor-pointer")

        # Date range input
        with ui.card().classes('mt-2 w-full rounded-2xl'):
            with ui.input("Duration").classes("w-full") as date_range:
                with ui.menu().props("no-parent-event") as menu:
                    with ui.date().props("range").bind_value(
                        date_range,
                        forward=lambda x: f'{x["from"]} - {x["to"]}' if x else None,
                        backward=parse_date_range,
                    ):
                        with ui.row().classes("justify-end"):
                            ui.button("Done", on_click=menu.close).props("flat")
                with date_range.add_slot("append"):
                    ui.icon("edit_calendar").on("click", menu.open).classes("cursor-pointer")

        # Budget range
        currency_symbol = 'Rs. '
        with ui.card().classes('mt-2 w-full rounded-2xl'):
            ui.label("Budget Range")
            budget_range = ui.range(min=1000, max=100000, step=1000, value={"min": 20000, "max": 50000})
            ui.label().bind_text_from(
                budget_range,
                'value',
                backward=lambda v: f"{currency_symbol}{v['min']:,.0f} - {currency_symbol}{v['max']:,.0f}"
            )

        # Trip Type & dynamic travelers
        with ui.card().classes('mt-2 w-full rounded-2xl'):
            ui.label('Trip Type').classes('w-full')

            def update_sections(value):
                group_section.visible = value != 'solo'
                family_section.visible = value == 'family'

            # Note: This is not reactive binding — an `on_change` event handler on the radio input is used to manually toggle visibility of other UI sections (group and family travelers).
            # The `update_sections()` function handles this logic.
            # Since NiceGUI doesn't auto-trigger on_change on load, we also call it manually once to ensure the correct sections are visible at first render.

            trip_type = 'solo'
            ui.radio(
                {'solo': 'Solo', 'family': 'Family', 'friends': 'Friends'},
                value=trip_type,
                on_change=lambda e: update_sections(e.value)
            ).props('inline flat').classes('w-full')

            group_section = ui.column().classes('w-full mt-2')
            with group_section:
                ui.number(label='Number of Travelers', min=1, value=2).classes('w-full')

            family_section = ui.column().classes('w-full')
            with family_section:
                ui.number(label='Number of Children (2-11 yrs)', min=0, value=0).classes('w-full')
                ui.number(label='Number of Infants (Under 2 yrs)', min=0, value=0).classes('w-full')

            # Ensures correct visibility for solo on first load
            update_sections('solo')

        # Submit
        ui.button('Find Best Results', on_click=lambda: ui.navigate.to('/trip-options')).classes('mt-4 w-full rounded-2xl mb-20')

        bottom_nav()