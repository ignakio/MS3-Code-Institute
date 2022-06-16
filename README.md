<div align="center">
    <img src="/static/images/readme/mockup.png" target="_blank" rel="noopener" alt="FeedMe" aria-label="FeedMe"/>
</div>


[FeedMe](https://ms3-feedme.herokuapp.com/) was designed, built, and deployed, by myself, Ignacio Cladera Crespo as the third project for the Code Institute Full Stack Web Development diploma. The purpose of FeedMe is to be a recipe website that allows members to view FeedMe recipes, as well as add and share recipes of the users own liking.

## Table of Contents
1. [UX](#ux)
    - [Goals](#goals)
        - [Visitor Goals](#visitor-goals)
        - [Site Owner Goals](#site-owner-goals)
    - [User Stories](#user-stories)
    - [Design Choices](#design-choices)
    - [Wireframes](#wireframes)

2. [Features](#features)
    - [Existing Features](#existing-features)
        - [Elements on every page](#elements-on-every-page)
        - [Home](#home)
	    - [Login](#login)
	    - [Register](#register)
        - [FeedMe Recipes](#feedme-recipes)
        - [My Recipes](#my-recipes)
        - [Add Recipes](#add-recipes)
        - [Edit Recipe](#edit-recipe)
        - [FAQ](#faq)
        - [404 error](#404-error)
   	    - [Log out](#log-out)
    - [Features for Future Releases](#features-for-future-releases)

3. [Information Arcitecture](#information-architecture)
	- [Database choice](#database-choice)

4. [Technologies Used](#technologies-used)
    - [Tools](#tools)
    - [Databases](#databases)
    - [Libraries](#libraries)
    - [Languages](#languages)

5. [Testing](#testing)
    - See seperate [TESTING.md](TESTING.md) file.

6. [Deployment](#deployment)
    - [How to run this project locally](#how-to-run-this-project-locally)
    - [Heroku Deployment](#heroku-deployment)
 
7. [Credits](#credits)
    - [Content](#content)
    - [Images](#images)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

----

# UX

## Goals

### Visitor Goals

The target audience for FeedMe are:
- People who enjoy cooking. 
- People who are interested in joining an online recipe website.
- People who want to share good recipes they make. 
- People looking for recipe recommendations. 
- People looking for a website to store their recipes. 

User goals are:
- To join an online recipe website. 
- Find new recipes via the FeedMe website. 
- Share recipes that I have enjoyed with other FeedMe members. 
- To be able to add, edit, and delete my recipes on the website. 
- Be able to navigate the website easily and view the recipe in detail. 

### FeedMe's Goals

The goals of FeedMe are:
- Provide a platform where users can find recipe recommendations via the FeedMe website and its members. 
- For FeedMe members to be able to add, edit, and delete recipes that they would like to share. 
- Provide a platform for FeedMe members to share recipes they would like to add. 
- For FeedMe members to be able to view recipes in detail.  

## User Stories

As a visitor to the FeedMe website I expect/want/need:

1. To be able to easily find the information I am looking for, the layout needs to make sense so that I am not put off. 

2. The site to be laid out in a way that is easy to navigate, so that I can find what I need. 

3. The site to be responsive and navigable for various device sizes; desktop, tablet, and phone. For the content to look good 
   on all of the devices.

4. To be able to connect to FeedMe's social media accounts. 

5. To be able to click on recipes for further information about them. 

6. To be able to add, edit, and delete recipes that I would like to share with others. 

7. To be able to search for recipes on the website using keywords.

8. To be able to log in and out with ease. 

9. To be notified that I have logged in or out of my account. 

10. To be notified about changes that are made, inlcluding adding, editing, and deleting recipes. 

11. To be able to find out more about FeedMe and how the website works. 

## Design Choices

### Fonts
- The primary font 'Open Sans' was chosen to be the main text of this site as it is easy to read, looks professional, and goes well with the secondary font. "Open Sans Condensed' is used for headings and sub headings. 

- The secondary font 'Playfair Display' was chosen for the websites logo font, hoome banner and recipe headings as it looks fun, and is easy to read. 

### Colors
- The colour scheme for this site was rendered on [Cooler](https://coolors.co/) and can be seen below:

<div align="center">
    <img src="/static/images/color-palette.png" alt="Colors used in the FeedMe website" aria-label="Colors used in the FeedMe website"/>
</div>

- Cadet Grey: #91A3B0
- Columbia Blue: #BCD4DE
- Pale Pink: #EFD3D7
- Isabelline: #FCF7F2

- The grey was used in the navbar and footer when you hover over the nav links. 

- The blue was used as the background color for both the navbar and footer.

- The pale pink was used as the background color for succesful flash messages and for the banner on the home page. 

- The cream color was used as the background color for the website. 

## Wireframes

These wireframes were created using [Balsamiq](https://balsamiq.com/) during the design and planning process for this project. 

- [Desktop - Home page](/static/images/wireframes/desktop-home-page.png)
- [Desktop - FeedMe recipes](/static/images/wireframes/desktop-feedme-recipes.png)
- [Desktop - Your recipes](/static/images/wireframes/desktop-your-recipes.png)
- [Desktop - Recipe page](/static/images/wireframes/desktop-recipe-page.png)
- [Desktop - Add a recipe](/static/images/wireframes/desktop-add-recipe.png)
- [Tablet - Home page](/static/images/wireframes/tablet-home-page.png)
- [Tablet - FeedMe recipes](/static/images/wireframes/tablet-feedme-recipes.png)
- [Tablet - Your recipes](/static/images/wireframes/tablet-your-recipes.png)
- [Tablet - Recipe page](/static/images/wireframes/tablet-recipe-page.png)
- [Tablet - Add a recipe](/static/images/wireframes/tablet-add-recipe.png)
- [Mobile - Home page](/static/images/wireframes/mobile-home-page.png)
- [Mobile - FeedMe recipes](/static/images/wireframes/mobile-feedme-recipes.png)
- [Mobile - Your recipes](/static/images/wireframes/mobile-your-recipes.png)
- [Mobile - Recipe page](/static/images/wireframes/mobile-recipe-page.png)
- [Mobile - Add a recipe](/static/images/wireframes/mobile-add-recipe.png)

# Features
 
## Existing Features

### Elements on every page

#### Navbar

![Navbar](/static/images/readme/navbar.png)

- The navbar features on every page.

- **In desktop view**  The navigation bar features the website name ‘FeedMe' on the far left, and website pages on the far right.
  
- A user who is logged in will see the options of Home, FeedMe Recipes, My Recipes, Add recipe, and Log out. 

- A user or visitor who is not logged in will see the options of Home, FeedMe Recipes, Log in, and Register. 

- **In tablet and mobile view**  the name remains in the left side of the navigation bar, where users would expect it to be. The burger 
  icon to display the full navigation menu is on the far right. 

#### Footer

![Footer](/static/images/readme/footer.png)

- The footer features on every page.

- The footer has four sections - social media icons, contact us, recipes, and my account. 

- The social icons are links to FeedMe's social media accounts for Facebook, Instagram, Pinterest, and Twitter. They are located under the FeedMe heading. 

- Contact us, includes an email address and telephone number for FeedMe.  

- Recipes, include all the different recipe categories. 

- My account, when logged in, shows 'My Recipes' and 'Logout'. If not logged in, it shows 'Log in' and 'Register'. 

### Home

**Top Recipes**

![Top Recipes](/static/images/readme/top-recipes.png)

- The first section of the home page displays top recipes of the week. 
- There are four recipes, and if you click on them, they take you to the full recipe. 

**Home Banner**

![Home Banner](/static/images/readme/home-banner.png)

- This section includes a banner, which has been split in two.
- The first half includes the phrase 'Feeling hungry? Checkout some of our recipes below', with the 'See All Recipes' button directly below. This button will take you to the FeedMe Recipes page. 
- The second half is a panorama image of pizza and pasta. 

**Search by Category**

![Search by category](/static/images/readme/search-by-category.png)

- This is the last section of the home page, with the sub-heading of 'Search by Category' and each of the categories below. 
- The categories are displayed via a circular image, with it's category name below. 

### Log in

![Log in](/static/images/readme/login.png)

- The login page features a standard login form asking for username and password.
- Validation for this form is handled in the back end and a flash message displays 'Nice to see you again (username)'. 
- Once logged in they are taken directly to their 'My Recipes' page. 

### Register

![Register](/static/images/readme/register.png)

- A user who is not logged in can create a new account using the register page. The page on this form includes a username 
 (which must be unique), and a password. 
- If a user who already has an account tries to register, a flash message displays 'Username already exists'. 

### FeedMe Recipes

![FeedMe Recipes](/static/images/feedme.png)

- This page displays all the recipes that have been added to FeedMe by the various users.
- At the top of the page, there is a search bar that users can use to search for recipes. 
- The recipe is displayed by its image with the recipe and the user who added it below.  
- If you hover over the image it displays 'See Recipe' with the recipe image faded. 
- If the image is clicked on, you can see thee recipe in full.  

### My Recipes

![My Recipes](/static/images/readme/your-recipes.png)

- This page displays all the users recipes that they have added. 
- The recipe is displayed by its image with the recipe name, and edit and delete buttons below.  
- If you hover over the image it displays 'See Recipe' with the recipe image faded. 
- If the image is clicked on, you can see the recipe in full.  

**Recipe page**

![Recipe page](/static/images/readme/recipe-page.png)

- This is the page displayed when users view a recipe in full.  
- It includes the recipe name on top, with the image, who the reecipe was uploaded by, the course type, total time of the recipe, and number of servings per recipe. 
- Below this are the list of ingredients needed for the recipe, with the recipe. directions below the ingredients. 
- At the bottom of the recipe card is a 'See All Recipes' button which takes the user to the FeedMe Recipes page. 

### Add Recipes

![Add Recipes](/static/images/readme/add-recipe.png)

- This page contains a form for members to add a recipe to their profile for other members to see. 
- It includes a section for the recipe name, recipe type, image url, time, servings, ingredients, directions, and notes. 
- Once the recipe has been added, a flash message displays 'Recipe successfully added'. 

### Edit recipe

- This page is accessed within the edit button of the recipe in My Recipes. It contains a form for members to edit a recipe that they have 
  previously added.  
- It is identical to the Add Recipe page. 
- Once the recipe has been edited, a flash message displays 'Recipe successfully updated'.
- Members only have access to edit their own recipes, and are unable to edit other members recipes. 

### Frequently asked questions

![FAQ](/static/images/readme/faq.png)

- This page can be accessed via the FAQ banner on the home page, as well as the Questions section in the footer. 
- The FAQ is presented as an accordian. 
- It answers some of the questions users may have. 

### 404 error

![404 error](/static/images/readme/404.png)

- This page is displayed when users try an access a page that does not exist. 
- They have the option of returning to the home page by pressing the button displayed. 

### Log out

![Log out](/static/images/readme/logout.png)

- Any user who clicks on 'Log out' from the navigation bar is automatically logged out and their session data cleared. They are informed
  that they have been logged out with a flash message displaying 'You have been logged out'. 

## Features for Future Releases

1. **Being able to comment on recipes**
    - Having a star rating available on the recipe page for users to vote for. 
    - The star rating is displayed on the FeedMe Recipes page and full recipe page, under the recipe name, giving the user an idea of how other members felt about the recipe. 

2.  **Being able to comment on recipes**
    - Having an option for users to write a comments on recipes added by FeedMe and its members.
    - The comments would appear below the full recipe.  

# Information Arcitecture

### Database Choice
- According to project instructions, the document-based database MongoDB is used. 

- The database 'FeedMeDB' has three collections 'categories', 'recipes' and 'users'.

## Setting up a database
In order to set up a database in MongoDB:

1. Signup or login to MongoDB
2. Create a cluster as well as a database.
3. Create three collections within your database following the data structure below.

![Database structure](/static/images/readme/database-structure.png)


- **users** contains information about the user, including a unique id, their username, and a hashed password. 

- **categories** contains the various recipe categories on he FeedMe website, including a unique id, and category name. 

- **recipes** contains information about the recipes added to the FeedMe website. 
- This includes the recipe category, recipe name, a url for the recipe image, the total time it takes to make the recipe, number of servings per recipe, which user added the recipe, recipe ingredients, recipe direections, and additional recipe. notes. 

# Technologies Used

### Tools

- [GitHub](https://github.com/) to store and share all project code remotely. 
- [Gitpod](https://www.gitpod.io/) - IDE (Integrated Development Environment) used to write the code.
- [Balsamiq](https://balsamiq.com/) to create the wireframes for this project.
- [Heroku](https://id.heroku.com/) - Container-based cloud platform for deployment and running of apps.
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) - Templating engine used.
- [Favicon](https://favicon.io/) used to created the favicon used on the site.
- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) - Used to inspect page elements, test different CSS styles and debug site issues using the console.

### Databases
- [MongoDB](https://www.postgresql.org/) a NoSQL database program, using JSON-like documents. 

### Libraries
- [JQuery](https://jquery.com) to simplify DOM manipulation.
- [Bootstrap](https://www.bootstrapcdn.com/) to simplify the structure of the website and make the website responsive easily.
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) to provide icons for The House of Mouse webshop.
- [Google Fonts](https://fonts.google.com/) to style the website fonts.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) used to provide libraries and tools for the site such as Werkzeug.

### Languages
- This project uses HTML, CSS, JavaScript and Python programming languages.

# Testing 
 
- See seperate [TESTING.md](TESTING.md) file. 

# Deployment

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools: 
    - An IDE such as [Visual Studio Code](https://code.visualstudio.com/)

The following **must be installed** on your machine:
    - [PIP](https://pip.pypa.io/en/stable/installing/)
    - [Python 3](https://www.python.org/downloads/)
    - [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

### Instructions
1. Save a copy of the github repository located at https://github.com/PillowFishSticks/MP3-FeedMe by clicking the "download zip" button at 
   the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the 
   repository with the following command.
    ```
    git clone https://github.com/PillowFishSticks/MP3-FeedMe
    ```

2. Open your preferred IDE, open a terminal session in the unzip folder or cd to the correct location.

3. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. Enter the command:
    ```
    python -m .venv venv
    ```  
_NOTE: The `python` part of this command and the ones in other steps below assumes you are working with a windows operating system. 
Your Python command may differ, such as `python3` or `py`_

4. Activate the .venv with the command:
    ```
    .venv\Scripts\activate 
    ```
_Again this **command may differ depending on your operating system**, please check the [Python Documentation on virtual environments](
    https://docs.python.org/3/library/venv.html) for further instructions._

5. If needed, Upgrade pip locally with
    ```
    pip install --upgrade pip.
    ```

6. Install all required modules with the command 
    ```
    pip -r requirements.txt.
    ```

7. Set up the following environment variables within your IDE. 

    - If using VSCode, locate the `settings.json` file within the .vscode directory and add your environment variables as below. 
      Do not forget to restart your machine to activate your environment variables or your code will not be able to see them: 

    ```json
    "terminal.integrated.env.windows": {
        "HOSTNAME": "<enter hostname here>",
        "DEV": "1",
        "IP": "<your IP>",
        "MONGO_DBNAME": "<your database name on MongoDB>",
        "MONGO_URI": "<your URI to your MongoDB database>",
        "PORT": "<your port>",
        "SECRET_KEY": "<your secret key>" 
    }
    ```

    - If using an IDE that includes a `bashrc` file, open this file and enter all the environment variables listed above using the 
      following format: 
    ```
    HOSTNAME="<enter key here>"
    ```
    - `HOSTNAME` should be the local address for the site when running within your own IDE.
    - `DEV` environment variable is set only within the development environment, it does not exist in the deployed version, making it 
      possible to have different settings for the two environments. For example setting DEBUG to True only when working in development 
      and not on the deployed site.

8. If you have restarted your machine to activate your environment variables, do not forget to reactivate your virtual environment with 
   the command used at step 4.

9. You can now run the program locally with the following command: 
    ```
    python3 app.py
    ```

## Heroku Deployment

To deploy the FeedMe website to heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

4. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. 
   Give it a name and set the region to whichever is applicable for your location.

5. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

6. Confirm the linking of the heroku app to the correct GitHub repository.

7. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

8. Set the following config vars:

| Key | Value |
--- | ---
IP | `<your IP>`
MONGO_DBNAME | `<your database name on MongoDB>`
MONGO_URI | `<your URI to your MongoDB database>`
PORT | `<your port>`
SECRET_KEY | `<your secret key>`

9. In your heroku dashboard, click "Deploy". Scroll down to "Manual Deploy", select the master branch then click "Deploy Branch".

10. Once the build is complete, click the "View app" button provided.

12. Your heroku site should run as expected.

# Credits

## Content
- Recipe content was taken from [inspired taste](https://www.inspiredtaste.net/). 

## Images
- The hero image was taken from [Shutterstock](https://www.shutterstock.com/home). 
- The recipe images were taken from [inspired taste](https://www.inspiredtaste.net/). 
- The mockup image in the README.md file was created using [Techsini](https://techsini.com/).

## Code

- The following websites helped me understand and create my website, by viewing examples and explanatons.
    - [W3schools](https://www.w3schools.com/)
    - [Bootsnipp](https://bootsnipp.com/)
    - [Code Institute](https://codeinstitute.net/)
    - [Stack Overflow](https://stackoverflow.com/)

- The following website provided inspiration for my website.
    - [Tasty](https://tasty.co/)
    - [Pick Up Limes](https://www.pickuplimes.com/)

- The 404 template was taken from [colorlib](https://colorlib.com/). 


## Acknowledgements

 - Code Institute tutors for helping support and guide me in the right direction with my code.