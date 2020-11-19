<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

# My Veggie Food

## Code Institute: Milestone Project 3

My Veggie Food is a website where users can **create, read, update** and **delete (CRUD)** their own recipes,
adding their vegetarian touch. Lately, more and more people are deciding to
change their eating habits, either for health reasons, or out of respect for animals.

This website aims to be a platform for people who want to start this new lifestyle,
showing delicious, easy and nutritious recipes, and best of all, with contribution from
the community.

<a href="https://my-veggie-food-2020recipes.herokuapp.com/">Click here to view the project live</a>

## UX

### Main aims

- Provide a website where the users can **create, read, update** and **delete (CRUD)** their recipes. To achieve this, the site makes use of Mongo DB to store user data, to organize the recipes into different categories, and also to store each user's recipes.
- To make a website that is interactive, efficient and reacts well to user requests, to achieve this, the website makes use of the programming language called **Python** to create the bridge between the **database (Mongo DB)** and the webpage.
- To make a website that is easy to navigate through the different features it has, to achieve this, the website has a navigation bar with a clear menu, orderly and intuitive, also has a search bar and even has different sections on each page that differ from each other.
- To create a design that would be fully responsive on all devices and screen sizes.

### Ideal User

#### The ideal user for this website is:

- Who speaks English, due to the language used on the website.
- Be vegetarian, due to the topic of the website.
- Who likes to cook and learn new recipes.
- Who ideally has a good internet connection.

#### Occasional User

- Who speaks English, due to the language used on the website.
- Who is not a vegetarian, but would like to vary in his eating habits.
- Who is not a vegetarian, but likes to cook and learn new recipes.

#### This project is the best way to help them achieve these things because:

- This is a great platform to show the information required by the users, because it allows to interact with the available data, giving the possibility to create a user account, where they can create, read, update and delete their recipes in an easy and intuitive way.
- The website has many visual resources, whether images, bright colors or different text fonts, all with the aim of creating a great experience for users who use this platform.
- This platform is interested in knowing what its users think, therefore it has a contact page.

### User Stories

- As a user, I want a platform where I can review vegetarian recipes in an
easy way, and that it has a great variety of recipes.
- As a user, I want a platform that allows me to create an account, and allows
me to upload my own recipes in an easy way and also to edit or delete my
content contributed to the community.
- As a user, I want a website that looks good on all devices, whether from a
laptop, to a mobile phone, because this way I can review the recipes while
I'm cooking.
- As a user, I want a website where I can search and filter the recipes by
categories, allowing me to make a quick and efficient search.
- As a user, I want a website that displays information in an organized way
and that is easy to navigate.
- As a user, I want a website that has a contact page, where I can express my questions
or suggestions.

### Design Process

1. **Strategy Plane:** My goal in creating this project was to provide a platform for users to create, read, update and delete their recipes, in order to comply with CRUD, in an easy and intuitive way.

2. **Scope:** For the users, I wanted to offer a platform that will provide relevant information, in this case vegetarian recipes, since it is a new style of feeding and it is gaining more followers every day. For this, I created a welcome page with quick access to the desired information, through a section with recipes, another section giving reasons to be vegetarian and that invites you to join the website, among other features.

3. **Structure:** The website has a navigation bar with different links, it also has the logo of the website and a search bar in it, and a footer that has the copyright of the same website, these being the basic structures of the platform. The website has a home page, whose purpose is to welcome users, provide quick information, and invite them to register to create an account. In addition the platform has a recipes page divided into different categories, the recipes are displayed on cards with a brief description, and pressing the button that invites you to read more information, redirects you to a page that displays each recipe, providing relevant information such as ingredients, instructions, etc. The other pages are for registration, to login to the account created by a user, which upon login will appear 3 new links on the navigation bar, which are Profile, add recipes and logout. The user's profile welcomes him/her and shows the recipes he/she has, and if he/she is a new user and has no recipes published, the profile shows a special message inviting the user to create his/her first recipe. The other pages are the contact page, which allows users to contact the website directly, and a search results page.

4. **Skeleton:**
- Home Page wireframe.
    - <a href="https://github.com/cotebarrientos/3rd-milestone-project-my-veggie-food/blob/master/static/wireframes/001-desktop-home_page.png" target="_blank">Desktop</a>
    - <a href="https://github.com/cotebarrientos/3rd-milestone-project-my-veggie-food/blob/master/static/wireframes/012-mobile-home_page.png" target="_blank">Mobile</a>
- Recipes Page wireframe.
    - <a href="https://github.com/cotebarrientos/3rd-milestone-project-my-veggie-food/blob/master/static/wireframes/002-desktop-recipes.png" target="_blank">Desktop</a>
    - <a href="https://github.com/cotebarrientos/3rd-milestone-project-my-veggie-food/blob/master/static/wireframes/013-mobile_recipes.png" target="_blank">Mobile</a>
- Recipe Page wireframe.
    - <a href="https://github.com/cotebarrientos/3rd-milestone-project-my-veggie-food/blob/master/static/wireframes/003-desktop-recipes_opened.png" target="_blank">Desktop</a>
    - <a href="https://github.com/cotebarrientos/3rd-milestone-project-my-veggie-food/blob/master/static/wireframes/014-mobile-recipes_opened.png" target="_blank">Mobile</a>
- Register Page wireframe.
    - <a href="https://github.com/cotebarrientos/3rd-milestone-project-my-veggie-food/blob/master/static/wireframes/004-desktop-register.png" target="_blank">Desktop</a>
    - <a href="https://github.com/cotebarrientos/3rd-milestone-project-my-veggie-food/blob/master/static/wireframes/015-mobile-register.png" target="_blank">Mobile</a>
- Login Page wireframe.
    - <a href="https://github.com/cotebarrientos/3rd-milestone-project-my-veggie-food/blob/master/static/wireframes/005-desktop-login.png" target="_blank">Desktop</a>
    - <a href="https://github.com/cotebarrientos/3rd-milestone-project-my-veggie-food/blob/master/static/wireframes/016-mobile-login.png" target="_blank">Mobile</a>
- User Profile with no recipes Page wireframe.
    - <a href="https://github.com/cotebarrientos/3rd-milestone-project-my-veggie-food/blob/master/static/wireframes/006-desktop-profile_no_recipes.png" target="_blank">Desktop</a>
    - <a href="https://github.com/cotebarrientos/3rd-milestone-project-my-veggie-food/blob/master/static/wireframes/017-mobile-profile_no_recipes.png" target="_blank">Mobile</a>
- User Profile with recipes Page wireframe.
    - <a href="https://github.com/cotebarrientos/3rd-milestone-project-my-veggie-food/blob/master/static/wireframes/007-desktop-profile_with_recipes.png" target="_blank">Desktop</a>
    - <a href="https://github.com/cotebarrientos/3rd-milestone-project-my-veggie-food/blob/master/static/wireframes/018-mobile_profile-with_recipes.png" target="_blank">Mobile</a>
- User recipe Page wireframe.
    - <a href="https://github.com/cotebarrientos/3rd-milestone-project-my-veggie-food/blob/master/static/wireframes/008-desktop-profile_user_recipe.png" target="_blank">Desktop</a>
    - <a href="https://github.com/cotebarrientos/3rd-milestone-project-my-veggie-food/blob/master/static/wireframes/019-mobile-profile_user_recipe.png" target="_blank">Mobile</a>
- Add or Edit Form Pages wireframes.
    - <a href="https://github.com/cotebarrientos/3rd-milestone-project-my-veggie-food/blob/master/static/wireframes/009-desktop-profile_add_or_edit_recipe.png" target="_blank">Desktop</a>
    - <a href="https://github.com/cotebarrientos/3rd-milestone-project-my-veggie-food/blob/master/static/wireframes/020-mobile-profile_add_or_edit_recipe.png" target="_blank">Mobile</a>
- Contact Page wireframe.
    - <a href="https://github.com/cotebarrientos/3rd-milestone-project-my-veggie-food/blob/master/static/wireframes/010-desktop_contact.png" target="_blank">Desktop</a>
    - <a href="https://github.com/cotebarrientos/3rd-milestone-project-my-veggie-food/blob/master/static/wireframes/021-mobile-contact.png" target="_blank">Mobile</a>
- Search Page wireframe.
    - <a href="https://github.com/cotebarrientos/3rd-milestone-project-my-veggie-food/blob/master/static/wireframes/011-desktop-search.png" target="_blank">Desktop</a>
    - <a href="https://github.com/cotebarrientos/3rd-milestone-project-my-veggie-food/blob/master/static/wireframes/022-mobile-search.png" target="_blank">Mobile</a>

5. **Surface:** In this last phase of design, I planned the colors to be used on the website. To give it a more professional look and at the same time eye-catching for the users we used the tone **#343a40** for the navigation bar and the footer. For titles, subtitles and the navigation bar I used the text font called ***"Oswald"***, and for the paragraphs I used the text font called ***"Monserrat"***. For the ***H1*** tags I used the text color **#025830** , and for the titles and subtitles I set everything to uppercase. In addition to create a great user experience, I looked for the best way to display the images and order the information, for this I used cards that show each recipe, giving a professional and pleasant look to the user. Some pages have cover images such as the search results and contact, the purpose is to impress the user by inviting him to continue browsing the website.

## Features

### Existing Features

The project consist in 11 pages, which can be reached through the **Navigation bar** with a conventional placing of logo (top left). Each page has a **footer** with copyright information. the website is totally responsive.

#### Navbar

The navigation bar has a logo on the left side, in the center it has a search bar and on the right side it has the following links:

***When the user is not logged in***
- Home 
- Recipes
    - Main
    - Desserts
    - Snacks
    - Smoothies
    - All
- Register
- Login
- Contact

***When the user is logged in***
- Home
- Recipes
    - Main
    - Desserts
    - Snacks
    - Smoothies
    - All
- Profile
- Add Recipes
- Logout
- Contact

#### Home Page

It is responsible for welcoming future users. It is divided into 4 sections:

- **Carrousel Images:** It is located at the top of the page, and has 4 images that are changing from time to time.

- **Go Veggie Section:** In this section you will find a jumbotron image with a paragraph that invites you to be a vegetarian and at the same time offers you to create a user account on the website.

- **Featured Recipes:** This section has 6 recipes, which are shown in images, that when you pass the mouse pointer over the image, it will show you the recipe name. Each recipe image contains a link that will direct you to the desired recipe.

- **Get in Touch Section:** This section contains the social networks of the website.

#### Recipes Page

This page contains all the recipes from the website, which are displayed on cards that contain a related image of the recipe, the title of the recipe, a brief description and a button that invites you to learn more about the recipe. In addition, this page is divided into the following categories:

- **Main:** This category is responsible to contain all the recipes selected for this category, besides this includes both breakfast, lunch or dinner.

- **Desserts:** This category is responsible for containing all the recipes selected for this one. 

- **Snacks:** This category is responsible for containing all the recipes selected for this one. 

- **Smoothies:** This category is responsible for containing all the recipes selected for this one. 

- **All:** This category is responsible to display all the recipes that are on the website.

#### Recipe Page

This page is responsible of displaying each recipe, and it is composed by the following:

- Recipe Title
- Recipe Image
- A brief description of the recipe
- Servings
- Calories
- Preparation Time
- Cooking Time
- Ingredients
- Instructions
- Tips
- Created by (*the author name goes here*)

#### Register Page

This page allows users to create a user account. To do this the requirements are to put in an *email*, a *username* and a *password*.

#### Login Page

This page allows users to log in to their account, thus accessing their profile with personalized recipes. The requirements for logging in are to enter the *user name* and *password*.

#### Profile

This page contains the recipes of each user, and can be displayed in 2 modes which are as follows:

- ***When the user has no recipes published:*** this usually happens when a user has recently created their account. When this scenario occurs, the profile welcomes you and shows you a special message with an entertaining image that implies that you have no recipes, and at the bottom of the message there is a special button that invites you to create your first recipe.

- ***When the user has recipes:*** if this scenario is given, all the recipes that the user has created will appear, these will be shown in cards and in a very similar way as in the recipes page. This way the user will be able to access his/her recipes and have the possibility to edit or delete them if necessary.

#### User Recipe

This page is responsible of showing a specific recipe selected by the user from his/her created recipes. This is very similar to the Recipe page, containing the same components, only with the difference that at the bottom it contains 3 buttons which are the following:

- **Edit Button:** This button will take you to the page containing the recipe editing form.

- **Add Button:** This button will take you to the page containing the recipe adding form.

- **Delete Button:** By pressing this button, you will be shown a message in a modal window asking the user if he or she is sure to carry out that action, in addition to warning that once the recipe is deleted, it cannot be recovered. There are 2 buttons in the modal window, one to cancel the action and another to carry out the process of deleting the recipe.

#### Add Recipe Form

This page is responsible for uploading users' recipes. In order to perform this task, the user must complete the following:

- Add a recipe title
- Choose a category
- Write a brief description about the recipe
- Add a valid image url
- Add total servings
- Add the calories per portion
- Write the preparation time
- Write the cooking time
- Write the ingredients
- Write the instructions
- Write a tip about the recipe

Once the above is completed, the user must press the submit button, and the recipe will be created.

#### Edit Recipe Form

This page allows the user to edit any recipes they have created. It has the same features as the add recipe form, only the difference is that it loads the existing recipe data, allowing the user to edit it in an easy way.

#### Logout

This link is only activated in the navigation bar when the user logs in, and is intended to allow the user to log out.

#### Contact Page

This page contains a cover image, page title and a small message. It has a contact form which request user name, email and a box to leave a message. Once the user finishes writing his/her message, the contact form has a Send Button, which when pressed, will display a mini modal window with a thank you message.

#### Search Page

This page is activated when the user uses the search bar, and it can be displayed in 2 ways which are the following

- ***When there are search related results:*** It will show the recipes on cards and in a very similar way as in the recipes page.

- ***When there are no results:*** It will show a message implying that there are no results, and this message is accompanied by a very entertaining image.

### Features Left to Implement

Everything that was contemplated at the beginning of this project has been implemented, but there are some ideas that I would like to implement in the future, for example, adding the function of rating the recipes (from 1 to 5 stars) or adding a comment section for each recipe.

## Technologies Used

- HTML 5
    - The project uses **HTML5** to define the structure of this website.
- CSS 3
    - The project uses **CSS3** to add styling to the website.
- JavaScript
    - The project uses **Javascript** to implement Email JS and add interactivity to the website.
- <a href="https://www.python.org/" target="_blank">Python</a> 
    - The project uses **Python 3.9.0** to build the backend of this website.
- <a href="https://flask.palletsprojects.com/en/1.1.x/" target="_blank">Flask</a>
    - The project uses **Flask 1.1.2**.
- <a href="https://jinja.palletsprojects.com/en/2.10.x/" target="_blank">Jinja</a>
    - The project uses **Jinja2 2.11.2**.
- Werkzeug security
    - the project uses **Werkzeug 1.0.1**.
- <a href="https://github.com/psf/black" target="_blank">Black formatter</a>
    - The project uses **Black Formatter** to fix and format python files.
- <a href="https://flake8.pycqa.org/en/latest/" target="_blank">Flake 8</a>
    - The project uses **Flake 8** to check that the python files comply with the PEP 8 rule.
- <a href="https://getbootstrap.com/" target="_blank">Bootstrap</a>
    - The project uses **Bootstrap** version 4.5.3 , to build responsive website.
- <a href="https://jquery.com/" target="_blank">jQuery</a>
    - The project uses jQuery version 3.5.1 to implement interactivity to the website.
- <a href="https://www.emailjs.com/" target="_blank">Email JS</a>
    - The project uses **Email JS** to implement a functional contact page.
- <a href="https://www.mongodb.com/cloud/atlas" target="_blank">MongoDB Atlas</a>
    - The project uses **MongoDB Atlas** to store all the recipes, recipe categories and users of this website.
- <a href="https://www.heroku.com/" target="_blank">Heroku</a>
    - The project uses **Heroku** to deploy the website.
- <a href="https://git-scm.com/" target="_blank">Git</a>
    - The project uses **Git** to control the different versions and history of the code.
- <a href="https://github.com/" target="_blank">GitHub</a>
    - The project uses **GitHub** to host the source code.
- <a href="https://fontawesome.com/" target="_blank">FontAwesome</a>
    - The project uses free **FontAwesome** version 5.15.1 icons.
- <a href="https://www.adobe.com/ie/products/illustrator.html?gclid=EAIaIQobChMI7sax79jo6AIVRuztCh1rOgpzEAAYASAAEgJWMPD_BwE&sdid=88X75SKS&mv=search&ef_id=EAIaIQobChMI7sax79jo6AIVRuztCh1rOgpzEAAYASAAEgJWMPD_BwE:G:s&s_kwcid=AL!3085!3!340697722021!e!!g!!adobe%20illustrator" target="_blank">Adobe Illustrator</a>
    - The project uses Adobe **Illustrator CS6** portable version 16.0.0, to draw vectorial images used in the website.
- <a href="https://www.adobe.com/ie/" target="_blank">Adobe Photoshop</a>
    - The project uses **Adobe Photoshop CS6** portable version 13.0.0, to improve the images used in the website.
- <a href="https://pencil.evolus.vn/" target="_blank">Pencil</a>
    - The project uses **Pencil** version 3.1.0 to create the wireframes.
- <a href="https://code.visualstudio.com/" target="_blank">Visual Studio Code</a>
    - The project uses **Visual Studio Code** to write the code for this website.
- <a href="https://affinity.serif.com/en-gb/designer/" target="_blank">Affinity Designer</a>
    - The project uses **Affinity Designer** version 1.6.5.123, to make the website logo.

## Deployment

### Deploying using Heroku

1. In Heroku, create an app. The app must have a unique name.
2. Link that app to the GitHub repository by going to the "Deploy" tab in the main app menu.
3. In the Settings tab, add the corresponding Configuration Variables which are the same that are present in the local development:

>`IP = 0.0.0.0`
>
>`PORT = 5000`
>
>`MONGO_DBNAME = |database name|`
>
>`MONGO_URI = mongodb+srv://...`
>
>`SECRET_KEY = |secret key|`

It is very important, to make the project run in Heroku, to have created a **requirements.txt** document and a **Procfile** document. To do this you must use the following commands:

- To create a Procfile file
> `echo web: python app.py > Procfile`

- To create a requirements.txt file
> `pip3 freeze --local > requirements.txt`

### Deploying in Heroku using the Terminal

1. Create a new app. The app must have a unique name.
2. In the terminal, you have to login into Heroku typing `heroku login -i`, and then you have to write your username and password.
3. To initialize your git repository, you have to type in the terminal `git init`. After doing this, to link this GitHub repository with the app previously created in Heroku, you must type the following in the terminal `git remote add heroku https://my-veggie-food-2020recipes.herokuapp.com/`
4. Create a requirements.txt to run the app `pip3 freeze --local > requirements.txt`
5. To run the web app, you have to create a Procfile file `echo web: python app.py > Procfile`

#### To update the GitHub repository and the Heroku app.

- `git status`
- `git add`
- `git commit -m "Write your commit here!"`
- `git push heroku master`

### Cloning the project

To clone this project from GitHub:

1. Follow this link to the <a href="https://github.com/cotebarrientos/3rd-milestone-project-my-veggie-food" target="_blank">Project GitHub repository.</a>
2. Scroll to the top of this repository and click on the "clone or download button".
3. Decide whether you want to clone the project using HTTPS or an SSH key and do the following:
    - HTTPS: click on the checklist icon to the right of the URL.
    - SSH key: first click on 'Use SSH' then click on the same icon as above.
4. Open the 'Terminal'.
5. Choose the location for the cloned directory.
6. Type `git clone`, and then paste the clone URL.
> `git clone https://github.com/USERNAME/REPOSITORY`
7. Press 'Enter' to create your local clone.



***Note:** project in progress.*
