# AutoMate – Portfolio Project 4

![A screenshot of the application in action](docs/repo-responsive.png)

## [Link to live web application](https://automate-pp4.herokuapp.com/)

---

## Project Documentation
### Welcome to [AutoMate](https://automate-pp4.herokuapp.com/)

---

## Table of Contents

-   [User Experience (UX)](#user-experience-ux)
    -   [Target Audiance](#target-audiance)
    -   [User Stories](#user-stories)
    -   [Typography](#typography)
    -   [Colour Palette](#colour-palette)
    -   [Wireframes](#wireframes)

- [Technical Design](#technical-design)
    -   [Flowchart](#flowchart)
    -   [Data Model](#data-model)

-   [Website Features](#website-features)
    -   [Application Elements](#application-elements)

-   [Future Features](#future-features) 

-   [Testing](#testing)
    -   [Manual Testing](#manual-testing)
        -   [User Stories Testing](#user-stories-testing)
    -   [Automated Testing](#automated-tests)
        -   [Unit Tests](#unit-tests)

-   [Validation](#validation)
    -   [HTML](#html)
    -   [CSS](#css)
    -   [JavaScript](#javascript)
    -   [Python](#python)

-   [Bug Fixes](#bug-fixes)

-   [Deployment](#deployment)
    -   [Local Deployment](#local-deployment)
    -   [Heroku Deployment](#heroku-deployment)

-   [Technologies Used](#technologies-used)
    -   [Hardware](#hardware)
    -   [Software](#software)
    -   [Platforms](#platforms)
    -   [Libraries](#libraries)
        -   [Local Libraries](#local-libraries)
        -   [Third Party Libraries](#third-party-libraries)

-   [Credits and References](#credits-and-references)
    -   [Repositories](#repositories)
    -   [Code Troubleshooting](#code-troubleshooting)
    -   [Documentation](#documentation)
    -   [Library Information](#library-information)
    -   [Theory](#theory)

-   [Acknowledgements](#acknowledgements)

-   [Closing Remarks](#closing-remarks)

---

## User Experience (UX)

### Target Audiance

This project primarily focuses on Irish youths who have recently acquired their full driving license and are in the market to purchase their first second-hand car.


### User Stories

#### User

`(MUST HAVE)`

- As a user I can view a contact us page that presents correspondence information so that I can contact the company for my queries.
- As a registered user I can edit the comments I posted so that I can change the content I originally posted in my comment.
- As a registered user I can click on a clearly labelled button so that I can add a post without having to navigate the site too much. 
- As a registered user I can use a dedicated form to edit my blog so that I can make changes to my content when I feel there is a need to do so.
- As a user I can click on a clearly labelled button on a blog card so that I am easily directed to the details of the relevant full blog post.
- As a user I can view all the newest posts on the website so that I can directly access the most up-to-date content available on the website.
- As a user I can view a paginated list of posts so that I easily select a post to view.
- As an unregistered user I can use a password and username I choose so that I can securely access the user-exclusive features of the website.
- As an unregistered user I can easily understand the features and purpose statement of the website on an initial look so that I more easily make a decision whether I am interested in creating an account or not.
- As an unregistered I can sign up to create an account so that I can fully access the features available on the website.
- As a registered user I can log out of my account so that I can securely quit the current session active on my device.
- As a registered user I can log in to my account so that I access the full functionality of the website.
- As a registered user I can delete my posts so that my published content is removed.
- As a registered user I can view posts from other users so that I can access and read content posted by others.
- As a registered user I can navigate the site so that I can interact with the available features.
- As a registered user I can create new posts so that I can share my thoughts and opinions on the platform.
- As a user I can view the consultation page so that I can learn about the various consultation service that the site offers.
- As a registered user I can expand posts so that more information is available to me to help me engage with the post.
- As a registered I can remove comments that I posted so that they are no longer visible on the site.
- As a registered I can leave comments on other users' blog posts so that I share my thoughts on the content they have posted.
- As a registered user I can like other people's posts so that I inform them that I had a positive experience with their posts.

`(SHOULD HAVE)`

- As a user I can be directed to an error page so that I know something went wrong with the website.
- As an admin I can view all submitted blog posts in the backend so that I can reject or approve posts depending on their compliance with community guidelines.
- As a user I can easily see how many comments a post accumulated without clicking into it so that I can decide whether it's worth checking out.
- As a user I can see special styling for particular usernames in comments so that I can identify which users are admins.
- As a user I can browse a website that incorporates overall cohesion among its various elements so that I have an aesthetically pleasing user experience.
- As a user I can browse profiles of cars on the website so that I can leave a comment to share my thoughts and experience relevant to a model that I choose.
- As a registered user I can like a post without having to wait for the website to refresh so that I can have a more cohesive and smooth experience when interacting with posts.
- As a user I can view the number of comments on any post so that I see if the post is popular or not and decide if it's worth checking out based on this information.
- As an unregistered user I can use single sign-on capabilities so that have a smoother authentication process before I can access the features of the site.
- As a registered user I want to be able to be notified if I do something wrong while creating a comment so that I can make sure that everything is as expected before I can publish my content.
- As a registered user I can make my profile private so that my personal information is reserved for specific people that I feel comfortable with sharing such information
- As a registered user I can clearly see date/time information on a post so that I learn how old or new the post is to determine its relevance.

`(COULD HAVE)`

- As a user I can use the calculator functionality so that I get a rough idea about whether it's viable for me to finance a car purchase.
- As a user I can view the location of the HQ of the site so that I decide if I want to have a visit for networking.
- As a registered user I can message other users so that I can establish private communication with other users on the site.
- As a registered I can receive notifications when I get new followers so that I can check their profile.
- As a registered user I can receive notifications about any new likes and comments on my content so that I am informed of the engagement of my posts.
- As a registered user I can search for any user or post so that I can easily find the content and people that I am interested in.

`(WON'T HAVE)`

- As a registered user I can be notified of incoming correspondence from other users so that I can read their messages and decide if I want to reply back to them.
- As a registered user I can create my profile so that other users can identify me.
- As a registered user I can reset my password so that I can regain access to my account if I forget my password.
- As a registered user I can add a profile picture and cover photo so that I can further personalize my profile.
- As a registered user I can edit my profile so that I can personalize my profile.
- As a registered user I can follow other users so that I can see their blog posts.
- As a registered user I can unfollow users so that their posts are no longer visible on my feed.


#### Admin

`(MUST HAVE)`


- As an admin I can provide a disclaimer at the bottom of the page so that I can specify that all outsourced content (texts, images etc.) is used for purposes of education as a part of this academic project and is in no circumstance to be used for commercial motivations. 
- Deploy project to Heroku before the start of the production process to prevent major issues in this area considering later stages.
- As an admin I can approve or reject comments left by registered users so that I can ensure that the content available on the site follows the community guidelines.
- As an admin I can create draft posts so that I can come back to them when I want to.
- As an admin I can create, read, update and delete posts so that *I can manage my blog content.


`(SHOULD HAVE)`


- As an admin I can suspend a user's access to site functionality if required so that I can prevent them from violating any major community guidelines and ensure a safe space for the site's users.

`(COULD HAVE)`

- As an admin I can view all reported content by users so that I can make decisions on whether content removal and user punishment are necessary or not.
- As a registered user I can report posts that I find inappropriate in terms of site community guidelines so that such content is communicated to admins and appropriate measures are taken, ensuring an overall positive experience on the site.


### Typography

- [Bitter](https://fonts.google.com/specimen/Bitter) is the primary font that is present across all textual elements present in the project.

- [Sans Serif](https://fonts.google.com/knowledge/glossary/sans_serif) is the fallback font set in case the primary font fails.

- [Font Awesome](https://fontawesome.com) is the source for the various icons used to decorate the textual content available in the project.


### Colour Palette

[Coolors](https://coolors.co/) was a highly beneficial resource that provided significant help in identifying matching colours that also have appropriate contrast.

More importantly, this colour combination consists of items designed to motivate excitement from users through the use of vivid colour tones contrasted by darker colours to balance the overall feel of the design.

![Colour Palette](docs/color-palette.png)

---

### Wireframes

<details>

<summary>Home Page</summary>

#### Mobile
![screenshot](docs/wireframes/ios-home.png)

#### Tablet
![screenshot](docs/wireframes/ipad-home.png)

#### Desktop
![screenshot](docs/wireframes/desktop-home.png)

</details>

<details>

<summary>Blog Page</summary>

#### Mobile
![screenshot](docs/wireframes/ios-blog.png)

#### Tablet
![screenshot](docs/wireframes/ipad-blog.png)

#### Desktop
![screenshot](docs/wireframes/desktop-blog.png)

</details>

<details>

<summary>Consultation Page</summary>

#### Mobile
![screenshot](docs/wireframes/ios-consultation.png)

#### Tablet
![screenshot](docs/wireframes/ipad-consultation.png)

#### Desktop
![screenshot](docs/wireframes/desktop-consultation.png)

</details>

<details>

<summary>Forms Page</summary>

#### Mobile
![screenshot](docs/wireframes/ios-forms.png)

#### Tablet
![screenshot](docs/wireframes/ipad-forms.png)

#### Desktop
![screenshot](docs/wireframes/desktop-forms.png)

</details>

<details>

<summary>Login Page</summary>

#### Mobile
![screenshot](docs/wireframes/ios-login.png)

#### Tablet
![screenshot](docs/wireframes/ipad-login.png)

#### Desktop
![screenshot](docs/wireframes/desktop-login.png)

</details>

<details>

<summary>Sign Out Page</summary>

#### Mobile
![screenshot](docs/wireframes/ios-signout.png)

#### Tablet
![screenshot](docs/wireframes/ipad-signout.png)

#### Desktop
![screenshot](docs/wireframes/desktop-signout.png)

</details>

<details>

<summary>Blog Detail Page</summary>

#### Mobile
![screenshot](docs/wireframes/ios-blog-detail.png)

#### Tablet
![screenshot](docs/wireframes/ipad-detail.png)

#### Desktop
![screenshot](docs/wireframes/desktop-detail.png)

</details>

---

## Technical Design

### Data Model - Entity Relationship Diagram

[Draw.io](https://www.drawio.com/) was a highly beneficial resource that provided significant help in building a ERP to illustrate the various table relationships of data models present in the project.

![Data Relationship Diagram](docs/entity-relationship-diagram.png)

---

## Website Features

The design considerations that impacted the envisioned features were mainly structured around user interaction and content sharing. While there were more features planned in the initial stages of the project, some were not entertained to the benefit of serving the needs referenced in the [User Stories](#user-stories) section. Thus, it was important to focus on a minimum viable project rather than prioritizing the implementation of further features for the sake of it. This would only bloat the application without adding much real value to the user experience overall. There are [records available](#future-features) as a part of this documentation that demonstrate the change in scope that took place moving further into development.

### Application Elements

The below elements are available to be experienced by the user across the application as a whole.

| Feature | Screenshot |
| --- | --- |
| Site Logo | ![screenshot](docs/features/site-logo.png) |
| Favicon | ![screenshot](docs/features/custom-favicon.png) |
| Default Post Banner | ![screenshot](docs/features/default-post-banner.png) |
| Custom Login Banner | ![screenshot](docs/features/login-banner-custom.png) |
| Navigation (Logged in) | ![screenshot](docs/features/sitenav-1.png) |
| Navigation (Logged Out) | ![screenshot](docs/features/sitenav-2.png) |
| Sign Up | ![screenshot](docs/features/signup.png) |
| Messages | ![screenshot](docs/features/messages.png) |
| Logout | ![screenshot](docs/features/logout.png) |
| Login | ![screenshot](docs/features/login.png) |
| Footer | ![screenshot](docs/features/footer.png) |
| Featured Blogs | ![screenshot](docs/features/featured-blogs.png) |
| Comment Content Editing | ![screenshot](docs/features/edit-comment.png) |
| Blog Content Editing | ![screenshot](docs/features/edit-blog.png) |
| Application Content Editing | ![screenshot](docs/features/edit-apply.png) |
| Post Deletion | ![screenshot](docs/features/delete-post.png) |
| Comment Deletion | ![screenshot](docs/features/delete-comment.png) |
| Application Deletion | ![screenshot](docs/features/delete-apply.png) |
| Comment Form | ![screenshot](docs/features/comment-form.png) |
| No Comments Placeholder | ![screenshot](docs/features/comment-0.png) |
| Home Page Carousel | ![screenshot](docs/features/carousel.png) |
| Blog Sidebar | ![screenshot](docs/features/add-post.png) |
| Blog Sidebar | ![screenshot](docs/features/blog-sidebar.png) |
| Blog Posts | ![screenshot](docs/features/blog-posts.png) |
| Blog Content | ![screenshot](docs/features/blog-content.png) |
| Blog Buttons | ![screenshot](docs/features/blog-buttons.png) |
| Blog Banner Image | ![screenshot](docs/features/blog-banner.png) |
| Application Summary | ![screenshot](docs/features/apply-summary.png) |
| Application Guide | ![screenshot](docs/features/apply-info.png) |
| Application Page (Logged In) | ![screenshot](docs/features/apply-1.png) |
| Add Application **(DISCLAIMER: The phone field will not accept any random combination of numbers that match the selected area number format. It needs to be a real number because of the security features that come with PhoneNumberField library.)** | ![screenshot](docs/features/add-apply.png) |
| Custom 500.html Page | ![screenshot](docs/features/custom-500.png) |
| Custom 404.html Page | ![screenshot](docs/features/custom-404.png) |
| Custom 403.html Page | ![screenshot](docs/features/custom-403.png) |
| Custom 400.html Page | ![screenshot](docs/features/custom-400.png) |

---

## Future Features

This section documents the features that were taken out of consideration for the benefit of the completion of the minimum viable project. The central observation in this area is that the level of ambition that the project initially set out with does not match with the intellectual labour required to complete a significant sum of the features first assigned. Below, are user stories that were deemed no longer necessary. You can view the full kanbar board used for project planning [here](https://github.com/users/beratzorlu/projects/4/views/1).

That being said, these features remain relevant to the overall scope of the project and it would see them expand its functional capacity in the future if the situation allowed it.

| Label | Feature |
| --- | --- |
| Won't Have | Direct Messaging |
| Won't Have | Unfollow Users |
| Won't Have | Admin/Inappropriate Blog Posts#52 |
| Won't Have | Car Finance Calculator#41 |
| Won't Have | Car Profile#40 |
| Won't Have | Comments/Post Card Comment Count#51 |
| Won't Have | Contact Us/Google Maps and Marker Clusterer#33 |
| Won't Have | Background Refresh For Post Likes#32 |
| Won't Have | Authentication/SSO#30 |
| Won't Have |  Profiles/Private Profiles#28 |
| Won't Have | Admin/Suspend Users#27 |
| Won't Have | Direct Messaging/Notifications#26 |
| Won't Have | Admin/View Reported Posts#24 |
| Won't Have | Post Report#23 |
| Won't Have | Follow Users#6 |
| Won't Have | Notifications/New Follower#22 |
| Won't Have | Notifications/Post Engagement#21 |
| Won't Have | Search Users & Posts#20 |
| Won't Have | Password Reset#9 |
| Won't Have | Profiles/Create Profile#13 |
| Won't Have | Profiles/Edit Profile#7 |

---

## Testing

### Automated Testing

#### Unit Tests

| Scope | Screenshot | Result |
| --- | --- | --- |
| Global | ![screenshot](docs/validation/python/unittest.png) | Pass |

### Manual Testing

#### User Stories Testing

| **Feature**   |  **Screenshot**          | **Result** |
| ------------- | ------------------------ | ----------------- |
| As an admin I can provide a disclaimer at the bottom of the page so that I can specify that all outsourced content (texts, images etc.) is used for purposes of education as a part of this academic project and is in no circumstance to be used for commercial motivations. | ![screenshot](docs/features/footer.png) | Pass |
|  As a user I can browse a website that incorporates overall cohesion among its various elements so that I have an aesthetically pleasing user experience. | ![screenshot](docs/features/carousel.png) | Pass |
| As a user I can be directed to an error page so that I know something went wrong with the website. | ![screenshot](docs/features/custom-404.png) | Pass (This is valid for all custom error pages.) | 
| As a user I can view all the newest posts on the website so that I can directly access the most up-to-date content available on the website. | ![screenshot](docs/features/blog-posts.png) | Pass |
| As a user I can view the consultation page so that I can learn about the various consultation service that the site offers. | ![screenshot](docs/features/apply-1.png) | Pass |
| As a registered I can remove comments that I posted so that they are no longer visible on the site. | ![screenshot](docs/features/delete-comment.png) | Pass |
| As a registered user I can edit the comments I posted so that I can change the content I originally posted in my comment. | ![screenshot](docs/features/edit-comment.png) | Pass |
| As a registered user I can create new posts so that I can share my thoughts and opinions on the platform. | ![screenshot](docs/features/add-post.png) | Pass |
| As a registered user I can use a dedicated form to edit my blog so that I can make changes to my content when I feel there is a need to do so. | ![screenshot](docs/features/edit-blog.png) | Pass |
| As a registered user I can delete my posts so that my published content is removed. | ![screenshot](docs/features/delete-post.png) | Pass |
| As a user I can view the number of comments on any post so that I see if the post is popular or not and decide if it's worth checking out based on this information. | ![screenshot](docs/features/blog-banner.png) | Pass |
| As a registered user I can view posts from other users so that I can access and read content posted by others. | ![screenshot](docs/features/blog-list-1.png) | Pass |
| As a registered user I can like other people's posts so that I inform them that I had a positive experience with their posts. | ![screenshot](docs/features/blog-banner.png) | Pass |
| As a user I can see special styling for particular usernames in comments so that I can identify which users are admins. | ![screenshot](docs/features/admin-crown.png) | Pass |
| As a registered user I can clearly see date/time information on a post so that I learn how old or new the post is to determine its relevance. | ![screenshot](docs/features/blog-banner.png) | Pass |
| As an unregistered I can sign up to create an account so that I can fully access the features available on the website. | ![screenshot](docs/features/signup.png) | Pass |
| As a registered I can leave comments on other users' blog posts so that I share my thoughts on the content they have posted. | ![screenshot](docs/features/comment-form.png) | Pass |
| As a registered user I can log out of my account so that I can securely quit the current session active on my device. | ![screenshot](docs/features/logout.png) | Pass |
| As a registered user I can log in to my account so that I access the full functionality of the website. | ![screenshot](docs/features/login.png) | Pass |
| As an unregistered user I can use a password and username I choose so that I can securely access the user-exclusive features of the website. | ![screenshot](docs/features/signup.png) | Pass |
| As a user I can click on a clearly labelled button on a blog card so that I am easily directed to the details of the relevant full blog post. | ![screenshot](docs/features/featured-blogs.png) | Pass |
| As a registered user I can navigate the site so that I can interact with the available features. | ![screenshot](docs/features/sitenav-1.png) | Pass |
| As an admin I can approve or reject comments left by registered users so that I can ensure that the content available on the site follows the community guidelines. | ![screenshot](docs/features/comments-approve.png) | Pass |
| As an admin I can create draft posts so that I can come back to them when I want to. | ![screenshot](docs/features/post-draft.png) | Pass |
| As an admin I can create, read, update and delete content so that I can manage my blog content. | ![screenshot](docs/features/admin-content-manage.png) | Pass |

---

## Validation

### HTML

| Page | Screenshot | Result |
| --- | --- | --- |
| Home | ![screenshot](docs/validation/html/w3c-index.png) | Pass |
| Blog | ![screenshot](docs/validation/html/w3c-blog.png) | Pass |
| Consultation | ![screenshot](docs/validation/html/w3c-apply.png) | Pass |
| Login | ![screenshot](docs/validation/html/w3c-login.png) | Pass |
| Logout | ![screenshot](docs/validation/html/w3c-logout.png) | Pass |
| Signup | ![screenshot](docs/validation/html/w3c-signup.png) | Pass |
| Add Post | ![screenshot](docs/validation/html/w3c-add-post.png) | Pass |
| Edit Post | ![screenshot](docs/validation/html/w3c-edit-post.png) | Pass |
| Add Consultation | ![screenshot](docs/validation/html/w3c-add-app.png) | 1 Error: Caused by widget properties set for the DateTimeField. This input field needs a placeholder, thus the error is allowed to remain. |
| Edit Consultation | ![screenshot](docs/validation/html/w3c-edit-app.png) | Pass |

### CSS

| File | Screenshot | Result |
| --- | --- | --- |
| style.css | ![screenshot](docs/validation/css/jigsaw-css.png) | Pass |

### JavaScript

| File | Screenshot | Result |
| --- | --- | --- |
| fade.js | ![screenshot](docs/validation/js/jshint.png) | Pass (It is not possible to install Bootstrap in jshint, thus the warning is allowed to remain.) |

### PYTHON

| File | Screenshot | Result |
| --- | --- | --- |
| urls.py (main) | ![screenshot](docs/validation/python/linter-urls-main.png) | Pass |
| settings.py (main) | ![screenshot](docs/validation/python/linter-settings.png) | Pass |
| admin.py (blog) | ![screenshot](docs/validation/python/linter-admin-blog.png) | Pass |
| forms.py (blog) | ![screenshot](docs/validation/python/linter-forms-blog.png) | Pass |
| tests.py (blog) | ![screenshot](docs/validation/python/linter-tests-blog.png) | Pass |
| urls.py (blog) | ![screenshot](docs/validation/python/linter-urls-blog.png) | Pass |
| views.py (blog) | ![screenshot](docs/validation/python/linter-views-blog.png) | Pass |
| admin.py (consultation) | ![screenshot](docs/validation/python/linter-admin-consultation.png) | Pass |
| cars.py (consultation) | ![screenshot](docs/validation/python/linter-cars-consultation.png) | Pass |
| forms.py (consultation) | ![screenshot](docs/validation/python/linter-forms-consultation.png) | Pass |
| models.py (consultation) | ![screenshot](docs/validation/python/linter-models-consultation.png) | Pass |
| tests.py (consultation) | ![screenshot](docs/validation/python/linter-tests-consultation.png) | Pass |
| urls.py (consultation) | ![screenshot](docs/validation/python/linter-urls-consultation.png) | Pass |
| views.py (consultation) | ![screenshot](docs/validation/python/linter-views-consultation.png) | Pass |

---

## Bug Fixes

In this section, all bugs that cased errors that prevented the successful execution of the application and their relevant fixes are provided.

| **Bug** | **Fix** |
| ------- | ------- |
| SyntaxError on STATIC_ROOT variable. | [here](https://github.com/beratzorlu/AutoMate/commit/70e0273a16c29968d5ed463f5bb69cf63e9aba7e). |
| Alignment issue for like and comment icons. | [here](https://github.com/beratzorlu/python-quiz/commit/d3fc300dc47d88aecd65f99b7ab7cbb6ca6f13b7). |
| Comment textfield issue.  | [here](https://github.com/beratzorlu/AutoMate/commit/11c99d53f14d9b4e536b8c5522019e194061ab74) |
| Delete blog button positioning issue.  | [here](https://github.com/beratzorlu/AutoMate/commit/306849d24d314e52ec4e2bd863d3d56942024e76) |
| Post detail render issue when logged in as admin.  | [here](https://github.com/beratzorlu/AutoMate/commit/0c606ba4cf32c5a625d95201eff7f06da745ee79) |
| Unresponsive footer. | [here](https://github.com/beratzorlu/AutoMate/commit/e4d1d7a1d1ffe802e82cacfbc4a05d11dc054a30) |
| Consultation frontend render issue. | [here](https://github.com/beratzorlu/AutoMate/commit/4b531cbddf683782b7168eb66540b3f1bc9e3815) |
| Consultation form loop render issue. | [here](https://github.com/beratzorlu/AutoMate/commit/c7dbc7f8b35e05e3d286e784872b67a9883f6199) |
| Card wrap issue. | [here](https://github.com/beratzorlu/AutoMate/commit/162b2bfff80a1ad3b22ee7ec3db0cb2bf798da4c) |
| Application summary card render issue. | [here](https://github.com/beratzorlu/AutoMate/commit/3b5a304272b4be5ea19373b8770ff78d0a9f56ef) |
| Edit view frontend content update issue. | [here](https://github.com/beratzorlu/AutoMate/commit/4848f1c68c68774a8ae5dfb947346e9f35a0de50) |
| cars.py import issue. | [here](https://github.com/beratzorlu/AutoMate/commit/4757863be79691120d3a7a9f841f49b6ebca4b93) |
| ID text capitalization issue. | [here](https://github.com/beratzorlu/AutoMate/commit/dd9bc150e39562fb02b4859dbd776797e222f288) |
| Comment security issue. | [here](https://github.com/beratzorlu/AutoMate/commit/23528285f3d115745b90ccd1e67c005294272159) |
| author_id Null value issue. | [here](https://github.com/beratzorlu/AutoMate/commit/0c0e5e0280444d6805c48daf89c7f92d087b6e3e) |
| Blog page responsivity issue. | [here](https://github.com/beratzorlu/AutoMate/commit/7b054286b982038cca277428d6955ce95a201ac8) |

---

## Deployment

This application has been deployed by using the Heroku cloud platform. Please find below the neccessary procdures to replicate the deployment process.

You can find a [template](https://github.com/Code-Institute-Org/python-essentials-template) prepared by Code Institute that is designed to display this backend application in a modern web browser. This allows the project to be accessible for users without the need of any third party software other than an Internet browser application.

### Local Deployment 

Gitpod IDE is the development environment for this project.

If you wish to make copy of this repository locally, you can clone it by inputting the following code into your preferred integrated development environment (IDE):
- `git clone https://github.com/beratzorlu/python-quiz.git`

As anoher method, you can click below button to create your own workspace using this repository if you are using Gitpod.e

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/beratzorlu/python-quiz)

### Heroku Deployment

This project utilizes the services available at [Heroku](https://www.heroku.com). Heroku is a platform as a service (PaaS) that allows users to build, deploy, and control applications in a cloud environment.

Disclaimer: To be able successfully replicate the Heroku deployment process, it is highly reccomended that users setup an account on the platform prior to following the steps provided below.

- Select *New* in the top-right corner of your Heroku Dashboard after log-in.
- Select navigate to the *Create new app* button from the dropdown menu and select it.
- Assign a unique name to your application.
- Navigate to the *region* dropdown menu and select the region closest to you from either EU or USA. 
- Select *Create App*.
- Navigate to your newly created application and select *Settings*. 
- Click *Reveal Config Vars*.
- Add first *Config Var*.
- Set the value of KEY to `CREDS`, copy and paste the data in your credentials file (ie. creds.json) into the value area.
- Add second *Config Var*.
- Set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- You need to add support to dependencies to be able to successfully deploy application, select *Add Buildpack*.
- The order in which you list your dependencies is critical, select `Python` as the first dependency.
- From the same menu, select `Node.js` after you select `Python`. (You can drag the list items upwards and downwards to change their order if needed.)
- Scroll until you find your desired deployment method, select `Enable Automatic Deploy` to rebuild your project automatically every time you push a new commit. Select `Manual Deployment` to manually deploy from your desired branch on will.*

*If you have selected automatic deployment, your application will only deploy after your first push to the system.

After the completion of this process, Heroku needs two files further to deploy successfully. These are;
    - requirements.txt
    - Procfile

To install your project's requirements use: `pip3 install -r requirements.txt`. 

If you have third party packages in your project the requirements file needs updated, use: `pip3 freeze --local > requirements.txt`

To create your Procfile, use: `echo web: node index.js > Procfile`

For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:

- In the Terminal (CLI), connect to Heroku using this: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a <app_name>` (replace <app_name> with your chosen name for your application without the angle-brackets)
- Input commands `git add`, `git commit`, and `git push` to GitHub sequentially.
- Finally, type `git push heroku main` in the terminal to connect to Github.

Alternatively, you can connect to your Github account by following the below steps on Heroku's platform.

- Navigate to your Heroku account dashboard.
- Find the relevant project and click on its icon.
- On the next page, navigate to the `Deploy` subsection.
- Scroll down until you find `Deployment method` and find `Use Github`.
- Finally, input your Github account credentials to complete the process. 

---

## Technologies Used

### Hardware

- Monster Abra A5 V13.4 15.6" Laptop
- Lenovo IdeaPad 3i 14" Laptop
- Samsung VA 1920x1080 144Hz Curved Gaming Monitor
- iPhone 11
- Ipad Air 5th Generation
- Samsung A51

### Software

- Mozilla Firefox: Main browser used for development, testing and device simulation.
- Google Chrome: Secondary browser for testing and device simulation.
- Microsoft Edge: Tertiary browser for testing.
- Firefox Mobile: Mobile testing of the deployed site.
- Chrome Mobile: Mobile testing of the deployed site.
- Safari Mobile: Mobile testing of the deployed site.
- Windows Snip & Sketch: Capturing screenshots for readme and archiving identified bugs.
- Microsoft Snipping Tool: Fallback screen capture software when MS Snip & Sketched became unresponsive.
- DiffChecker: Comparing code to identify issues, solutions and ideas.
- Python Checker: Checking the syntax of Python code.
- ElephantSQL: PosgresSQL database resource.
- Django: Fullstack framework used to build the project
- Bootstrap: Responsive frontend CSS framework used to design the visual aspects of the project.
- Cloudinary: Cloud storage for static files.
- Balsamiq: Wireframe design and rendering.
- Draw.io: Diagram design and rendering.

### Platforms

- GitHub: Version control and site deployment.
- GitPod: Integrated Development Environment (IDE) chosen for this project.
- Google Fonts: Finding and exporting third-party fonts for the website.
- CodePen: For quickly testing out ideas before carrying them to 
DevTools.
- Coolors: For creating a matching colour palette that has appropriate contrast.
- Heroku: Cloud platform used for deploying project.
- Canva: Graphic design platform used for custom visual elements.

### External Modules

| **Name** | **Version** |
| ------- | ------- |
| asgiref | 3.6.0 |
| Babel | 2.12.1 |
| cloudinary | 1.32.0 |
| dj-database-url | 0.5.0 |
| dj3-cloudinary-storage | 0.0.6 |
| Django | 3.2.18 |
| django-allauth | 0.54.0 |
| django-crispy-forms | 1.14.0 |
| django-phonenumber-field | 7.1.0 |
| django-summernote | 0.8.20.0 |
| gunicorn | 20.1.0 |
| oauthlib | 3.2.2 |
| phonenumbers | 8.13.11 |
| psycopg2 | 2.9.6 |
| PyJWT | 2.6.0 |
| python3-openid | 3.2.0 |
| pytz | 2023.3 |
| requests-oauthlib | 1.3.1 |
| sqlparse | 0.4.4 |

---

## Credits and References

### Repositories

- [Code Institute](#): CI's curriculum provided the main knowledge-base required to create and finalize this project. Various academic modules and the tasks available in them helped understand Django before the start of the development process.
    - [Hello Django](#): This walkthrough project provided significant practice for understanding how to implement CRUD functionality to a Django application.
    - [I Think Therefore I Blog](#): While more difficult to fully understand, the concepts demonstrated in this walkthrough project allowed for a deeper understanding of Django admin and site operations. More specifically, pagination was a difficult element to fully implement to this project. The code available here provided the help needed to integrate a pagination system to the project.
- [adamgilroy](https://github.com/adamgilroy22/tribe/): This was an inspirational project that offers an expansive set of features. Beacuse of this I would like to congratualte Adam Gilroy for his excellent work. Reading through his code helped me understand how to compartmentalize code, add security against unauthorized access to published user content, and how to work class based views.
- [CHCheshire](https://github.com/CHCheshire/Project-blog/tree/main): This project helped me understand managing comments from the frontend when building associated CRUD functionality.
- [stephaniecrocker91](https://github.com/stephaniecrocker91/for-the-love-of-food): This project provided a live perspective towards connecting models from different applications with each other.


### Code Troubleshooting

| Source | Title | URL |
| --- | --- | --- |
| Stack Overflow | delete button | [here](https://stackoverflow.com/questions/68008514/how-i-can-create-a-delete-button-in-django-python) |
| Stack Overflow | delete button #2 | [here](https://stackoverflow.com/questions/46003056/how-to-make-delete-button-in-django) |
| Stack Overflow | backport version issue | [here](https://stackoverflow.com/questions/71712258/error-could-not-build-wheels-for-backports-zoneinfo-which-is-required-to-insta) |
| Stack Overflow | bootstrap header width | [here](https://stackoverflow.com/questions/72279036/why-is-my-boostrap-card-header-not-filling-entire-width-of-the-card) |
| Stack Overflow | bootstrap grid and aside usage | [here](https://stackoverflow.com/questions/36161615/bootstrap-grid-with-html5-sections-and-aside ) |
| Stack Overflow | ajax for liking without page refresh | [here](https://stackoverflow.com/questions/21791037/implement-a-like-this-button-in-django-without-refreshing-page) |
| Stack Overflow | django import js documents | [here](https://stackoverflow.com/questions/30313314/django-how-to-include-javascript-in-template) |
| Stack Overflow | centering cards | [here](https://stackoverflow.com/questions/39031224/how-to-center-cards-in-bootstrap-4) |
| Stack Overflow | center button | [here](https://stackoverflow.com/questions/41664991/bootstrap-4-how-do-i-center-align-a-button) |
| Stack Overflow | prepopulate author dropdown on addpost | [here](https://stackoverflow.com/questions/45221097/add-data-to-django-form-before-it-is-saved/45221181#45221181) |
| Stack Overflow | best image size for bootstrap | [here](https://stackoverflow.com/questions/25554020/bootstrap-carousel-with-photos-optimal-image-size) |
| Stack Overflow | django dropdown | [here](https://stackoverflow.com/questions/31130706/dropdown-in-django-model) |
| Stack Overflow | HTTP referrer | [here](https://stackoverflow.com/questions/4406377/django-request-to-find-previous-referrer) |
| Stack Overflow | unittests | [here](https://stackoverflow.com/questions/51560850/how-to-unit-test-a-post-method-in-python) |
| Stack Overflow | django phonenumberfield | [here](https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-a-phone-number-in-django-models) |
| Stack Overflow | remove crispyforms labels | [here](https://stackoverflow.com/questions/11472495/remove-labels-in-a-django-crispy-forms) |
| Stack Overflow | carousel not working fix | [here](https://stackoverflow.com/questions/48824568/bootstrap-4-carousel-sliders-not-working) |
| Stack Overflow | import django forms | [here](https://stackoverflow.com/questions/56785003/attribute-error-module-django-forms-forms-has-no-attribute-modelform) |
| Stack Overflow | django equalto method | [here](https://stackoverflow.com/questions/20529234/how-to-select-reduce-a-list-of-dictionaries-in-flask-jinja) |
| Stack Overflow | django count of list item | [here](https://stackoverflow.com/questions/40006617/get-count-of-list-items-that-meet-a-condition-with-jinja2) |
| Stack Overflow | only available as class instances issue | [here](https://stackoverflow.com/questions/48613146/python-error-this-method-is-only-available-to-the-class-not-on-instances) |
| Stack Overflow | editing posts on django blog | [here](https://stackoverflow.com/questions/60042351/editing-posts-in-a-django-blog) |
| Stack Overflow | default value set on form | [here](https://stackoverflow.com/questions/70559902/django-how-do-i-set-a-default-value-in-a-form-to-be-the-current-user) |
| Stack Overflow | tuple error indices | [here](https://stackoverflow.com/questions/35359969/typeerror-tuple-indices-must-be-integers-not-str) |
| Stack Overflow | assign default value | [here](https://stackoverflow.com/questions/23718484/django-assign-default-value-to-field-in-modelform) |
| Stack Overflow | placeholder charfield | [here](https://stackoverflow.com/questions/4101258/how-do-i-add-a-placeholder-on-a-charfield-in-django) |
| Stack Overflow | change date format field | [here](https://stackoverflow.com/questions/67538930/how-to-change-date-format-in-a-form-field-django) |
| Stack Overflow | date placeholder | [here](https://stackoverflow.com/questions/39025926/dateinput-how-to-show-placeholder) |
| Stack Overflow | date picker widget | [here](https://stackoverflow.com/questions/41645030/django-date-picker-for-date-of-birth) |
| Stack Overflow | limit blog posts per account – class context method – Django pagination | [here](https://stackoverflow.com/questions/68405198/adding-a-maximum-limit-to-the-number-of-post-using-python) |
| Stack Overflow | dispatch - loginrequired | [here](https://stackoverflow.com/questions/71782596/why-loginrequiredmixin-dont-stop-my-dispatch-flow-when-user-is-not-authenticat) |
| Stack Overflow | delete success message with obj value | [here](https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown) |
| Stack Overflow | how to add custom error pages | [here](https://stackoverflow.com/questions/17662928/django-creating-a-custom-500-404-error-page) |
| Stack Overflow | how to use css in django forms | [here](https://stackoverflow.com/questions/5827590/css-styling-in-django-forms) |
| Stack Overflow | bootstrap card resize | [here](https://stackoverflow.com/questions/65616251/how-to-re-size-my-cards-divs-using-bootstrap) |
| Stack Overflow | relationship with slug and getabsoluteurl | [here](https://stackoverflow.com/questions/35581956/relationship-between-slug-and-get-absolute-url-what-am-i-doing-wrong) |
| GitHub | fix crispy forms label issue | [here](https://github.com/django-crispy-forms/django-crispy-forms/issues/248) |
| Sophyia.me | secret key generate from terminal | [here](https://sophyia.me/the-easist-way-to-create-your-secret-key) |
| Stack Exchange | username length best practice | [here](https://security.stackexchange.com/questions/18516/usernames-should-their-length-be-limited ) |
| Radu | bootstrap footer bottom | [here](https://radu.link/make-footer-stay-bottom-page-bootstrap/) |
| Learn Django | slugify post title | [here](https://learndjango.com/tutorials/django-slug-tutorial) |
| Geeks For Geeks | Django fields | [here](https://www.geeksforgeeks.org/django-model-data-types-and-fields-list/) |
| Adamj | how to use limit integerfield | [here](https://adamj.eu/tech/2021/05/08/django-check-constraints-limit-range-integerfield/ ) |
| W3 Schools | github checkbox markdown | [here](https://www.w3schools.io/file/markdown-checkbox-github/) |
| Geeks For Geeks | how to use typed choice field | [here](https://www.geeksforgeeks.org/typedchoicefield-django-forms/) |
| Geeks For Geeks | form filed custom widgets | [here](https://www.geeksforgeeks.org/django-form-field-custom-widgets/) |
| Codeing Gear | add favicon to django | [here](https://codinggear.blog/django-add-favicon/) |
| Grepper | add class to form field | [here](https://www.grepper.com/answers/564807/Add+class+to+form+field+Django+ModelForm) |
| Medium | crispy forms | [here](https://levelup.gitconnected.com/how-to-make-your-django-forms-look-crispy-78a68000bc3f) |


### Documentation

| Source | Title | URL |
| --- | --- | --- |
| Django | working with forms | [here](https://docs.djangoproject.com/en/3.2/topics/forms/) |
| Django | django's built-in form classes | [here](https://docs.djangoproject.com/en/3.2/ref/forms/api/) |
| Django | working with model forms | [here](https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/) |
| Django | writing views | [here](https://docs.djangoproject.com/en/3.2/topics/http/views/) |
| Django | wandling HTTP requests | [here](https://docs.djangoproject.com/en/3.2/topics/http/) |
| Django | URL dispatcher | [here](https://docs.djangoproject.com/en/3.2/topics/http/urls/) |
| Django | django's messages framework | [here](https://docs.djangoproject.com/en/3.2/ref/contrib/messages/) |
| Django | working with Django templates | [here](https://docs.djangoproject.com/en/3.2/topics/templates/) |
| Django | 	Using the Django ORM | [here](https://docs.djangoproject.com/en/3.2/topics/db/queries/) |
| Django | django's QuerySet API reference | [here](https://docs.djangoproject.com/en/3.2/ref/models/querysets/) |
| Django | template tags and filters | [here](https://docs.djangoproject.com/en/3.2/topics/templates/#tags-and-filters) |
| Django | integer Field | [here](https://docs.djangoproject.com/en/dev/ref/models/fields/#integerfield ) |
| Django | for | [here](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#for) |
| Django | Django User model | [here](https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#django.contrib.auth.models.User) |
| Django | redirects | [here](https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/#redirect) |
| Django | messages | [here](https://docs.djangoproject.com/en/3.2/ref/contrib/messages/) |
| Django | ForeignKey field | [here](https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.ForeignKey) |
| Django | Url dispatcher | [here](https://docs.djangoproject.com/en/3.2/topics/http/urls/ ) |
| Django | form validation | [here](https://docs.djangoproject.com/en/3.2/ref/forms/validation/ ) |
| Django | form fields | [here](https://docs.djangoproject.com/en/4.2/ref/forms/fields/ ) |
| Django | form templates | [here](https://docs.djangoproject.com/en/4.1/topics/forms/#working-with-form-templates) |
| Django PhoneNumberField | django phonenumberfield docs | [here](https://django-phonenumber-field.readthedocs.io/en/latest/reference.html#validator) |
| Mozilla | setTimeout | [here](https://developer.mozilla.org/en-US/docs/Web/API/setTimeout) |
| Bootstrap | methods | [here](https://getbootstrap.com/docs/5.0/components/alerts/#methods) |
| Bootstrap | usage |  [here](https://getbootstrap.com/docs/5.0/components/alerts/#usage ) |
| Bootstrap | carousel examples | [here](https://getbootstrap.com/docs/4.1/examples/carousel/)|
| Bootstrap | login page examples | [here](https://mdbootstrap.com/docs/standard/extended/login/) |
| Bootstrap | blog page examples | [here](https://getbootstrap.com/docs/4.1/examples/blog/) |


### Tutorials

| Source | Title | URL |
| --- | --- | --- |
| YouTube - Web Zone | responsonive grid with bootstrap | [here](https://www.youtube.com/watch?v=ei5-5vcEPz8&t=136s) |
| YouTube - Codemy| add posts | [here](https://www.youtube.com/watch?v=CnaB4Nb0-R8) |
| YouTube - Codemy| comment section | [here](https://www.youtube.com/watch?v=hZrlh4qU4eQ) |
| YouTube - Codemy| delete blog post | [here](https://www.youtube.com/watch?v=8NPOwmtupiI) |
| YouTube - Codemy| update blog post | [here](https://www.youtube.com/watch?v=J7xaESAddDQ) |
| YouTube - Coding Entrepreneurs | Ajax likes | [here](https://www.youtube.com/watch?v=pkPRtQf6oQ8) |
| YouTube - Coding Is Thinking |  delete comments | [here](https://www.youtube.com/watch?v=kuJPMKbN3Yg) |
| YouTube - Django World |  edit and delete button for blog detail page | [here](https://www.youtube.com/watch?v=wFci3tnRNFw) |


### Articles

These article samples were taken from third party resources to prepopulate the website with blogs that present organic content.

- [Jalopnik](https://jalopnik.com/every-car-looks-like-this-thanks-to-a-gigantic-regulato-1849837803): Every Car Looks Like This Thanks to a Gigantic Regulatory Loophole
- [Car Zone](https://www.carzone.ie/motoring-advice/should-you-buy-a-used-electric-car/2933): Should You Buy A Used Electric Car?


### Library Information

- [Car Info](https://www.car.info/en-se/brand): This website presents a database of all car manufacturers in the world. It provided help in preparing the car maker choices tuple that is present in the consultation application submission form.

- [The Python Package Index (PyPI)](https://pypi.org/): PyPI was critical in accessing libraries that added functionality to the project that otherwise would be impossible to feature in the end product.

- [Code Insitute](https://codeinstitute.net/ie/): The theory available in the Code Institute curriculum has been central in successfully setting up and utilizing Google Cloud API services for this project.


### Theory

- [UCD Professional Academy](https://www.ucd.ie/professionalacademy/): I would like to thank UCD PA for their facilitator and masterclass sessions in partnership with Code Insitute. These have been invaluable in better understanding relevant theory and practice elements.

---

## Acknowledgements

I would like to first and foremost thank my mentor, Rohit Sharma, for his dedication to helping me find direction in developing my projects and understand the fundamental considerations in growing as a software developer. Moreover, the tutor support available at Code Institute has been an excellent help in finding solutions to various issues I came across in the development process that I needed help. Lastly, the Slack community at Code Institute has been nothing less than inspirational. I commend their dedication to a constructive culture that strives to help future developers in their struggles towards their software development journey. 

--- 

## Closing Remarks


---
 [Back to Top](#table-of-contents)