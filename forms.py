from django import forms
from .models import Contact, Customer, Notification, Category, Movie, Webseries, Serials, Episode, Serials_Episodes, \
    Movie_Review, Serial_Review, Webseries_Review, Subscription, Subscribers


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        exclude = ['status', 'startdate', 'enddate']


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"


class WebseriesForm(forms.ModelForm):
    class Meta:
        model = Webseries
        fields = "__all__"


class SerialsForm(forms.ModelForm):
    class Meta:
        model = Serials
        fields = "__all__"


class EpisodeForm(forms.ModelForm):
    class Meta:
        model = Episode
        fields = "__all__"


class SerialEpisodeForm(forms.ModelForm):
    class Meta:
        model = Serials_Episodes
        fields = "__all__"


class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = Movie_Review
        exclude = ['date']


class WebseriesReviewForm(forms.ModelForm):
    class Meta:
        model = Webseries_Review
        exclude = ['date']


class SerialReviewForm(forms.ModelForm):
    class Meta:
        model = Serial_Review
        exclude = ['date']


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = "__all__"


class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['holder_name', 'card_number', 'cvv_number', 'bank_name']
