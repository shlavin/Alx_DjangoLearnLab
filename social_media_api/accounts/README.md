# Social Media API

A Django REST API for a social media platform with user authentication.

## Features
- Custom User Model
- Token-based Authentication
- User Profiles
- Followers / Following System

## Setup

```bash
git clone https://github.com/yourname/Alx_DjangoLearnLab.git
cd social_media_api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


## Follow System

### Follow a User
POST `/api/accounts/follow/<user_id>/`

### Unfollow a User
POST `/api/accounts/unfollow/<user_id>/`

## Feed

### Get Feed
GET `/api/feed/`

Returns posts from users you follow, ordered by most recent.
