## My Blog App

**A simple Flask-based blog app for my GitHub portfolio**

The My Blog App is a Flask project designed for personal study and portfolio enhancement on Python, Flask and Web. Employing SQLite for data storage and password encryption for security, it serves as a valuable showcase of skills, featuring user authentication, blog post management, and image 
handling functionalities.

![Photo Homepage](/myblog/static/Capturar.JPG)

## Description

This project is a simple blog app I created using the Flask framework to showcase my skills and knowledge for my GitHub portfolio. It features functionalities such as:

- User authentication and profile management
- Creation and editing of posts
- Upload and management of images for profile pictures and potentially blog posts (depending on implementation)
- Basic blog functionalities including a home page, post listings, and individual post pages

## Technologies Used

The following technologies were used in developing this app:

- **Backend:**
  - Python
  - Flask
  - SQLAlchemy
  - SQLite
- **Frontend:**
  - HTML
  - CSS
  - Bootstrap
- **Others:**
  - Git
  - GitHub

## Project Structure
The structure of the project, follows a common folder and file structure for Flask projects. Let's analyze each element:

![folder_image](/myblog/static/Capturar5.JPG)

- **Folders:**
  
  - myblog: It is the central project folder, everything is inside it. Contains the main file main.py that initializes the Flask application and configures its components.

  - static: Stores static files such as images, CSS, and JavaScript.

  - templates: Contains the HTML templates that define the user interface. This folder is responsible for show all webpages in this project. I used Python variables {{ abc }} and Python commands {% if abc %} to make all pages dynamic.


- **Files:**

  - init.py: Responsible to initialize all dependencies and create the app instance. It will be called automatic form main.py  
  
  - main.py: The main file that starts the Flask application and configures its components, such as routes, blueprints, and extensions. You must run this file to start the application.
  
  - forms.py: Defines the forms used in the application.
  
  - models.py: Defines the data models that represent the data in your application.

  - routes.py: Defines the application's routes, mapping URLs to specific functions.
  

## Project Functionality

The app utilizes Flask for routing and request handling. Here's a detailed analysis of some important functionalities achieved through provided code snippets:

**User Management:**

- Users can register for new accounts and log in using the `/login` route. This route handles login and account creation functionalities based on the submitted form button. Password hashing is implemented using bcrypt for security.
- The `/users` route (protected by login requirement) displays a list of all registered users.
- The `/profile` route displays the profile information of the current user, including their profile picture (if uploaded).
- The `/profile/edit` route allows users to edit their profile details such as username, email, and profile picture. It utilizes Flask-WTF forms for data validation and processing.

![phto_edit_profile](/myblog/static/Capturar4.JPG)
![phto_edit_profile](/myblog/static/Capturar3.JPG)



**Blog Postings:**

- The `/` route (home page) displays all blog posts in reverse chronological order (most recent posts first).
- The `/post/create` route allows authorized users to create new blog posts using a form.
- The `/post/<post_id>` route displays a specific blog post based on its ID. Additionally, if the current user is the author of the post, an edit form is provided to modify the post content.
- The `/post/<post_id>/delete` route allows authorized users to delete their own blog posts.

![photo_create`post](/myblog/static/Capturar2.JPG)

**Image Management:**

- The `save_photo` function assists in storing uploaded profile pictures for users. It generates a unique filename and resizes the image to a fixed dimension (200x200 pixels in this case) before saving it to the `photos_profile` directory.

**Additional Functionalities:**

- The `update_courses_list` function seems to be related to managing a user's courses, possibly for display on the profile. It extracts course selections from the profile edit form and stores them as a semicolon-separated string.



## Notes

- This is a basic blog app and can be further extended to include additional functionalities and features.
- The app is designed for educational purposes and should not be used in a production environment without proper security measures.


## License

This project is licensed under the MIT License.


