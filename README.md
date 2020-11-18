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

***Note:** project in progress.*