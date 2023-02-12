# FastAPI
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python. 
This is a simple blog application using latest FastAPI framework where users can login, sign
up, create/delete posts and make comment on those posts. Registered member can see the list of signed
users. If a user is deleted the all its posts, comments will be deleted 

## Installation
To install dependencies run:

    pip install -r requirements.txt

To start this app run:

    uvicorn blog.main:app --reload
You can avoid `--reload`, its actually always tracking changes and restart your app.


## File Structure
```
├── blog.db
│   ├── __init__.py
│   │── auth.py
│   ├── database.py
│   ├── hashpass.py
│   ├── loginToken.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── blogs.py
│   │   └── users.py
│   │   └── usercomment.py
│   └── internal
│   │   ├── __init__.py
│   │   └── blog.py
│   │   └── comments.py
│   │   └── login.py
│   │   └── user.py
├── README.md
├── requirements.txt
```

## Features:

The application have those following features:

### Login
* Valid user can login otherwise shows proper error message

### Sign up
* User can signup in the app

### Add new post
* Logged in user can add a new post.
  * Required fields
    * Title
    * Description
    * Featured Image
  
### Get Post
* Registered User can see specific user's post.

### List Users
* Registered User can list signup users.

### Delete User
* Registered User can delete signup users. Actually role based login is not implemented yet.

### All Post
* Registered User can list all blog posts.

### Create Post
* Registered User can create post.

### Read Post
* Registered User can read specific post.

### Delete Post
* Registered User can delete post.

> one more important thing is, if user is deleted, all of his/her post and comments of the post will be deleted

### Comment on a post
Anyone can comment on any post. But S/he must provide, name and email address. 
