from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from django.conf import settings
from django.http import HttpResponse
import statistics as st
from .models import *
from django.contrib.auth import authenticate
from django.contrib import messages

def home(request):
    return render(request, "index.html")

def login(request):
    if request.POST:
        username=request.POST['email']
        Password=request.POST['password']
        print(username,'##',Password)
        user=authenticate(username=username,password=Password)
        print(user)
        if user is not None:
            # login(request,user)
            if user.usertype=='admin':
                id=user.id
                request.session['uid']=id
                msg="login successfully"
                messages.info(request,msg)
                print("msg",msg)
                return redirect('adminHome')
            elif user.usertype=='user':
                id=user.id
                request.session['uid']=id
                msg="login successfully"
                messages.info(request,msg)
                print("msg",msg)
                return redirect('userHome')
            else:
                msg="username or password invalid"
                messages.info(request,msg)
                print("msg",msg)
                return redirect('login')
        elif username=='admin@gmail.com' and Password=='admin':
            #   id=user.id
            #     request.session['uid']=id
                msg="login successfully"
                messages.info(request,msg)
                print("===========================================",msg)
                return redirect('adminHome')
            
        else:
            msg="username or password invalid"
            messages.info(request,msg)
            print("msg",msg)
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.POST:
        name=request.POST['name']
        address=request.POST['address']
        phone=request.POST['phone number']
        Email=request.POST['email']
        password=request.POST['password']
        if Login.objects.filter(username__iexact=Email).exists() or Register.objects.filter(Email__iexact=Email).exists():
            print("User already exists")
            messages.info(request,"An account with this email already exists. Please log in or use a different email.")
        else:
            q=Login.objects.create_user(username=Email,usertype='user',password=password,viewpassword=password)
            q.save()
            regqry=Register.objects.create(Name=name,Email=Email,Address=address,Phone=phone,usertype='user',user=q)
            regqry.save()
            messages.info(request,"User Registered successfully")
        return redirect('login')
    return render(request,'register.html')


def userHome(request):
    return render(request,'User/userHome.html')
def adminHome(request):
 
    movies = AdminMovie.objects.all()
    return render(request, 'admin/adminhome.html', {'movies': movies})
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AdminMovie  # Ensure this matches your model name

def add_movie_view(request):
    if request.method == 'POST':
        # 1. Get data from the POST request
        name = request.POST.get('movie_name')
        emotion = request.POST.get('emotion_type')
        desc = request.POST.get('description')
        link = request.POST.get('movie_link')
        rating = request.POST.get('star_rating')
        
        # 2. Get the uploaded image file (from request.FILES)
        img = request.FILES.get('image')

        # 3. Create and save the object
        try:
            movie = AdminMovie(
                movie_name=name,
                emotion_type=emotion,
                description=desc,
                movie_link=link,
                star_rating=rating,
                image=img
            )
            movie.save()
            
            # This triggers the alert script in your HTML
            messages.success(request, "Movie added successfully!")
            return redirect('add_movie_view') # Redirect back to clear the form
            
        except Exception as e:
            messages.error(request, f"Error: {e}")
            
    return render(request, 'admin/add_movie.html') # Adjust path if different


def view_movies(request):
    # Fetch all movies from the database
    movies = AdminMovie.objects.all()
    
    # Pass the movies list to the template
    return render(request, 'admin/view_movies.html', {'movies': movies})
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import AdminMovie

def delete_movie(request):
    # Retrieve the movie or return a 404 if not found
    id=request.GET.get('id')
    movie = get_object_or_404(AdminMovie, id=id)
    movie.delete()
    
    # Send a success message
    messages.success(request, "Movie deleted successfully.")
    return redirect('view_movies')  # Redirect back to your list page


def camera(request):
    i = 0
    GR_dict = {0: (0, 255, 0), 1: (0, 0, 255)}
    model = tf.keras.models.load_model('final_model.h5')
    face_cascade = cv2.CascadeClassifier(str(settings.BASE_DIR / 'haarcascade_frontalface_default.xml'))

    output = []
    cap = cv2.VideoCapture(0)
    while (i <= 30):
        ret, img = cap.read()
        faces = face_cascade.detectMultiScale(img, 1.05, 5)

        for x, y, w, h in faces:
            face_img = img[y:y+h, x:x+w]
            resized = cv2.resize(face_img, (224, 224))
            reshaped = resized.reshape(1, 224, 224, 3) / 255
            predictions = model.predict(reshaped)

            max_index = np.argmax(predictions[0])

            emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'neutral', 'surprise')
            predicted_emotion = emotions[max_index]
            output.append(predicted_emotion)

            cv2.rectangle(img, (x, y), (x+w, y+h), GR_dict[1], 2)
            cv2.rectangle(img, (x, y-40), (x+w, y), GR_dict[1], -1)
            cv2.putText(img, predicted_emotion, (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        i = i + 1

        cv2.imshow('LIVE', img)
        key = cv2.waitKey(1)
        if key == 27:
            cap.release()
            cv2.destroyAllWindows()
            break

    cap.release()
    cv2.destroyAllWindows()
    final_output1 = st.mode(output)
    return render(request, "buttons.html", {'final_output': final_output1})

def buttons(request):
    return render(request, "buttons.html")

def moviesSurprise(request):
    data=AdminMovie.objects.filter(emotion_type='surprise')
    return render(request, "moviesSurprise.html", {'data': data})

def moviesAngry(request):
    data = AdminMovie.objects.filter(emotion_type='angry')
    return render(request, "moviesAngry.html", {'data': data})


def moviesSad(request):
    data = AdminMovie.objects.filter(emotion_type='sad')
    return render(request, "moviesSad.html", {'data': data})


def moviesDisgust(request):
    data = AdminMovie.objects.filter(emotion_type='disgust')
    return render(request, "moviesDisgust.html", {'data': data})


def moviesHappy(request):
    data = AdminMovie.objects.filter(emotion_type='happy')
    return render(request, "moviesHappy.html", {'data': data})


def moviesFear(request):
    data = AdminMovie.objects.filter(emotion_type='fear')
    return render(request, "moviesFear.html", {'data': data})


def moviesNeutral(request):
    data = AdminMovie.objects.filter(emotion_type='neutral')
    return render(request, "moviesNeutral.html", {'data': data})


# def adminHome(request):
#     if 'uid' not in request.session or Login.objects.get(id=request.session['uid']).usertype != 'admin':
#         return redirect('login')
#     movies = Movie.objects.all()
#     return render(request, 'adminHome.html', {'movies': movies})

def add_movie(request):
    if 'uid' not in request.session or Login.objects.get(id=request.session['uid']).usertype != 'admin':
        return redirect('/login')
    if request.method == 'POST':
        movie_name = request.POST['movie_name']
        description = request.POST['description']
        movie_link = request.POST['movie_link']
        emotion_type = request.POST['emotion_type']
        star_rating = request.POST['star_rating']
        image = request.FILES.get('image')
        AdminMovie.objects.create(movie_name=movie_name, description=description, movie_link=movie_link, emotion_type=emotion_type, star_rating=star_rating, image=image)
        messages.info(request, "Movie added successfully")
        return redirect('adminHome')
    return render(request, 'add_movie.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Login, Feedback

def add_feedback(request):
    # Check session
    if 'uid' not in request.session:
        messages.info(request, "Please login first")
        return redirect('login')

    uid = request.session['uid']

    try:
        user = Login.objects.get(id=uid)
    except Login.DoesNotExist:
        messages.info(request, "Invalid session")
        return redirect('login')

    # Allow both admin and user (change if needed)
    if user.usertype not in ['admin', 'user']:
        messages.info(request, "Unauthorized access")
        return redirect('login')

    # Handle form submit
    if request.method == "POST":
        subject = request.POST.get('subject')
        feedback_text = request.POST.get('feedback')

        Feedback.objects.create(
            user=user,
            subject=subject,
            feedback=feedback_text
        )

        messages.success(request, "Feedback submitted successfully!")
        return redirect('add_feedback')

    return render(request, 'User/add_feedback.html')



def view_feedback(request):
    if 'uid' not in request.session:
        messages.info(request, "Please login first")
        return redirect('login')

    uid = request.session['uid']

    try:
        user = Login.objects.get(id=uid)
    except Login.DoesNotExist:
        return redirect('login')

    # Admin sees all feedback
    if user.usertype == 'admin':
        feedbacks = Feedback.objects.all().order_by('-created_at')

    # User sees only their feedback
    elif user.usertype == 'user':
        feedbacks = Feedback.objects.filter(user=user).order_by('-created_at')

    else:
        return redirect('login')

    return render(request, 'User/view_feedback.html', {'feedbacks': feedbacks})
def admin_view_feedback(request):
    if 'uid' not in request.session:
        messages.info(request, "Please login first")
        return redirect('login')

    uid = request.session['uid']

    try:
        user = Login.objects.get(id=uid)
    except Login.DoesNotExist:
        return redirect('login')

    # Admin sees all feedback
    if user.usertype == 'admin':
        feedbacks = Feedback.objects.all().order_by('-created_at')

    # User sees only their feedback
    elif user.usertype == 'user':
        feedbacks = Feedback.objects.filter(user=user).order_by('-created_at')

    else:
        return redirect('login')

    return render(request, 'admin/view_feedback.html', {'feedbacks': feedbacks})
