# Emotion-Based Movie Recommendation System

A Django web application that detects a user’s facial emotion using a webcam and recommends movies based on the detected mood. The system blends machine learning, computer vision, and a movie catalog so users can get movie suggestions that match their emotional state.

## Overview

This project was designed as an emotion-aware recommendation platform where:

- a user logs in or registers,
- the webcam captures the user’s face,
- a deep learning model predicts the current emotion,
- the app redirects the user to a movie category matching that emotion,
- an admin can manage movie records and their emotional mapping.

The project combines:

- Django for the web app
- OpenCV for face detection
- TensorFlow/Keras for emotion classification
- SQLite as the database
- HTML/CSS/JS templates for the front end

## Features

- User authentication and registration
- Admin dashboard for managing movies
- Add, view, and delete movie entries
- Emotion-based movie recommendation pages
- Real-time webcam emotion detection
- Feedback submission and viewing
- Movie pages grouped by mood such as Happy, Sad, Angry, Fear, Neutral, Surprise, and Disgust

## Supported Emotion Categories

The application organizes movies into these categories:

- Angry
- Fear
- Happy
- Neutral
- Sad
- Surprise
- Disgust

## Tech Stack

- Python 3.9+
- Django 4.2.19
- TensorFlow 2.12
- OpenCV
- NumPy
- SQLite
- HTML, CSS, JavaScript

## Project Structure

```text
movie_recommender/
├── myapp/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── movie_recommender/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── template/
├── static/
├── images/
├── WD_INNOVATIVE/
├── db.sqlite3
├── manage.py
├── requirements.txt
├── final_model.h5
├── Emotion_Detection.ipynb
├── Emotion_Model_RealTime_Tester.ipynb
├── README.md
├── Update_Model.py
├── capture.py
├── model.py
├── model.xml
├── haarcascade_frontalface_default.xml
├── READIT.odt
└── ...
```

## Prerequisites

Before running the project, install:

- Python 3.9 or newer
- pip
- Virtual environment (recommended)
- A webcam for real-time emotion detection

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd movie_recommender
```

2. Create and activate a virtual environment:

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Create an admin account (optional but recommended):

```bash
python manage.py createsuperuser
```

## Running the Application

Start the Django development server:

```bash
python manage.py runserver
```

Then open the browser at:

```text
http://127.0.0.1:8000/
```

## How the System Works

1. A user registers or logs in.
2. The user opens the camera-based emotion detection route.
3. The app captures face frames using OpenCV.
4. The TensorFlow model predicts an emotion such as happy, sad, fear, or angry.
5. The predicted mood is used to fetch related movie suggestions.
6. Admin users can upload movie posters, links, and emotion categories through the admin panel or movie management page.

## Admin Features

The admin can:

- add movie entries to the database,
- categorize each movie by emotion,
- upload the cover image,
- provide a movie link and rating,
- remove outdated or incorrect movie entries,
- view user feedback.

## User Flow

- Register as a user
- Login to the system
- Open the movie recommendation section
- Start the webcam emotion detection
- View movies based on the detected emotion
- Rate or provide feedback if the interface supports it

## Model Notes

The project includes a trained model file:

- `final_model.h5`

This file is used by the emotion detection logic to classify the face captured by the webcam. You can also retrain or update the model using the notebooks in the project folder:

- `Emotion_Detection.ipynb`
- `Emotion_Model_RealTime_Tester.ipynb`
- `Update_Model.py`

## Common Setup Notes

- Use a working webcam connected to the system.
- If TensorFlow is not installed correctly, install the matching version from the requirements file.
- For some environments, you may need to install OpenCV and TensorFlow separately depending on your OS and Python version.
- If there are issues with static/media files, ensure the `static` and `media` folders exist and permissions are correct.

## Troubleshooting

### Django migration errors

Run:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Module import errors

Ensure all packages are installed:

```bash
pip install -r requirements.txt
```

### Webcam not working

- Check whether the device is connected and accessible.
- Confirm your browser environment allows camera access if a web app is used.
- Verify OpenCV has permission to open the camera.

### Model not found

Make sure `final_model.h5` is present in the project root and the path used by the app points to the correct directory.

## Future Improvements

- Improve emotion recognition accuracy with a larger training dataset
- Add more movie genres and recommendation logic
- Add recommendation ranking by user ratings
- Include personalized recommendations using user history
- Add a REST API for integration with mobile apps
- Add user profile management and watchlist features

## License

This project is intended for educational and academic use. You may modify or extend it for learning purposes.

## Acknowledgements

This project is a demonstration of how computer vision and machine learning can enhance user experiences in media platforms. It uses open-source frameworks such as Django, OpenCV, and TensorFlow.

## Contact

If you want to improve or extend this project, you can work from the repository and update the app logic, model, and recommendations.
