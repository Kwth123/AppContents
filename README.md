### AppContents

AppContents is a basic Python program that demonstrates the steps and underlying logic used in our final application.

#### Setup

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/Kwth123/AppContents
   cd AppContents
   ```

2. **Activate the Provided Virtual Environment:**
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

3. **Set Up the Google Maps API Key:**
   - Obtain an API key from the [Google Maps website](https://developers.google.com/maps/documentation/javascript/get-api-key).
   - Replace `API_KEY = "KEY_HERE"` with your actual API KEY.

#### Running the Project
To run the project, execute:
```sh
python main.py
```

#### Additional Notes
- Avoid hardcoding the Google Maps API key in production. If you do its no issue, commit a new change with the key replaced with "KEY_HERE" and delete the key from google maps website

---

#### CODE USED TO CREATE `requirements.txt`:
```sh
Install python
python -m venv venv
venv\Scripts\activate
pip install googlemaps
pip freeze > requirements.txt
```
