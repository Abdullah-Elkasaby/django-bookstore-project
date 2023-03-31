
# ITI-Project-Online-Library 
<p>is a web project built with Django. It provides a platform for managing an online library that allows users to search for, filter, and purchase books.</p>

https://user-images.githubusercontent.com/97049761/220857505-f2f86560-9ac6-483f-879b-fc71132d65ee.mp4


## Getting Started
To run the project locally, follow these steps:

<ol> 
<li>
    Clone the repository
    
    git clone https://github.com/Abdullah-Elkasaby/ITI-Project-Online-Library.git
     
</li>
<li>
     Install the required dependencies using pip 
    
     pip install -r requirements.txt 
</li>
<li>
    Create the database tables
    
     python manage.py migrate 
    
</li>
<li>
Start the development server
    
    python manage.py runserver 

The project will be available at http://localhost:8000.
</li>
</ol>

## Project Structure
The project's directory structure follows Django's recommended best practices, with separate folders for the project settings, applications, and static files.
```
ITI-Project-Online-Library/
    library/
        migrations/
        static/
            library/
                css/
                img/
                js/
        templates/
            library/
                base.html
                book_detail.html
                book_list.html
                cart.html
                checkout.html
                login.html
                signup.html
        tests/
        __init__.py
        admin.py
        apps.py
        forms.py
        models.py
        urls.py
        views.py
    online_library/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    static/
    templates/
    db.sqlite3
    manage.py
    README.md
    requirements.txt
```



## User Authentication
<p>The application includes user authentication functionality that allows users to register, login, and logout. The authentication system uses Django's built-in authentication views and templates.</p>

* Registration: Users can register for an account by providing their email, username, and password. The application validates the email and username fields to ensure they are unique, and the password field is hashed and stored securely in the database.

* Login: Registered users can log in to the application using their email and password. The application checks the provided credentials against the database and grants access if they are valid.

* Logout: Logged-in users can log out of the application by clicking on the "Logout" button in the navigation bar.

## Book Search and Filtering
* Users can search for books by title or author name using the search bar on the home page. The application also includes filtering functionality that allows users to filter books by category, author, or publisher.


## Cart and Checkout
* Users can add books to their cart and checkout when they are ready to purchase. The application uses Django sessions to store the user's cart data.


## Admin Interface
* The application includes an administrative interface that allows administrators to manage books, categories, authors, and publishers. The admin interface uses Django's built-in admin views and templates.

* Books: Administrators can add, edit, and delete books using the admin interface. The admin interface provides a form where administrators can enter the book's details, including the title, author, publisher, publication date, category, cover image, and description.




## TODOS
* add ratings, maybe comments too
