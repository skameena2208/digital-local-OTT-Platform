from datetime import timedelta

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import ContactForm, CustomerForm, NotificationForm, CategoryForm, MovieForm, WebseriesForm, SerialsForm, \
    EpisodeForm, SerialEpisodeForm, MovieReviewForm, SerialReviewForm, WebseriesReviewForm, SubscriptionForm, \
    SubscribersForm
from .models import Customer, AdminLogin, Notification, Category, Movie, Webseries, Serials, Episode, Serials_Episodes, \
    Movie_Review, Webseries_Review, Serial_Review, Subscription, Subscribers, Webseries


# Create your views here.
def index(request):
    return render(request, "index.html", {})


def about(request):
    profile = Movie.objects.all()
    return render(request, "about.html", {"profile": profile})


def services(request):
    return render(request, "services.html", {})


def apartment(request):
    return render(request, "apartment.html", {})


def blog(request):
    return render(request, "blog.html", {})


def elements(request):
    return render(request, "elements.html", {})


def project(request):
    return render(request, "project.html", {})


def single_blog(request):
    return render(request, "single-blog.html", {})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return render(request, "contact.html", {"msg": "Contact Sent Successfully"})
        return render(request, "contact.html", {"psg": "Contact Not Sent...Please Try Again"})
    return render(request, "contact.html", {})


# def customer_login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         log = Customer.objects.filter(email=email, password=password)
#         if log.exists():
#             if log[0].status == "Accepted":
#                 request.session['email'] = email
#                 return render(request, "customer_home.html", {"msg": "Accepted Successfully"})
#             elif log[0].status == "Rejected":
#                 return render(request, "customer_login.html", {"msg": "Rejected Login"})
#             else:
#                 return render(request, "customer_login.html", {"msg": "Pending"})
#         return render(request, "customer_login.html", {"msg": "Login Failed"})
#     return render(request, "customer_login.html", {})


def customer_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email, "", password)
        login = Customer.objects.filter(email=email, password=password)
        if login.exists():
            print("hi")
            if login[0].status == "Accepted":
                request.session['email'] = email
                client = Customer.objects.get(email=email)
                return render(request, "customer_home.html", {"psg": "Login Successfully"})
            else:
                return render(request, "customer_login.html", {"msg": "Your Account Is On Hold !"})
        else:
            return render(request, "customer_login.html", {"msg": "Invalid Data"})
    return render(request, "customer_login.html", {})


# def customer_registered(request):
#     if request.method == "POST":
#         form = CustomerForm(request.POST, request.FILES)
#         print(form.errors)
#         if form.is_valid():
#             form.save()
#             return render(request, "customer_login.html", {"msg": "Your "})
#         return render(request, "customer_registered.html", {"msg": "Not Registered"})
#     return render(request, "customer_registered.html", {})

def customer_registered(request):
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES)
        print(form.errors)
        email = request.POST["email"]
        if Customer.objects.filter(email=email).exists():
            return render(request, "customer_registered.html", {"psg": "This Email Is Already Exists"})
        else:
            if form.is_valid():
                form.save()
                return render(request, "customer_login.html", {"msg": "Your Details Is Register Successfully"})
    return render(request, "customer_registered.html", {})


def customer_home(request):
    return render(request, "customer_home.html", {})


def customer_view_movies(request):
    email = request.session.get('email')  # Get the customer's email from the session
    movies = Movie.objects.all()  # Fetch all movies

    if not email:  # Check if the user is logged in or has an email session
        return redirect('login')  # Redirect to login page if not logged in

    # Get customer and their current subscription if available
    customer = get_object_or_404(Customer, email=email)
    active_subscription = Subscribers.objects.filter(
        customer_email=email,
        startdate__lte=timezone.now().date(),
        enddate__gte=timezone.now().date()
    ).first()

    # Determine if the user is eligible to watch movies
    eligible_to_watch = active_subscription is not None

    return render(request, "customer_view_movies.html", {
        "movies": movies,
        "eligible_to_watch": eligible_to_watch
    })


def customer_view_webseries(request):
    email = request.session.get('email')  # Get the customer's email from the session
    profile = Webseries.objects.all()  # Fetch all web series

    if not email:  # Check if the user is logged in or has an email session
        return redirect('login')  # Redirect to login page if not logged in

    # Get customer and their current subscription if available
    customer = get_object_or_404(Customer, email=email)
    active_subscription = Subscribers.objects.filter(
        customer_email=email,
        startdate__lte=timezone.now().date(),
        enddate__gte=timezone.now().date()
    ).first()

    # Determine if the user is eligible to view episodes
    eligible_to_watch = active_subscription is not None

    return render(request, "customer_view_webseries.html", {
        "profile": profile,
        "eligible_to_watch": eligible_to_watch
    })


def customer_view_serials(request):
    email = request.session.get('email')  # Get the customer's email from the session
    profile = Serials.objects.all()  # Fetch all serials

    if not email:  # Check if the user is logged in or has an email session
        return redirect('login')  # Redirect to login page if not logged in

    # Get customer and their current subscription if available
    customer = get_object_or_404(Customer, email=email)
    active_subscription = Subscribers.objects.filter(
        customer_email=email,
        startdate__lte=timezone.now().date(),
        enddate__gte=timezone.now().date()
    ).first()

    # Determine if the user is eligible to view serials
    eligible_to_watch = active_subscription is not None

    return render(request, "customer_view_serials.html", {
        "profile": profile,
        "eligible_to_watch": eligible_to_watch
    })


def customer_profile(request):
    email = request.session.get('email')  # Get customer email from session
    profile = get_object_or_404(Customer, email=email)  # Fetch customer profile

    # Fetch all subscriptions for the customer
    all_subscriptions = Subscribers.objects.filter(customer_email=email)

    # Filter active subscriptions (where end date is in the future or today)
    active_subscription = all_subscriptions.filter(enddate__gte=timezone.now().date()).order_by('-enddate').first()

    # Filter expired subscriptions (where end date is in the past)
    expired_subscriptions = all_subscriptions.filter(enddate__lt=timezone.now().date()).order_by('-enddate')

    return render(request, "customer_profile.html", {
        "x": profile,
        "active_subscription": active_subscription,  # Active subscription details
        "expired_subscriptions": expired_subscriptions,  # Expired subscriptions for history
    })


def customer_logout(request):
    request.session.flush()
    return redirect('/customerlogin')


def admin_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        log = AdminLogin.objects.filter(email=email, password=password)
        try:
            if log.exists():
                request.session["email"] = email
                return render(request, "admin_home.html", {"msg": "Successfully Login"})
            return render(request, "admin_login.html", {"msg": "Incorrect Email Or Password"})
        except Exception as e:
            print(e)
            return render(request, "admin_home.html", {"msg": ""})
    return render(request, "admin_login.html", {"msg": ""})


def admin_home(request):
    return render(request, "admin_home.html", {})


def admin_view_contact(request):
    contact = Customer.objects.all()
    return render(request, "admin_view_contact.html", {"contact": contact})


def admin_view_customer(request):
    customer = Customer.objects.all()
    return render(request, "admin_view_customer.html", {"customer": customer})


def accept_customer(request, id):
    cus = Customer.objects.get(id=id)
    cus.status = "Accepted"
    cus.save()
    return redirect('/admin_view_customer')


def reject_customer(request, id):
    cus = Customer.objects.get(id=id)
    cus.status = "Rejected"
    cus.save()
    return redirect('/admin_view_customer')


def admin_logout(request):
    request.session.flush()
    return redirect('/admin_login')


def customer_edit(request):
    email = request.session['email']
    customer = Customer.objects.get(email=email)
    return render(request, 'customer_edit.html', {'x': customer})


def customer_update(request):
    if request.method == 'POST':
        id = request.POST['id']
        cus = Customer.objects.get(id=id)
        form = CustomerForm(request.POST, request.FILES, instance=cus)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('/customer_profile')
        return render(request, 'customer_edit.html', {})
    return render(request, 'customer_edit.html', {})


def is_login(request):
    if request.session.__contains__('email'):
        return True
    else:
        return False


def customer_change_password(request):
    email = request.session['email']
    if is_login(request):
        if request.method == 'POST':

            password = request.POST['password']
            new_password = request.POST['new_password']
            try:
                cust = Customer.objects.get(email=email, password=password)
                cust.password = new_password
                cust.save()
                return redirect('/customerlogin')
            except Exception as e:
                print(e)
                return render(request, "customer_change_password.html", {"msg": "Invalid Credentials", "email": email})
        return render(request, "customer_change_password.html", {"email": email})
    return render(request, "customer_change_password.html", {"email": email})


def customer_deactivate(request, id):
    cust = Customer.objects.get(id=id)
    cust.status = 'pending'
    cust.save()
    return redirect('/customerlogin')


# def admin_change_password(request):
#     email = request.session['email']
#     if (request):
#         if request.method == 'POST':
#
#             password = request.POST['password']
#             new_password = request.POST['new_password']
#             try:
#                 cust = Customer.objects.get(email=email, password=password)
#                 cust.password = new_password
#                 cust.save()
#                 return redirect('/admin_login')
#             except Exception as e:
#                 print(e)
#                 return render(request, "admin_change_password.html",
#                               {"msg": "Your Password Not Changed, Please Try Again", "email": email})
#         return render(request, "admin_change_password.html", {"email": email})
#     return render(request, "admin_change_password.html", {"email": email})


def admin_change_password(request):
    email = request.session["email"]
    if is_login(request):
        print("hello")
        if request.method == 'POST':
            print("hello1")
            password = request.POST['password']
            new_password = request.POST['new_password']
            try:
                user = AdminLogin.objects.get(email=email, password=password)
                user.password = new_password
                user.save()
                return redirect('/admin_login')
            except Exception as e:
                print(e)
                return render(request, "admin_change_password.html",
                              {"msg": "Your Password Not Changed, Please Try Again", "email": email})
        return render(request, "admin_change_password.html", {"email": email})
    return render(request, "admin_change_password.html", {"email": email})


def add_notification(request):
    email = request.session['email']
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_notification')
        return render(request, "add_notification.html",
                      {"msg": "Notification Not Posted, Please Try Again", "email": email})
    return render(request, "add_notification.html", {"email": email})


def view_notification(request):
    profile = Notification.objects.all()
    return render(request, "view_notification.html", {"profile": profile})


def notification_update(request):
    if request.method == 'POST':
        id = request.POST['id']
        cus = Notification.objects.get(id=id)
        form = NotificationForm(request.POST, request.FILES, instance=cus)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('/view_notification')
        return render(request, "notification_edit.html", {})
    return render(request, "notification_edit.html", {})


def notification_edit(request, id):
    profile = Notification.objects.get(id=id)
    return render(request, "notification_edit.html", {'x': profile})


def view_notification_delete(request, id):
    cus = Notification.objects.get(id=id)
    cus.delete()
    return redirect('/view_notification')


def admin_add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_view_category')
        return render(request, "admin_add_category.html", {})
    return render(request, "admin_add_category.html", {})


def admin_view_category(request):
    profile = Category.objects.all()
    return render(request, "admin_view_category.html", {"profile": profile})


def category_update(request):
    if request.method == 'POST':
        id = request.POST['id']
        cus = Category.objects.get(id=id)
        form = CategoryForm(request.POST, request.FILES, instance=cus)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('/admin_view_category')
        return render(request, "category_edit.html", {})
    return render(request, "category_edit.html", {})


def category_edit(request, id):
    profile = Category.objects.get(id=id)
    return render(request, "category_edit.html", {'x': profile})


def view_category_delete(request, id):
    cus = Category.objects.get(id=id)
    cus.delete()
    return redirect('/admin_view_category')


def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('view_movie')
        return render(request, "add_movie.html", {"msg": "Movie Not Added , Please Try Again"})
    return render(request, "add_movie.html", {})


def view_movie(request):
    profile = Movie.objects.all()
    return render(request, "view_movie.html", {"profile": profile})


def movie_update(request):
    if request.method == 'POST':
        id = request.POST['id']
        cus = Movie.objects.get(id=id)
        form = MovieForm(request.POST, request.FILES, instance=cus)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('/view_movie')
        return render(request, 'movie_edit.html', {})
    return render(request, 'movie_edit.html', {})


def movie_edit(request, id):
    profile = Movie.objects.get(id=id)
    return render(request, 'movie_edit.html', {'x': profile})


def view_movie_delete(request, id):
    cus = Movie.objects.get(id=id)
    cus.delete()
    return redirect('/view_movie')


def add_web_series(request):
    if request.method == 'POST':
        form = WebseriesForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('view_webseries')
        return render(request, "add_webseries.html", {"msg": "Webseries Not Added , Please Try Again"})
    return render(request, "add_webseries.html", {})


def view_webseries(request):
    profile = Webseries.objects.all()
    return render(request, "view_webseries.html", {"profile": profile})


def webseries_update(request):
    if request.method == 'POST':
        id = request.POST['id']
        cus = Webseries.objects.get(id=id)
        form = WebseriesForm(request.POST, request.FILES, instance=cus)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('/view_webseries')
        return render(request, "webseries_edit.html", {})
    return render(request, "webseries_edit.html", {})


def webseries_edit(request, id):
    pro = Webseries.objects.get(id=id)
    return render(request, "webseries_edit.html", {'x': pro})


def view_webseries_delete(request, id):
    cus = Webseries.objects.get(id=id)
    cus.delete()
    return redirect('/view_webseries')


def add_serials(request):
    if request.method == 'POST':
        form = SerialsForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('view_serials')
        return render(request, "add_serials.html", {"psg": "Serial Not Added...Please Try Again"})
    return render(request, "add_serials.html", {})


def view_serial(request):
    profile = Serials.objects.all()
    return render(request, "view_serials.html", {"profile": profile})


def serial_update(request):
    if request.method == 'POST':
        id = request.POST['id']
        cus = Serials.objects.get(id=id)
        form = SerialsForm(request.POST, request.FILES, instance=cus)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('/view_serials')
        return render(request, "serial_edit.html", {})
    return render(request, "serial_edit.html", {})


def serial_edit(request, id):
    profile = Serials.objects.get(id=id)
    return render(request, "serial_edit.html", {'x': profile})


def view_serial_delete(request, id):
    cus = Serials.objects.get(id=id)
    cus.delete()
    return redirect('/view_serials')


def webseries_add_episode(request, id):
    web_series = Webseries.objects.get(id=id)
    if request.method == 'POST':
        form = EpisodeForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return render(request, 'view_webseries_episodes.html',
                          {'form': form, 'x': web_series, "msg": "Episode Added"})
        else:
            form = EpisodeForm()
            return render(request, 'webseries_add_episodes.html',
                          {'form': form, 'x': web_series, "psg": "Episode Not Added"})
    return render(request, 'webseries_add_episodes.html', {'x': web_series, "msg": ""})


def view_webseries_episodes(request, id):
    episode = Episode.objects.filter(webseries_id=id)
    return render(request, "view_webseries_episodes.html", {"episode": episode})


def serial_add_episode(request, id):
    serial = Serials.objects.get(id=id)
    if request.method == 'POST':
        form = SerialEpisodeForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return render(request, 'view_serials_episodes.html',
                          {'form': form, 'x': serial, "msg": "episode added"})
        else:
            form = SerialEpisodeForm()
            return render(request, 'serial_add_episode.html',
                          {'form': form, 'x': serial, "msg": "episode not added"})
    return render(request, 'serial_add_episode.html', {'x': serial, "msg": ""})


def view_serials_episodes(request, id):
    episode = Serials_Episodes.objects.filter(serial_id=id)
    return render(request, "view_serials_episodes.html", {"episode": episode})


def customer_view_webseries_episodes(request, id):
    episode = Episode.objects.filter(webseries_id=id)
    return render(request, "customer_view_webseries_episodes.html", {"episode": episode})


def customer_view_serials_episodes(request, id):
    episode = Serials_Episodes.objects.filter(serial_id=id)
    return render(request, "customer_view_serials_episodes.html", {"episode": episode})


def add_movie_review(request, id):
    email = request.session['email']
    movie = Movie.objects.get(id=id)
    if request.method == 'POST':
        form = MovieReviewForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('view_movie_review')
        return render(request, "add_movie_review.html",
                      {'x': movie, "email": email, "msg": "Review Not Posted ,Please Try Again"})
    return render(request, "add_movie_review.html", {'x': movie, "email": email})


def view_movie_review(request):
    profile = Movie_Review.objects.all()
    return render(request, "view_movie_review.html", {"profile": profile})


def add_webseries_review(request, id):
    email = request.session['email']
    webseries = Webseries.objects.get(id=id)
    if request.method == 'POST':
        form = WebseriesReviewForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('view_webseries_review')
        return render(request, "add_webseries_review.html",
                      {'x': webseries, "email": email, "msg": "Review Not Posted ,Please Try Again"})
    return render(request, "add_webseries_review.html", {'x': webseries, "email": email})


def view_webseries_review(request):
    profile = Webseries_Review.objects.all()
    return render(request, "view_webseries_review.html", {"profile": profile})


def add_serial_review(request, id):
    email = request.session['email']
    serial = Serials.objects.get(id=id)
    if request.method == 'POST':
        form = SerialReviewForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('view_serial_review')
        return render(request, "add_serial_review.html",
                      {'x': serial, "email": email, "msg": "Review Not Posted ,Please Try Again"})
    return render(request, "add_serial_review.html", {'x': serial, "email": email})


def view_serial_review(request):
    profile = Serial_Review.objects.all()
    return render(request, "view_serial_review.html", {"profile": profile})


def add_plan(request):
    email = request.session['email']
    if request.method == 'POST':
        form = SubscriptionForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('view_plan')
        return render(request, "add_plan.html", {"email": email, "msg": "Plan Not Added ,Please Try Again"})
    return render(request, "add_plan.html", {"email": email})


def view_plan(request):
    plan = Subscription.objects.all()
    return render(request, "view_plan.html", {"plan": plan})


def customer_view_plans(request):
    plans = Subscription.objects.all()
    return render(request, "customer_view_plans.html", {"plans": plans})


from datetime import timedelta
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Subscribers, Subscription, Customer
from .forms import SubscribersForm


def buy_plan(request, id):
    email = request.session.get('email')  # Get the customer's email from the session
    plans = get_object_or_404(Subscription, id=id)  # Retrieve the selected subscription plan
    customer = get_object_or_404(Customer, email=email)  # Retrieve the customer object

    # Check if the customer has any active subscriptions that are still valid
    active_subscriptions = Subscribers.objects.filter(customer_email=email, enddate__gte=timezone.now().date())

    # If there is an active subscription, show a message and prevent buying a new plan
    if active_subscriptions.exists():
        return render(request, 'buy_plan.html', {
            "message": "Already subscribed to this plan. Enjoy your current subscription!"
        })

    # Auto-calculate start and end dates for the new subscription
    start_date = timezone.now().date()  # Set the start date to today
    end_date = start_date + timedelta(days=plans.months * 30)  # Calculate the end date based on the plan duration

    if request.method == "POST":
        form = SubscribersForm(request.POST)
        if form.is_valid():
            # Save the new subscription
            new_subscription = form.save(commit=False)
            new_subscription.customer_email = email
            new_subscription.subscription = plans
            new_subscription.startdate = start_date
            new_subscription.enddate = end_date
            new_subscription.save()

            # Update the customer's startdate and enddate fields
            customer.startdate = start_date
            customer.enddate = end_date
            customer.save()

            return render(request, 'buy_plan.html', {"message": "Thank you for subscribing! Enjoy your plan."})
        else:
            print(form.errors)

    # Pass 'startdate' and 'enddate' in context
    return render(request, 'buy_plan.html', {
        "plans": plans,
        'email': email,
        'startdate': start_date,
        'enddate': end_date
    })


def admin_view_subscribers(request):
    # Fetch all subscribers with their related subscription plan
    subscribers = Subscribers.objects.select_related('subscription').all()

    # Get the current date to compare subscription status
    today = timezone.now().date()

    # Render the 'admin_view_subscribers.html' template with the list of subscribers
    return render(request, "admin_view_subscribers.html", {"subscribers": subscribers, "today": today})


from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Subscribers, Subscription


def customer_view_history(request):
    # Get the customer's email from the session
    email = request.session.get('email')

    if not email:  # Check if the user is logged in or has an email session
        return redirect('login')  # Redirect to login page if not logged in

    # Fetch the customer's subscription history
    subscriptions = Subscribers.objects.filter(customer_email=email).select_related('subscription')

    # Get the current date to compare subscription status
    today = timezone.now().date()

    # Render the 'customer_view_history.html' template with the list of subscriptions
    return render(request, "customer_view_history.html", {
        "subscriptions": subscriptions,
        "today": today
    })


def plan_delete(request, id):
    cus = Subscription.objects.get(id=id)
    cus.delete()
    return redirect('/view_plan')


def customer_view_movie_reviews(request, id):
    reviews = Movie_Review.objects.filter(movie_id=id)
    return render(request, "customer_view_movie_reviews.html", {'reviews': reviews})


def customer_view_webseries_reviews(request, id):
    reviews = Webseries_Review.objects.filter(web_series_id=id)
    return render(request, "customer_view_webseries_reviews.html", {'reviews': reviews})


def customer_view_serial_reviews(request, id):
    reviews = Serial_Review.objects.filter(serial_id=id)
    return render(request, "customer_view_serial_reviews.html", {'reviews': reviews})
