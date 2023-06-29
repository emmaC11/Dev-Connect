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