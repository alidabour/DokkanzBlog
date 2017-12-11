# DokkanzBlog
Django Task for Dokkanz.

## Blog Features :

    Real Time:
        New posts added in real time at /blog
        Post details at /blog/<post_id>
        Post edits added in real time at /blog/<post_id>/edit_post
        Post delete, Post page will be replaced by "Sorry Not available" at /blog/<post_id>/delete_post
    Authentication and Authorization:
         Sign up at /blog/sign_up
        Login at /blog/log_in
        Logout at /blog/log_out
        Login in user can add,edit,delete posts and add comments
        Only the owner of Post can edit/delete it.
    MySql Database
## Guide

Install [Python3.6](https://askubuntu.com/a/865569).

Install [virtualenv](https://virtualenv.pypa.io/en/stable/installation/).

Create a new virtualenv called `my_env`: `virtualenv -p python3 my_env`.

Activate virtualenv : `my_env/source bin/activate`.

Install packages : `pip install -r req.txt`.

Install [Redis](https://redis.io/download).

Install & Connect [MySql](https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database).

Migrate : `python manage.py migrate`.

Runserver : `python manage.py runserver`.
