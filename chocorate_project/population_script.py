import os


import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chocorate_project.settings')

django.setup()

from django.contrib.auth.models import User
from chocorate.models import Chocolate, UserProfile




def add_user(username, email, password):
    try:
        u = User.objects.get(username=username)
    except:
        u = User.objects.create_user(username, email, password)
    return u


def add_user_profile(user, website, picture, notifications):
    p = \
        UserProfile.objects.get_or_create(user=user, website=website, picture=picture, notifications=notifications)[0]
    return p


def add_chocolate(name, description, picture, picture_url, picture_alt, chocolate_type, comments, avgrating):
    choco = Chocolate.objects.get_or_create(name=name, description=description, picture=picture, picture_alt=picture_alt,
                                            picture_url=picture_url, chocolate_type=chocolate_type,
                                            comments=comments, avgrating=avgrating)[0]
    return choco


def populate():
    print('populating....')
    # Users
    annie = add_user('pretty_annie', 'annie1997@gmail.com', '1234')
    annie.save()
    julie = add_user('julie.peterson', 'Julie.Peterson@gla.ac.uk', '0000')
    julie.save()

    # User profiles
    Annie = add_user_profile(annie, '', '', 5)
    Annie.save()
    Julie = add_user_profile(julie, '', '', 2)
    Julie.save()

    # Chocolates
    choco1 = add_chocolate('choco1', 'best chocolate', '', '', '', 'milk chocolate', 'hfjgk,\njhdfdjlskg', 3.5)
    choco1.save()
    choco2 = add_chocolate('choco2', 'best chocolate', '', '', '', 'milk chocolate', 'hfjgk,\njhdfdjlskg', 3.5)
    choco2.save()

    print('done')


if __name__ == '__main__':
    populate()

