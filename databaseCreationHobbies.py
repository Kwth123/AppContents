#THIS FILE DOESNT NEED TO BE RAN, ITS JUST CREATING THE DATABASE OF HOBBIES WITH LOCATIONS RUN main.py


import sqlite3

# Connect to SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('hobbies.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS hobbies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS locations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hobby_id INTEGER NOT NULL,
    location TEXT NOT NULL,
    FOREIGN KEY (hobby_id) REFERENCES hobbies(id)
)
''')

# Insert hobbies
hobbies = [
    'Swimming', 'Running', 'Art', 'History', 'Gaming', 'Cycling', 'Hiking', 'Cooking', 'Photography',
    'Yoga', 'Dancing', 'Fishing', 'Bird Watching', 'Gardening', 'Traveling', 'Writing', 'Reading',
    'Music', 'Fitness', 'Rock Climbing', 'Skiing', 'Snowboarding', 'Surfing', 'Scuba Diving', 'Martial Arts',
    'Pottery', 'Woodworking', 'Knitting', 'Baking', 'Tennis', 'Basketball', 'Soccer', 'Volleyball',
    'Table Tennis', 'Archery', 'Horse Riding', 'Camping', 'Astronomy', 'Chess', 'Golf', 'Geocaching',
    'Kite Flying', 'Origami', 'Model Building', 'Drone Flying', 'Sailing', 'Kayaking', 'Canoeing',
    'Wine Tasting', 'Astrology', 'Meditation', 'Calligraphy', 'Magic Tricks', 'Scrapbooking',
    'Metal Detecting', 'Juggling', 'Parkour', 'Bowling', 'Lacrosse', 'Rugby', 'Fencing', 'Ice Skating',
    'BMX Riding', 'Roller Skating', 'Stand-Up Comedy', 'Beer Brewing', 'Cheese Making', 'Soap Making'
]

for hobby in hobbies:
    cursor.execute('INSERT INTO hobbies (name) VALUES (?)', (hobby,))

# Insert locations
locations = {
    'Swimming': ['Water Parks', 'Open Water', 'Swimming Pools', 'Beaches'],
    'Running': ['Stadiums', 'Running Tracks', 'Parks', 'Trails', 'Urban Areas'],
    'Art': ['Museums', 'Art Galleries', 'Art Studios', 'Street Art Locations'],
    'History': ['Museums', 'Historical Sites', 'Monuments', 'Ancient Ruins'],
    'Gaming': ['Internet Cafes', 'Gaming Studio Tours', 'Arcades', 'Esports Arenas'],
    'Cycling': ['Cycling Paths', 'Mountain Trails', 'City Roads', 'Scenic Routes'],
    'Hiking': ['Mountain Trails', 'National Parks', 'Forests', 'Coastal Trails'],
    'Cooking': ['Cooking Classes', 'Food Festivals', 'Restaurants', 'Local Markets'],
    'Photography': ['Nature Reserves', 'Urban Areas', 'Landmarks', 'Scenic Overlooks'],
    'Yoga': ['Yoga Studios', 'Parks', 'Retreat Centers', 'Beaches'],
    'Dancing': ['Dance Studios', 'Clubs', 'Cultural Festivals', 'Dance Halls'],
    'Fishing': ['Lakes', 'Rivers', 'Fishing Ponds', 'Coastal Areas'],
    'Bird Watching': ['Nature Reserves', 'Parks', 'Wetlands', 'Bird Sanctuaries'],
    'Gardening': ['Botanical Gardens', 'Community Gardens', 'Home Gardens', 'Garden Tours'],
    'Traveling': ['Tourist Attractions', 'Beaches', 'Mountains', 'Cultural Landmarks'],
    'Writing': ['Libraries', 'Cafes', 'Writing Workshops', 'Inspirational Locations'],
    'Reading': ['Libraries', 'Bookstores', 'Reading Clubs', 'Quiet Parks'],
    'Music': ['Concert Halls', 'Music Festivals', 'Music Studios', 'Live Music Venues'],
    'Fitness': ['Gyms', 'Fitness Centers', 'Parks', 'Outdoor Workout Areas'],
    'Rock Climbing': ['Climbing Gyms', 'Rock Faces', 'Bouldering Areas', 'Mountain Ranges'],
    'Skiing': ['Ski Resorts', 'Mountain Slopes', 'Winter Parks', 'Backcountry Areas'],
    'Snowboarding': ['Ski Resorts', 'Mountain Slopes', 'Winter Parks', 'Snowboarding Parks'],
    'Surfing': ['Beaches', 'Surf Schools', 'Surf Competitions', 'Famous Surf Spots'],
    'Scuba Diving': ['Coral Reefs', 'Diving Schools', 'Underwater Parks', 'Shipwreck Sites'],
    'Martial Arts': ['Dojo', 'Martial Arts Schools', 'Fitness Centers', 'Martial Arts Camps'],
    'Pottery': ['Pottery Studios', 'Art Centers', 'Craft Shops', 'Pottery Classes'],
    'Woodworking': ['Woodshops', 'Craft Centers', 'DIY Workshops', 'Woodworking Schools'],
    'Knitting': ['Craft Stores', 'Knitting Groups', 'Community Centers', 'Knitting Cafes'],
    'Baking': ['Bakeries', 'Cooking Schools', 'Home Kitchens', 'Baking Classes'],
    'Tennis': ['Tennis Courts', 'Sports Centers', 'Country Clubs', 'Tennis Resorts'],
    'Basketball': ['Basketball Courts', 'Sports Centers', 'Parks', 'Recreational Facilities'],
    'Soccer': ['Soccer Fields', 'Stadiums', 'Sports Complexes', 'Soccer Camps'],
    'Volleyball': ['Volleyball Courts', 'Beaches', 'Sports Centers', 'Beach Volleyball Courts'],
    'Table Tennis': ['Table Tennis Clubs', 'Sports Centers', 'Recreation Rooms', 'Table Tennis Halls'],
    'Archery': ['Archery Ranges', 'Sports Clubs', 'Outdoor Parks', 'Archery Competitions'],
    'Horse Riding': ['Stables', 'Riding Schools', 'Countryside Trails', 'Equestrian Centers'],
    'Camping': ['Campgrounds', 'National Parks', 'Forest Reserves', 'Wilderness Areas'],
    'Astronomy': ['Observatories', 'Planetariums', 'Dark Sky Parks', 'Astronomy Clubs'],
    'Chess': ['Chess Clubs', 'Libraries', 'Parks', 'Chess Tournaments'],
    'Golf': ['Golf Courses', 'Driving Ranges', 'Country Clubs', 'Golf Resorts'],
    'Geocaching': ['Parks', 'Urban Areas', 'Nature Reserves', 'Historical Sites'],
    'Kite Flying': ['Beaches', 'Parks', 'Open Fields', 'Kite Festivals'],
    'Origami': ['Craft Stores', 'Community Centers', 'Art Classes', 'Origami Exhibitions'],
    'Model Building': ['Hobby Shops', 'Community Centers', 'Home Workshops', 'Model Exhibitions'],
    'Drone Flying': ['Open Fields', 'Parks', 'Drone Racing Tracks', 'Scenic Areas'],
    'Sailing': ['Marinas', 'Yacht Clubs', 'Lakes', 'Coastal Waters'],
    'Kayaking': ['Rivers', 'Lakes', 'Coastal Waters', 'Kayak Tours'],
    'Canoeing': ['Rivers', 'Lakes', 'Parks', 'Canoe Trails'],
    'Wine Tasting': ['Vineyards', 'Wine Festivals', 'Wine Bars', 'Wine Regions'],
    'Astrology': ['Observatories', 'Astrology Retreats', 'Planetariums', 'Astrology Workshops'],
    'Meditation': ['Meditation Centers', 'Parks', 'Retreat Centers', 'Temples'],
    'Calligraphy': ['Art Studios', 'Workshops', 'Craft Stores', 'Calligraphy Exhibitions'],
    'Magic Tricks': ['Magic Shops', 'Theaters', 'Magic Shows', 'Magic Conventions'],
    'Scrapbooking': ['Craft Stores', 'Workshops', 'Community Centers', 'Scrapbooking Clubs'],
    'Metal Detecting': ['Beaches', 'Historical Sites', 'Parks', 'Open Fields'],
    'Juggling': ['Circus Schools', 'Parks', 'Performance Spaces', 'Juggling Conventions'],
    'Parkour': ['Urban Areas', 'Parkour Gyms', 'Parks', 'Parkour Competitions'],
    'Bowling': ['Bowling Alleys', 'Recreation Centers', 'Sports Complexes', 'Bowling Tournaments'],
    'Lacrosse': ['Lacrosse Fields', 'Sports Complexes', 'Schools', 'Lacrosse Camps'],
    'Rugby': ['Rugby Fields', 'Sports Complexes', 'Stadiums', 'Rugby Clubs'],
    'Fencing': ['Fencing Clubs', 'Sports Centers', 'Schools', 'Fencing Tournaments'],
    'Ice Skating': ['Ice Rinks', 'Sports Centers', 'Winter Parks', 'Ice Skating Shows'],
    'BMX Riding': ['BMX Parks', 'Urban Areas', 'Trails', 'BMX Competitions'],
    'Roller Skating': ['Skating Rinks', 'Parks', 'Urban Areas', 'Roller Derby Events'],
    'Stand-Up Comedy': ['Comedy Clubs', 'Theaters', 'Festivals', 'Open Mic Nights'],
    'Beer Brewing': ['Breweries', 'Beer Festivals', 'Home Brewing Clubs', 'Brewing Classes'],
    'Cheese Making': ['Dairies', 'Cheese Festivals', 'Culinary Schools', 'Cheese Tasting Events'],
    'Soap Making': ['Craft Stores', 'Workshops', 'Community Centers', 'Soap Making Classes']
}

for hobby, loc_list in locations.items():
    cursor.execute('SELECT id FROM hobbies WHERE name = ?', (hobby,))
    hobby_id = cursor.fetchone()[0]
    for location in loc_list:
        cursor.execute('INSERT INTO locations (hobby_id, location) VALUES (?, ?)', (hobby_id, location))

# Commit changes and close connection
conn.commit()
conn.close()
