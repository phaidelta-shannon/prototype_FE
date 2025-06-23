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

    with ui.column().classes('w-full max-w-4xl mx-auto mt-12'):
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

                if value == 'family':
                    num_travelers.props('readonly')
                    update_total_travelers()
                else:
                    num_travelers.props(remove='readonly')

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
                num_travelers = ui.number(label='Number of Travelers', min=1, value=2).classes('w-full')

            family_section = ui.column().classes('w-full')
            with family_section:
                num_adults = ui.number(label='Number of Adults', min=1, value=2).classes('w-full')
                num_children = ui.number(label='Number of Children (2-11 yrs)', min=0, value=0).classes('w-full')
                num_infants = ui.number(label='Number of Infants (Under 2 yrs)', min=0, value=0).classes('w-full')

            def update_total_travelers():
                a = num_adults.value or 0
                c = num_children.value or 0
                i = num_infants.value or 0
                total = a + c + i
                num_travelers.value = total
                num_travelers.update()

            num_adults.on('blur', lambda _: update_total_travelers())
            num_children.on('blur', lambda _: update_total_travelers())
            num_infants.on('blur', lambda _: update_total_travelers())

            # Ensures correct visibility for solo on first load
            update_sections('solo')

        # Collapsible Preferences Section
        with ui.expansion('Trip Preferences (optional)').classes('mt-2 w-full rounded-2xl backdrop-blur-sm bg-white/40'):
            preferences_column = ui.column().classes('w-full items-center')
            
            embedded_questions = [
                {'title': 'Stay Preferences', 'options': ['Hotel', 'Hostel', 'Resort', 'Homestay', 'Camping', 'Guesthouse', 'BnB', 'Villa', 'Treehouse', 'Capsule']},
                {'title': 'Food Preferences', 'options': ['Vegetarian', 'Non-Vegetarian', 'Vegan', 'Local Cuisine', 'Street Food', 'Fine Dining', 'Fast Food', 'Seafood', 'Organic', 'Fusion']},
                {'title': 'Transport Preferences', 'options': ['Flight', 'Train', 'Bus', 'Car Rental', 'Bike Rental', 'Public Transport', 'Walking', 'Boat', 'Helicopter', 'Campervan']},
                {'title': 'Sightseeing Interests', 'options': ['Historical', 'Nature', 'Museums', 'Beaches', 'Mountains', 'Cities', 'Cultural', 'Spiritual', 'Wildlife', 'Architecture']},
                {'title': 'Activity Preferences', 'options': ['Hiking', 'Surfing', 'Skiing', 'Snorkeling', 'Shopping', 'Spa', 'Nightlife', 'Photography', 'Volunteering', 'Festivals']},
            ]
            embedded_selected_answers = [[] for _ in embedded_questions]
            embedded_index = {'i': 0}

            def render_embedded_question():
                preferences_column.clear()
                q_index = embedded_index['i']
                q = embedded_questions[q_index]

                preferences_column.clear()
                with preferences_column:
                    ui.label(f'Q{q_index + 1}/{len(embedded_questions)}: {q["title"]}').classes('text-lg font-medium mt-2 mb-2')

                    with ui.grid(columns=2).classes('gap-2'):
                        for opt in q['options']:
                            is_selected = opt in embedded_selected_answers[q_index]
                            ui.button(
                                opt,
                                on_click=lambda o=opt: toggle_embedded_option(o)
                            ).classes(
                                f'border rounded-xl text-black {"bg-green-300" if is_selected else "bg-white"}'
                            )

                    with ui.row().classes('mt-4 w-full justify-center gap-4'):
                        back_btn = ui.button('Back', on_click=embedded_prev_question).props('color=none').classes('bg-gray-300 text-black rounded-lg')
                        if q_index == 0:
                            back_btn.props('disable')

                        ui.button('Skip', on_click=embedded_next_question).props('color=none').classes('bg-gray-300 text-black rounded-lg')

                        if q_index < len(embedded_questions) - 1:
                            ui.button('Next', on_click=embedded_next_question).classes('bg-blue-500 text-white rounded-lg')
                        else:
                            ui.button('Submit', on_click=submit_embedded_answers).props('color=none').classes('bg-green-400 text-white rounded-lg')

            def toggle_embedded_option(option):
                q_index = embedded_index['i']
                if option in embedded_selected_answers[q_index]:
                    embedded_selected_answers[q_index].remove(option)
                else:
                    embedded_selected_answers[q_index].append(option)
                render_embedded_question()

            def embedded_next_question():
                if embedded_index['i'] < len(embedded_questions) - 1:
                    embedded_index['i'] += 1
                    render_embedded_question()

            def embedded_prev_question():
                if embedded_index['i'] > 0:
                    embedded_index['i'] -= 1
                    render_embedded_question()

            def submit_embedded_answers():
                ui.notify('Preferences saved!', type='positive')
                print('Saved preferences:', embedded_selected_answers)

            render_embedded_question()

        # Submit
        ui.button('Find Best Results', on_click=lambda: ui.navigate.to('/trip-options')).classes('mt-4 w-full rounded-2xl mb-20')

        bottom_nav()