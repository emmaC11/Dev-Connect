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
    * [About](#about-screen)
    * [Post Content](#post-content)
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
    * [GitHub Pages](#deployment-to-github-pages)
    * [Run Locally](#run-locally)

* [Credits/References](#creditsreferences)
    * [Technologies Used](#technologies-used)
    * [Content & Media](#content--media)
    * [Code](#code)
    * [Achknowledgements](#achknowledgements)

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
Content throughout the site is with NTR google font.

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
* The home screen displays a post list, each card contains the post heading & the category the post relates to, there are 4 categories: Interview tips/tricks, Coding Resources, Career Development, AI, Tech Explained.
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
add content

## Manual Testing
add content

## Responsive Testing
* The website was tested on several devices and screen sizes to ensure it was responsvie regardless of the screen size. It has been tested on desktop, Ipad Mini, Ipad Air, Iphone 5, Samsung Galaxy S8+, Iphone X, Iphone SE. Mobile devices have been tested in portrait and landscape mode. The site has been tested in Chrome, Edge, FireFox & Brave browsers.

## Lighthouse Testing
* The Lighthouse tool in Chrome DevTools is used to test a websites performance & accessibility. It is an open-source automated tool used to improve the quality of webpages. 
When I tested my website, an audit report was returned indicating that my website has high performance and is accessible.
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/2aa9a132-6c3a-4d07-8a3c-d1959a08ba0a)

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
