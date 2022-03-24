from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from todos.models import Todo


def index(request):
    items = []
    filter = None

    # Get only the user-specific todo items.
    if request.user.is_authenticated:
        filter = request.GET.get('filter')
        print('Filter = ', filter)

        items = filter_results(request.user, filter)

    return render(request, 'index.html', {
        'items': items,
        'filter': filter
    })


def filter_results(user, filter):
    # If filter is completed
    if filter == 'completed':
        return Todo.objects.filter(
            user=user,
            completed=True
        ).order_by('-created_at')

    # Else If filter is pending
    elif filter == 'pending':
        return Todo.objects.filter(
            user=user,
            completed=False
        ).order_by('-created_at')

    # Otherwise
    else:
        return Todo.objects.filter(user=user).order_by('-created_at')


@login_required
def create(request):
    return render(request, 'form.html', {
        'form_type': 'create'
    })


@login_required
def save(request):
    # Get the form data from the request.
    title = request.POST.get('title')
    description = request.POST.get('description')

    # Get hidden form data.
    form_type = request.POST.get('form_type')
    id = request.POST.get('id')

    print('Form type received:', form_type)
    print('Form todo id received:', id)

    # Validation logic
    if title is None or title.strip() == '':
        messages.error(request, 'Item not saved. Please provide the title.')
        return redirect(request.META.get('HTTP_REFERER'))

    if form_type == 'create':
        # Create a new todo item with the data.
        todo = Todo.objects.create(
            title=title,
            description=description,
            created_at=timezone.now(),
            user=request.user
        )
        print('New Todo created: ', todo.__dict__)
    elif form_type == 'edit' and id.isdigit():
        todo = Todo.objects.get(pk=id)
        print('Got todo item: ', todo.__dict__)

        # Save logic
        todo.title = title
        todo.description = description

        todo.save()
        print('Todo updated: ', todo.__dict__)

    # Add save success message
    messages.info(request, 'Todo Item Saved.')
    # Redirect back to index page
    return redirect('index')


@login_required
def edit(request, id):
    print('Received Id: ' + str(id))

    # Fetch todo item by id
    todo = Todo.objects.get(pk=id)
    print('Got todo item: ', todo.__dict__)

    # Check if the logged in user is the creator user of todo.
    if request.user.id != todo.user.id:
        messages.error(
            request, 'You are not authorized to edit this todo item.')
        return redirect('index')

    return render(request, 'form.html', {
        'form_type': 'edit',
        'todo': todo
    })


@login_required
def delete(request, id):
    # Fetch todo item by id
    todo = Todo.objects.get(pk=id)
    print('Got todo item: ', todo.__dict__)

    # Check if the logged in user is the creator user of todo.
    if request.user.id == todo.user.id:
        messages.info(request, 'Todo Item has been deleted.')
        todo.delete()
        return redirect('index')

    messages.error(request, 'You are not authorized to delete this todo item.')
    return redirect('index')



from urllib import request
from jose import jwt
from social_core.backends.oauth import BaseOAuth2


class Auth0(BaseOAuth2):
    """Auth0 OAuth authentication backend"""
    name = 'auth0'
    SCOPE_SEPARATOR = ' '
    ACCESS_TOKEN_METHOD = 'POST'
    REDIRECT_STATE = False
    EXTRA_DATA = [
        ('picture', 'picture'),
        ('email', 'email')
    ]

    def authorization_url(self):
        return 'https://' + self.setting('DOMAIN') + '/authorize'

    def access_token_url(self):
        return 'https://' + self.setting('DOMAIN') + '/oauth/token'

    def get_user_id(self, details, response):
        """Return current user id."""
        return details['user_id']

    def get_user_details(self, response):
        # Obtain JWT and the keys to validate the signature
        id_token = response.get('id_token')
        jwks = request.urlopen('https://' + self.setting('DOMAIN') + '/.well-known/jwks.json')
        issuer = 'https://' + self.setting('DOMAIN') + '/'
        audience = self.setting('KEY')  # CLIENT_ID
        payload = jwt.decode(id_token, jwks.read(), algorithms=['RS256'], audience=audience, issuer=issuer)

        return {'username': payload['nickname'],
                'first_name': payload['name'],
                'picture': payload['picture'],
                'user_id': payload['sub'],
                'email': payload['email']}

from django.contrib.auth import logout as log_out
from django.conf import settings
from django.http import HttpResponseRedirect
from urllib.parse import urlencode


def logout(request):
    log_out(request)
    return_to = urlencode({'returnTo': request.build_absolute_uri('/')})
    logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
                 (settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
    return HttpResponseRedirect(logout_url)