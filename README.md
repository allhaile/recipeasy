# RecipEasy Final Project

For our final project we decided to create a web application titled, RecipEasy. The idea stemmed from the idea that both of us enjoyed cooking and aspired to become better. We realized there are hundreds of cooking applications already available but we felt that our social media platform is
something that made our idea unique. We decided to build a web app similar to Pinterest but
more interactive and would be solely dedicated to food. Our motivation was to create a
straightforward website that has simple user capabilities but still full of useful information for
each user. When we were searching for a food application most websites had either a limited
selection of recipes or the website was solely dedicated to one type of cuisine or diet style. With
RecipEasy we wanted to find a way to aggregate all of the information so when a user searches
for ‘Chicken’ or ‘Thai” the site would able to handle those types of requests.

<!-- Final project for Info290t

In order to use this application, you must install a plugin from the Google Chrome app.

To install, Google search the following term: "Allow-Control-Allow Origin."

The first search result should be the correct one, from the Google Chrome web store.

Click on the green button on the top-right hand corner of the app pop up to install.

Once completed, there should be a red square with the letters "CORS" in the top right hand corner of your Chrome tab next to the settings icon.

Click on the CORS icon.

Once you are ready to begin using the website, toggle the switch for "Enable cross-origin resource sharing." Copy and paste the following link in the user input "URL or URL pattern" section after your http://O.O.O.####/recipe_feed where the #### stands for the port number.

Refresh your page and you are ready to begin. -->




## Video Walkthrough

Here's a walkthrough of our development iterations:
### Onboarding
<img src="/gifs/onboarding.gif"  />

### Search Function
Once an user is signed in we created an interface that looks familiar to a Pinterest board where users can search for recipes, save recipes, and add their own recipes.The search capability makes a **GET call to the Food2Frok API** which aggregates recipes links, recipe images, ingredient list, and a rating of each recipe.
<img src="/gifs/search-func.gif"  />

### Profile View
After saving as many recipes from multiple searches the user can then decide to view their saved recipes on the profile page (pictured below). If a user decides to scrap a recipe they can simply click the trash can icon and the recipe image will be deleted from their profile.
<img src="/gifs/profile-view.gif"  />

<!-- > ![](/gifs/onboarding.gif) -->


#### Technologies Used
* Python (Flask)
* Sqlite (Database) & SQL
* JQuery
* JSON (API call)
* Bootstrap CSS
* HTML
