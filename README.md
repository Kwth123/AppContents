AppContents is a basic python program which shows the steps and underlying logic of whast used in our final application

Prerequisites

- Python (https://www.python.org/downloads/)
- pip (should be included with the Python download but if not please contact me for help)

Note: The databaseCreationHobbies.py file is used to generate the hobbies database and doesn't need to be run.

Setup

1. Clone the Repository

    git clone https://github.com/your-username/your-repository.git
    cd AppContents

2. Create and Activate a Virtual Environment

    On Windows:
        python -m venv venv
        venv\Scripts\activate

    On macOS/Linux:
        python3 -m venv venv
        source venv/bin/activate

3. Install the Dependencies

    pip install -r requirements.txt

4. Set Up the Google Maps API Key

    - Go to the Google Maps website and get an API key. Google typically provides new accounts with free credit, so you shouldn't run out of it anytime soon. https://developers.google.com/maps/documentation/javascript/get-api-key
    - Replace API_KEY = "ENTER_API_KEY" with your actual API key in the configuration file.

Running the Project

Once you have set up the virtual environment and installed the dependencies, you can run the project with:

    python main.py

Additional Notes

hard coding the google maps API shouldnt be done in production, 

CODE USED TO CREATE requirements.txt:
Install python 
python -m venv venv
venv\Scripts\activate
pip install googlemaps
pip freeze > requirements.txt
