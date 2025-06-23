from nicegui import ui, app  # app is used for static files

# Serve the static folder for bckg img
app.add_static_files('/static', 'static')  # CORRECT for v2.19.0

# your existing page routes
from app.auth import login_page, signup_page
from app.onboarding import onboarding_page
from app.onboarding_questions import onboarding_questions_page
from app.planner import planner_page
from app.trip_options import trip_options_page
from app.trip_details import trip_details_page
from app.profile import profile_page
from app.schedule import schedule_page
from app.trip_schedule import trip_schedule_page
from app.history import history_page
from app.trip_history_details_page import trip_history_details_page

def route():
    ui.page('/')(login_page)
    ui.page('/signup')(signup_page)
    ui.page('/onboarding')(onboarding_page)
    ui.page('/onboarding-questions')(onboarding_questions_page)
    ui.page('/profile')(profile_page)
    ui.page('/planner')(planner_page)
    ui.page('/trip-options')(trip_options_page)
    ui.page('/trip-details')(trip_details_page)
    ui.page('/schedule')(schedule_page)
    ui.page('/trip_schedule')(trip_schedule_page)
    ui.page('/history')(history_page)
    ui.page('/trip-history-details')(trip_history_details_page)

route()
ui.run(title="Trip Planner", reload=True)