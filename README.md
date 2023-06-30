# Dev Connect
This platform connects developers and empowers innovation. Here, you can find resources, tips, and insights to enhance your coding journey. It is for developers of all stages/levels where we can all support eachother & grow together!

# **Table Of Contents**
* [User Experience & Design](#user-experience--design)
    * [User Stories](#user-stories)
        * [Structure](#structure)
    * [Design](#design)
        * [Colour Scheme](#colour-scheme)
        * [Typography](#typography)
        * [Wireframes](#wireframes)
* [Features](#features)
    * [Home](#home-screen)
    * [Post Content](#post-content)
    * [About](#about-section)
    * [Login](#login-section)
    * [Logout](#logout-section)
    * [Register](#register-section)

* [Testing](#testing)
    * [Validator Testing](#validator-testing)
    * [Responsive Testing](#responsive-testing)
    * [Lighthouse Testing](#lighthouse-testing)
    * [Manual Testing](#manual-testing)
    * [Bugs](#bugs-identified-during-development--testing)

* [Development Environment](#development-environment)
    * [Development Structure](#dev-structure)
* [Deployment](#deployment)
    * [Project Creation](#project-creation)
    * [Heroku Deployment](#heroku-deployment)

* [Credits/References](#creditsreferences)
    * [Technologies Used](#technologies-used)
    * [Content & Media](#content--media)
    * [Code](#code)

# **User Experience & Design**

# User Stories
* As a first time user, I want to create an account on dev connect.
* As a first time user, I want to login to my account on dev connect.
* As a first time user, I want to like posts on dev connect.
* As a first time user, I want to unlike posts on dev connect.
* As a first time user, I want to comment on posts on dev connect.
* As a first time user, I want to edit comments on posts on dev connect.
* As a first time user, I want to delete comments on posts on dev connect.
* As a first time user, I want to navigate between content on dev connect.
* As a first time user, I want to view the website on all my devices (Iphone 10, Surface Pro 7+, 32 inch monitor).
* As an admin user, I want to create new posts on dev connect.
* As an admin user, I want to  delete posts on dev connect.
* As an admin user, I want to delete comments posts on dev connect.

## Structure

The home screen of Dev Connect presents users with intuitive navigation options. Three prominent buttons are available, enabling users to perform different actions. Users can choose to create an account, log in to an existing account, or explore and interact with posts.
> As a first time user, I want to navigate between content on dev connect.

A user registration form is displayed when a user selects the 'register' button. This allows users to provide the required information and create their account on Dev Connect.
> As a first time user, I want to create an account on dev connect.

Users who already have an account can use the 'login' navigation option. This will direct them to the login page where they can enter their credentials and access their account.
> As a first time user, I want to login to my account on dev connect.

Users can engage with posts on Dev Connect by liking or unliking them. By selecting the 'like' icon, users can express their appreciation for a particular post. If they change their mind or mistakenly liked a post, they can click the like icon again to remove their like.
> As a first time user, I want to like posts on dev connect.
> As a first time user, I want to unlike posts on dev connect.

Dev Connect allows users to share their thoughts, ideas, and experiences by commenting on posts. By filling out the comment form located at the end of a post.
> As a first time user, I want to comment on posts on dev connect.

Users have the ability to edit & delete their comments on Dev Connect. By selecting the 'edit' or 'delete' button associated with their comment.
> As a first time user, I want to edit comments on posts on dev connect.
> As a first time user, I want to delete comments on posts on dev connect.

Dev Connect is designed to be responsive and compatible with various devices. The website was designed using Bootstrap to ensure all pages are responsive regardless of device/screen-size.
>  As a first time user, I want to view the website on all my devices (Iphone 10, Surface Pro 7+, 32 inch monitor).

Admin users have the capability to create new posts on Dev Connect. By accessing the django admin panel via the navigation bar, they can compose and publish posts with relevant content and information.
> As an admin user, I want to create new posts on dev connect.

Admin users also have the authority to delete posts & comments from Dev Connect. If a post violates community guidelines or is deemed inappropriate, an admin user can take action by selecting the 'delete' option associated with the post & comment.
> As an admin user, I want to  delete posts on dev connect.
> As an admin user, I want to delete comments posts on dev connect.

# Design
The website follows a minimalistic design approach for a more professional look. I took inspiration from simplistic websites such as - [Gazi Portfoltio](https://gazijarin.com/). It is an intuitive, easily navigatable website with a unique colour scheme that aims for an elegant, simplistic look.

## Colour Scheme
The website uses a deep nay colour palette with pops of green. The primary colours used throughout the website are navy (#0a192f), white (#be83f1), green (#e6f1ff), purple (#AA00FF) & grey (#8892b0) I wanted to try something different for my colour scheme, something that is not seen in mainstream everyday.

## Typography
Content throughout the site is with NTR google font. Headings have a '/' before the text for an aesthetic feel and visually appealing style.

## Wireframes
The wireframes were created using Balsamiq Wireframes. These were created before dev started so production site design may vary slightly to wireframes.
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/930ae297-3b27-4dd4-8c46-600f1d5a300e)
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/21f5a419-4e66-4e6a-8d74-f4f4cb512a2e)
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/89d16ebf-0688-4c46-b65a-9b780c31b938)
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/eca5acd7-1346-4b02-b811-47976a04faef)

## Database Model
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/1bf46703-cab5-4784-9761-8e9aff96a7de)

# **Features**
## Home Screen
* At the top of the page, their is a navigation bar that varies based on the users status.
* When a user is not logged in, the navigation displays 4 headings - home, about, login, register
* When a user is logged in, the navigation displays 4 headings - home, about, logout, admin.
* The logged in users username is dispayed on the right hand side with the sites slogan.
* The home screen displays a post list, each card contains the post heading & the category the post relates to, there are 5 categories: Interview tips/tricks, Coding Resources, Career Development, AI, Tech Explained.
* The post headings are displayed with thick green text with a deep navy background colour. The headings can be clicked to open the post. The text colour is white to make it visible over the dark background.
* Pagination is in place when there is over 9 posts being displayed on the screen.
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/0d0282a9-4801-4a45-a061-e4f12425bf45)

## Post Content
* A post can be opened by clicking the 'title' on the card within the homescreen.
* Each post displays the title, author, created on date, default image then the post content.
* Posts can be liked & unliked by logged in users
* Like icon is disabled when user is not logged in
* Logged in users can comment on posts, there is an input field where the user can enter the message/comment they want to post
* Logged in users can edit & delete their posts by selecting the buttons beside their own comments.
* Users can only edit & delete their own comments.
* Admin super user can edit & delete any comments using the buttons beside each comment(s).
& Admin super user can delete post from post list using the delete button postioned underneath the title. This functionality is only available to admin super user.
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/02c856be-93cb-476f-a7fc-350492d61262)
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/a682dff3-7eda-4965-81d3-c6aa6ecbd9db)
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/09557577-498e-4704-9c78-c3d814fa8ab8)

# About Section
* The about scetion gives the user information about the Dev Connect platform & how to use the site & it's functionalities. 
* It outlines the different post categories & the commenting guidelines.
* It follows the same colour scheme as the homepage
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/84864be9-cbf3-4020-9bf5-98ec516e3aaa)

# Login Section
The login page serves as the entry point for registered users. It prompts users to provide their login credentials, their username and password, to verify their identity and authorize access to Dev Connect functionalities.
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/637ad6a0-0cc7-47fa-b51a-991bafb8e07f)

# Logout Section
The logout page in Dev Connect allows authenticated users to log out of their accounts. When a user clicks the logout button, they are immediately logged out and redirected to the homepage.
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/05bd8b47-ca65-418f-b599-5031aa965772)

# Register Section
The register page in Dev Connect allows new users to create an account and join the platform. It provides a user-friendly interface where individuals can input their registration details and become registered members of the site.
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/56fe2227-db78-4706-8719-bfb90bae17c3)

# Admin Panel
The admin super user can add posts within the posts section. One thing to note is that the text content needs to be white to ensure it will be visible over the dark background. Post content can be edited here. Admins can create draft posts via admin panel. Posts & comments can be deleted via UI.

# **Testing**
## Validator Testing
* To verify that the HTML code was written to the best standard, I conducted validator testing with the W3C Markup Validator. I fixed the errors and warnings and currently there are no errors or warnings in the HTML code.
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/ce1b1495-346c-4fcb-a77e-b1a77fda0399)

* CSS styling was validated using the W3C CSS Validation Service to ensure the code was written to the expected standard. No errors were found when passing the code through the W3C CSS validator.
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/10c56d43-9114-46f7-8340-49031808409b)

I have used the PEP8 Linter to validate my code. It is activated within my code editor (Visual Studio Code). I had lots of 'lines too long' & 'whitespace' errors. I split lines where applicable, but I had to use #noqa (meaning line(s) is ignored by linters & validators) in settings.py as these lines could not be split without causing errors. I installed a [VS Extension](https://marketplace.visualstudio.com/items?itemName=shardulm94.trailing-spaces#:~:text=At%20any%20time%2C%20you%20can,type%20%22Trailing%20Spaces%3A%20Highlight%22) that highlights whitespace within the code. Throughout development I have been making tweaks to my code to ensure there are no errors. There are now no errros in my code. View the PEP8 documentation [here](https://peps.python.org/pep-0008/)

## Event Listener Testing
Event listener testing focuses on verifying the functionality and responsiveness of event listeners within a web application.
* All button clicks trigger an event on the site.
* Like buttons are disabled & not triggering events when user is not logged in. 

## Manual Testing
| Feature                 | Expect                                                 | Action             | Result            |
| -------------           | -------------                                          | ------------------ | -------           |
| Github Pages Deployment Link | When clicked the Dev Connect website opens in a tab on chosen browser  | Clicked deployment link in about section in GitHub Repo     | Website loaded sucessfully in tab |
| Website Responsiveness | When the website is viewed on different screen sizes, it is reponsive & resizes appropriately | Open chrome dev tools and toggle through each of the different screen sizes | Website was fully responsive |
| Navigation - home | When clicked the homepage is displayed to the user with post list | Clicked '/home' button | Homepage displayed with post list |
| Navigation - about | When clicked the about page is displayed to the user | Clicked '/about' button | About page is displayed |
| Navigation - login | When clicked the login page is displayed to the user | Clicked '/login' button | Login page is displayed |
| Navigation - register | When clicked the register page is displayed to the user | Clicked '/register' button | Register page is displayed |
| Display post - no account user | When post title is clicked the post content should display. Like button should be disabled & comment form not visible. | Clicked 'Job Positions in Tech'heading | Post is displayed, like & comment functionality is disabled |
| User Login | User fills out login form & is signed in successfully | Clicked '/login' button, typed username & password into input fields, click submit | User is logged in successfully, indicated by username visible in slogan |
| User Logout | User is logged out from account | Clicked '/logout' button in nav & form | User is logged out successfully, indicated by username not visible in slogan |
| User Login - empty username field | User fills out password field & login is not successful due to missing fields | Clicked '/login' button, typed password into input field, click submit | Form is not submitted, warning that username field needs to be filled out |
| User Login - incorrect password field | Login not successful due to incorrect password | Clicked '/login' button, typed username & incorrect password into input fields | Form is not submitted, warning stating the username and/or password you specified are not correct. |
| Register | New account created, user logged in sucessfully & has like & comment functionality | Clicked '/register' button, completed register form with relevant details | Form is submitted succesfully, new user account is created, like & comment functionality working on posts. |
| Register - existing username | New account created not created as username already exists in database | Clicked '/register' button, completed register form with username that is currently in db | Form is not submitted, warning stating that a user with that username already exists.|
| Like Posts | User can click like button on post & like count is incremented | Clicked '/login' button, entered credentials, clicked'Python 101' post, clicked like icon| Like button enabled, like count incremented|
| Comment | User can comment on post(s) | Clicked '/login' button, entered credentials, clicked 'Python 101' post, in comment body typed 'Does anyone have any Python resources they would recommend?'| Comment posted successfully.
| Comment - edit | User can edit their own comments | Clicked '/login' button, entered credentials, clicked 'Python 101' post, clicked edit button beside comment, alter text | Comment edited successfully. |
| Comment - edit & delete, other user | Users cannot edit or delete other users comments, buttons are hidden | Clicked '/login' button, entered credentials, clicked 'Job Positions in tech' post,| Comment cannot be edited or deleted, buttons are hidden |
| Comment - delete | User can delete their own comments | Clicked '/login' button, entered credentials, clicked 'Python 101' post, clicked delete button beside comment | Comment deleted successfully. |
| Admin Comment - edit | Admin user can edit comments within UI | Clicked '/login' button, entered admin credentials, clicked 'Python 101' post, clicked edit button beside comment, alter text | Comment edited successfully.|
| Admin Comment - delete | Admin user can delete comments within UI | Clicked '/login' button, entered admin credentials, clicked 'Python 101' post, clicked delete button beside comment | Comment deleted successfully.|
| Admin Post - delete posts| Admin user can delete posts within UI | Clicked '/login' button, entered admin credentials, clicked 'New Test Post' post, clicked delete button beneath title | Post deleted successfully.|
| Admin Post - draft post | Admin user can create posts within admin panel | Clicked '/login' button, entered admin credentials, clicked 'admin' in navigation bar, clicked add post button in blog section. Title: Test Post Author: admin Content: test post content Image: local image Cateogry: Developer Tips Status: Draft| Draft created successfully, not visible in post list on UI|
| Admin Post - published post | Admin user can create posts within admin panel | Clicked '/login' button, entered admin credentials, clicked 'admin' in navigation bar, clicked posts section & selected 'test post' to be edited. Changed status from draft to published| Post published successfully, visible in post list on UI|
| Admin Post - edit post | Admin user can create posts within admin panel | Clicked '/login' button, entered admin credentials, clicked 'admin' in navigation bar, clicked posts section & selected 'test post' to be edited. Changed content field| Post content edited successfully, visible in post list on UI|
| Pagination | Pagination feature is enabled when post list is greater than 9 | Clicked '/login' button, entered admin credentials, clicked 'admin' in navigation bar, clicked posts section & created 3 new test posts| Pagination displaying as expected, next & previous buttons visible|


## Responsive Testing
* The website was tested on several devices and screen sizes to ensure it was responsvie regardless of the screen size. It has been tested on desktop, Ipad Mini, Ipad Air, Iphone 5, Samsung Galaxy S8+, Iphone X, Iphone SE. Mobile devices have been tested in portrait and landscape mode. The site has been tested in Chrome, Edge, FireFox & Brave browsers.

## Lighthouse Testing
* The Lighthouse tool in Chrome DevTools is used to test a websites performance & accessibility. It is an open-source automated tool used to improve the quality of webpages. 
When I tested my website, an audit report was returned indicating that my website has high performance and is accessible.
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/2aa9a132-6c3a-4d07-8a3c-d1959a08ba0a)

## User Testing
The site has been tested regularly during development. After the site was completed I reached out to some fellow students & asks them to test the site & provide feedback.

## Event Listener Testing
* All button clicks trigger an event on the site.
* Like buttons are disabled & not triggering events when user is not logged in. 

## Bugs Identified During Development & Testing
* Site would not run locally as I did not have gitpod server in allowed_hosts.
* Heroku deployment was failing as I did not have commas inbetween installed_apps in settings.py.
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/4137e353-fa19-4462-ab38-aea9c7d003e2)
* Heroku deployment was failing as I did add the disable_collectstatic config var
* Missing capital latters when import django models
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/cab23185-3c00-44a2-a957-34d2af1b1a66)
* Missing endblock tags in html template, fixed by adding {%endblock%} tag at end of HTML code.
* Content from base.html was not displaying in index.html as I did not add block content tags to base.html
* Several times I forgot to close loops & if statements, best practise was going line by line to ensure the conditional or loop was closed when required,
* Posts were displaying vertically not horizontally, as I had an extra row class within my container.
* My style changes were not reflecting on my html files, as I did not clear cache & was using incorrect css path. I was not using Jinja syntax - {% static 'styles/style.css' %}
* When trying to install allauth & identify python version, I did not include '.' within slash & pip ../.pip-modules/lib.
* Some of my commit messages have spelling errors, however this is due to an issue with the bash terminal. I type the commit message correctly however it is changed after I confirm the commit.
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/a41f9e86-5a3b-4d27-94a5-99dfcc3cd5be)
* Some of my commit messages are way to vague, several commits have comments as I only realise after I complete a git push that several files & lines have been edited. Towards the end of dev, I used the source control feature within VS to write meaningful commit messages & see which files were edited.
* Delete comments & posts is not functional within admin panel. This is a UI feature.

# **Development Environment**
## Dev Structure
* The first step for this PP4 project was to come up with the project idea, I always liked the idea of a blog, but wanted to feel content with the site purpose. I enjoy watching fun tech related content on tiktok so this is where I decided to create a site with tech related content for junior developers.
* I then moved on to creating some wireframes. I have learned from previous projects that having a good plan before writing any lines of code is critical. I worked on the django walkthrough project & referenced that heavily in the early stages during project setup.
* I created my user stories within my onenote & some on GitHub issues.
* I kept a onenote notebook to log all notes from CI content, links etc associated with PP4. This help me keep track of what resources I used, masterclass notes & bugs tracked throughout the development cycle.

![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/28e89c50-4dc6-4bfe-af66-a6da0c5251a1)

# **Deployment**
## Project Creation
This project was created using Gitpod, Gitpod provides prebuilt development environments with a variety of IDEs. 

To use Gitpod, install the Gitpod extension on either Firefox or Chrome. When the extension is installed, it adds a green Gitpod button to Github, where we can click to create a workspace in Gitpod.

For this project, I used the Visual Studio IDE. I used the prebuilt environment provided by [Code Institue](https://github.com/Code-Institute-Org/gitpod-full-template) to start this project. I clicked the 'use this template' button and named my repository 'Dev-Connect'. I then created a Gitpod workspace by clicking the green gitpod button in my [Dev-Connect](https://github.com/emmaC11/Dev-Connect) repository.

I used the following commands throughout the development of this project:
* **python3 manage.py runserver**  - This command runs a local webserver to view the project.
* **git add .** - This command adds all the changes that have been in the working directory to the staging area. Ready to be committed.
* **git commit -m ""** - This command is used to write descriptive messages of what changes have been made to the code and commits the changes to the local repository.
* **git push** - This command pushes all the committed changes to the Github repository.
* **python3 manage.py migrate** - This command migrates any database model changes.
* **pip3 freeze --local > requirements.txt** - This command updates requirements.txt file after any installations.

## Heroku Deployment
1. Open Heroku & create a free account.
2. From the dashboard page, click the 'create new app' button.
3. Create an app name, this must be unique & choose your region (either America or Europe).
4. Go to [elephantsql.com](https://www.elephantsql.com/), login with GitHub and create a new instance.
5. Copy the URL once the project instance has been created. This value can also be saved with as environment variable used to equal the `DATABASES` variable in `settings.py`.
6. Install the `dj-database-url` package version 0.5.0 by using `pip3 install dj_database_url==0.5.0` to format the URL into one that Django can use, subsequently updating the `requirements.txt`.
7. Create a cloudinary account.
8. Copy the Cloudinary API URL from your dashboard.
9. Make sure to make any migrations in the project, by typing `python3 manage.py makemigrations` followed by `python3 manage.py migrate` into the terminal.
10. Ensure a `Procfile`, which contains `web: gunicorn [project_name].wsgi:application` is added to the project.
11. Please ensure the above steps are completed before deplyment, the build will fail if these are not followed.
12. Go back to Heroku and when the Project’s page opens up, go to the "settings" tab and scroll down to the “Config Vars” section. 
13. Enter the following key-valuen pairs in the “Config Vars” section: 
	* Key = `PORT` : Value = 8000
	* Key = `SECRET_KEY` : Value = Django Secret Key value obtained from `settings.py`
	* Key = `DATABASE_URL` : Value = ElephantSQL URL from point 5.
	* Key = `CLOUDINARY_URL` : Value = Cloudinary API URL from your Cloudinary account in point 9.
14. Go to the “Deploy” tab next and scroll down to the GitHub deployment method.
15. Search for the suitable repository and then connect to it by selecting the “Connect” button.
16. Scroll down to the bottom of the “Deploy” Page and select the type of deployment you want to conduct. If you opt to “Automatically Deploy”, it will deploy every time you push new code to your repository. Otherwise, you will have to manually deploy, by selecting the button at the bottom of the page.
17. The application is now deployed!

# **Credits/References**

## Technologies Used
* [Django Framework](https://www.djangoproject.com/#:~:text=Django%20is%20a%20high%2Dlevel,It's%20free%20and%20open%20source.)
* [Python](https://www.python.org/)
* [Heroku](https://dashboard.heroku.com/apps)
* [Cloudinary](https://cloudinary.com)
* [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) 
* [Google Fonts](https://fonts.google.com/)
* [Github](https://github.com/emmaC11/PP1-starwars)
* [GitPod](https://gitpod.io/)
* [Font Awesome](https://fontawesome.com/)
* [Lordicon](https://lordicon.com/icons/wired/outline?categoryId=3&premium=0)
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator)
* [W3C HTML Validator](https://validator.w3.org/#validate_by_input)

## Content & Media
* Animated folder icon in header is from [Lordicon](https://lordicon.com/icons/wired/outline?categoryId=3&premium=0)
* NRT font is imported from [Google Fonts](https://fonts.google.com/)
* Default [image](https://codeinstitute.s3.amazonaws.com/fullstack/blog/default.jpg) from CI blog

## Code
* I referenced the sample blog from [CI content]((https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+JSE_PAGPPF+2021_Q2/courseware/30137de05cd847d1a6b6d2c7338c4655/c3bd296fe9d643af86e76e830e1470dd/)), this provided helpful snippets throughout my project for layouts, views, models, etc
* I worked on a [personal project](https://github.com/emmaC11/ec-portfolio) a couple months ago which I referenced. The code used bootstrap & followed a similar design theme.
* I used chat-gpt to generate sample content for my site & to write content for readme. I also used it to troubleshoot different errors such as line too long & errors in views etc. It was very helpful when working on the edit comment feature.
* I referenced the following GitHub repo's throughout for guidance, VeganEat helped with the delete comment functionality. All wonderful ladies! [VeganEat](https://github.com/KarinOldbring/vegan-a-eat/tree/main),[F1 Booking System](https://github.com/Grawnya/f1-dublin-race-ticket-booking-system/tree/main#heroku-deploy), [Where-Next](https://github.com/AngMaher/PP4-Where-Next/)




