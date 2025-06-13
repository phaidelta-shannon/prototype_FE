from nicegui import ui
from app.components import top_nav, bottom_nav, background_image

questions = [
    {'title': 'Stay Preferences', 'options': ['Hotel', 'Hostel', 'Resort', 'Homestay', 'Camping', 'Guesthouse', 'BnB', 'Villa', 'Treehouse', 'Capsule']},
    {'title': 'Food Preferences', 'options': ['Vegetarian', 'Non-Vegetarian', 'Vegan', 'Local Cuisine', 'Street Food', 'Fine Dining', 'Fast Food', 'Seafood', 'Organic', 'Fusion']},
    {'title': 'Transport Preferences', 'options': ['Flight', 'Train', 'Bus', 'Car Rental', 'Bike Rental', 'Public Transport', 'Walking', 'Boat', 'Helicopter', 'Campervan']},
    {'title': 'Sightseeing Interests', 'options': ['Historical', 'Nature', 'Museums', 'Beaches', 'Mountains', 'Cities', 'Cultural', 'Spiritual', 'Wildlife', 'Architecture']},
    {'title': 'Activity Preferences', 'options': ['Hiking', 'Surfing', 'Skiing', 'Snorkeling', 'Shopping', 'Spa', 'Nightlife', 'Photography', 'Volunteering', 'Festivals']},
]

selected_answers = [[] for _ in questions]
current_question = {'index': 0}

def onboarding_questions_page():
    background_image()
    top_nav()
    main_column = ui.column().classes('w-full max-w-md mx-auto mt-16 items-center')

    def render_question():
        main_column.clear()
        index = current_question['index']
        q = questions[index]

        with main_column:
            ui.label('User’s Preferences').classes('text-2xl font-bold mb-2 text-black')

            # Custom horizontal multi-step progress indicator
            with ui.row().classes('w-full items-center justify-center mt-2 mb-4 gap-0'):
                for i in range(len(questions)):
                    # Circle icon
                    icon = 'check_circle' if i < index else 'radio_button_checked' if i == index else 'radio_button_unchecked'
                    color = 'text-green-500' if i < index else 'text-green-500' if i == index else 'text-gray-400'
                    ui.icon(icon).classes(f'{color} text-xl')

                    # Line connector (except after the last circle)
                    if i < len(questions) - 1:
                        ui.element('div').classes('h-0.5 w-6 bg-gray-400')


            ui.label(f'Question {index + 1} of {len(questions)}: {q["title"]}').classes('text-lg mt-3 mb-2 text-center text-black')

            with ui.grid(columns=2).classes('gap-2'):
                for opt in q['options']:
                    is_selected = opt in selected_answers[index]
                    ui.button(
                        opt,
                        on_click=lambda o=opt: toggle_option(o)
                    ).classes(
                        f'border rounded-xl text-black {"bg-green-300" if is_selected else "bg-white"}'
                    )

            # Centered button row
            with ui.row().classes('mt-4 w-full justify-center gap-4'):
                back_btn = ui.button('Back', on_click=prev_question).props('color=none').classes('bg-gray-300 text-black rounded-lg')
                if index == 0:
                    back_btn.props('disable')

                ui.button('Skip', on_click=next_question).props('color=none').classes('bg-gray-300 text-black rounded-lg')

                if index < len(questions) - 1:
                    ui.button('Next', on_click=next_question).props('color=none').classes('bg-blue-500 rounded-lg')
                else:
                    ui.button('Submit', on_click=submit_answers).props('color=none').classes('bg-green-500 rounded-lg')

    def toggle_option(option):
        index = current_question['index']
        if option in selected_answers[index]:
            selected_answers[index].remove(option)
        else:
            selected_answers[index].append(option)
        render_question()

    def next_question():
        if current_question['index'] < len(questions) - 1:
            current_question['index'] += 1
            render_question()

    def prev_question():
        if current_question['index'] > 0:
            current_question['index'] -= 1
            render_question()

    def submit_answers():
        print("Selected answers:", selected_answers)
        ui.notify('Survey submitted!', type='positive')
        ui.navigate.to('/profile')

    render_question()
    bottom_nav()