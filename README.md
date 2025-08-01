# Setup (local development)

1. Clone:

git clone https://github.com/nicholasgizzi/nist_tracker_webapp.git
cd nist_tracker_webapp

2. Setup virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install requirements
pip install -r requirements.txt

4. Copy config template and customize
cp instance/config.example.py instance/config.py

5. Initialize or upgrade the db
flask db upgrade
python seed.py # this seeds the database with the NIST CSF framework functions, categories, and labels

6. run the app
gunicorn -w 4 -b 127.0.0.1:5001 "run:create_app()"
