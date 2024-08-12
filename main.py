import sqlite3
import googlemaps
from datetime import datetime, timedelta

# Directly assign the API key (for development only)
API_KEY = "ENTERKEYHERE"

if not API_KEY:
    raise ValueError("API key not found. Ensure the environment variable is set.")
else:
    # Print the API key to verify it is set correctly (Remove this in production)
    print("API Key found:", API_KEY)

# Initialize the Google Maps client with the API key directly
gmaps = googlemaps.Client(key=API_KEY)

class User:
    def __init__(self, hobbies, date_of_birth, dietary_restrictions=None,
                 disabilities=None, travel_dates=None, budget=None, current_location=None):
        self.hobbies = hobbies
        self.date_of_birth = date_of_birth
        self.dietary_restrictions = dietary_restrictions
        self.disabilities = disabilities
        self.travel_dates = travel_dates
        self.current_location = current_location
        self.budget = budget

def get_location_from_google_maps(address):
    try:
        geocode_result = gmaps.geocode(address)
        if geocode_result and "South Korea" in geocode_result[0]['formatted_address']:
            print(geocode_result[0]['formatted_address'])
            return geocode_result[0]['formatted_address']
        else:
            print("The address is not in South Korea. Please provide a valid address in South Korea.")
    except Exception as e:
        print(f"Error occurred while trying to geocode the address: {e}")
    return None

def get_user_location():
    while True:
        address = input("Please enter the full address of your stay: ").strip()
        location = get_location_from_google_maps(address)
        if location:
            return location
        print(f"Invalid address entered: {address}")
        print("Please enter a valid address in South Korea.")

def prompt_for_trip_details(user):
    def get_valid_date(prompt):
        while True:
            date_str = input(prompt).strip()
            try:
                date_obj = datetime.strptime(date_str, "%d/%m/%y")
                if date_obj < datetime.now():
                    print("The date cannot be in the past. Please enter a future date.")
                elif date_obj > datetime.now() + timedelta(days=60):
                    print("The algorithm works best on journeys within two months from now. Please run this again when you are closer to your journey.")
                else:
                    return date_str, date_obj
            except ValueError:
                print("Invalid date format. Please enter the date in dd/mm/yy format.")

    start_date_str, start_date = get_valid_date("Enter the start date of your trip (dd/mm/yy): ")

    end_date_str, end_date = get_valid_date("Enter the end date of your trip (dd/mm/yy): ")

    while end_date < start_date:
        print("The end date cannot be before the start date. Please enter a valid end date.")
        end_date_str, end_date = get_valid_date("Enter the end date of your trip (dd/mm/yy): ")

    trip_duration = end_date - start_date
    if trip_duration > timedelta(weeks=1):
        print("Warning: Our algorithm works best for trips under one week. For trips longer than a week, you might consider generating another request for each week of your stay.")
    user.travel_dates = (start_date_str, end_date_str)

    if not user.current_location:
        user.current_location = get_user_location()

    while True:
        try:
            user.budget = int(input("What's your budget for activities for your stay? (KRW): ").strip())
            break
        except ValueError:
            print("Please enter a valid integer for the budget.")

def fetch_hobbies_from_db(hobby_list):
    conn = sqlite3.connect('hobbies.db')
    cursor = conn.cursor()
    hobbies = {}
    missing_hobbies = []

    for hobby in hobby_list:
        cursor.execute("SELECT l.location FROM hobbies h JOIN locations l ON h.id = l.hobby_id WHERE h.name = ?", (hobby,))
        locations = cursor.fetchall()
        if locations:
            hobbies[hobby] = ", ".join([loc[0] for loc in locations])
        else:
            missing_hobbies.append(hobby)

    conn.close()
    if missing_hobbies:
        print(f"The following hobbies do not exist in the database: {', '.join(missing_hobbies)}")
        return None
    return hobbies

def validate_dietary_restrictions_and_disabilities(dietary_restrictions, disabilities):
    
    valid_dietary_restrictions = [
        "None", "Halal", "Kosher", "Vegan", "Vegetarian", "Nut allergy", "Gluten-free",
        "Dairy-free", "Lactose intolerant", "Shellfish allergy", "Soy allergy", 
        "Egg allergy", "Seafood allergy", "Low-sodium", "Low-carb", "Low-fat", 
        "Diabetic", "No pork", "Pescatarian", "Paleo", "Keto", "FODMAP", 
        "Organic only", "Peanut allergy", "Citrus allergy", "Sulfite allergy", 
        "Fructose intolerance", "MSG sensitivity", "Raw food diet", 
        "Nightshade allergy"
    ]

    valid_disabilities = [
        "None", "Wheelchair user", "Visual impairment", "Hearing impairment", 
        "Cognitive disability", "Autism", "Dyslexia", "ADHD", 
        "Mobility impairment", "Chronic pain", "Mental health condition", 
        "Speech impairment", "Chronic illness", "Epilepsy", "Alzheimer's disease", 
        "Parkinson's disease", "Down syndrome", "Spinal cord injury", 
        "Cerebral palsy", "Muscular dystrophy", "Multiple sclerosis"
    ]


    invalid_dietary = [restriction for restriction in dietary_restrictions if restriction not in valid_dietary_restrictions]
    invalid_disabilities = [disability for disability in disabilities if disability not in valid_disabilities]

    if invalid_dietary:
        print(f"Invalid dietary restrictions: {', '.join(invalid_dietary)}. Please provide valid dietary restrictions.")
        return False
    if invalid_disabilities:
        print(f"Invalid disabilities: {', '.join(invalid_disabilities)}. Please provide valid disabilities.")
        return False

    return True

def generate_prompt(user):
    clause = []

    if user.date_of_birth == datetime.now().strftime("%d/%m/%y"):
        clause.append("It's the user's birthday today, so add an appropriate birthday venue activity.")

    if user.dietary_restrictions:
        clause.append(
            f"The user has dietary restrictions: {', '.join(user.dietary_restrictions)}. Recommend only places that meet these criteria for food and activities.")

    if user.disabilities:
        clause.append(
            f"The user has disabilities: {', '.join(user.disabilities)}. Ensure that recommended places are accessible.")

    if user.budget:
        clause.append(f"The user has a budget of {user.budget} KRW. Make sure the total costs of activities shown do not go above this.")

    clause.append("Only recommend places in South Korea.")

    hobbies_str = "; ".join([f"{hobby}: {details}" for hobby, details in user.hobbies.items()])
    prompt = (
        f"User Information:\n"
        f"- Hobbies: {hobbies_str}\n"
        f"- Dietary Restrictions: {', '.join(user.dietary_restrictions) if user.dietary_restrictions else 'None'}\n"
        f"- Disabilities: {', '.join(user.disabilities) if user.disabilities else 'None'}\n"
        f"\n"
        f"Travel Information:\n"
        f"- Current Location: {user.current_location}, South Korea\n"
        f"- Travel Dates: {user.travel_dates[0]} to {user.travel_dates[1]}\n"
        f"- Budget: {user.budget} KRW\n"
        f"\n"
        f"Request:\n"
        f"Recommend a minimum of 10 places for the user near {user.current_location} to visit. "
        f"Consider the user's hobbies and recent headlines or trends from the internet related to the area, ensure recommendations are age-appropriate to the users age. "
        f"{' '.join(clause)}"
    )

    return prompt

user_data = User(
    hobbies=["Swimming", "Running", "Art", "History", "Gaming"],
    date_of_birth="31/07/24",
    dietary_restrictions=["Halal", "Nut allergy"],
    disabilities=["Wheelchair user"],
)

if validate_dietary_restrictions_and_disabilities(user_data.dietary_restrictions, user_data.disabilities):
    user_data.hobbies = fetch_hobbies_from_db(user_data.hobbies)

    if user_data.hobbies:
        prompt_for_trip_details(user_data)
        if user_data.travel_dates and user_data.current_location and user_data.budget:
            prompt = generate_prompt(user_data)
            print(prompt)
        else:
            print("Could not generate prompt due to missing or invalid data.")
    else:
        print("User hobbies validation failed.")
else:
    print("Validation of dietary restrictions or disabilities failed.")




