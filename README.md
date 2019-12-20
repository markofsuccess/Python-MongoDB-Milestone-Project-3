# Electronic Reviews

## Executive Summary of The Website

My third mile-stone project for my school [Code Institute](https://codeinstitute.net/) 

Data Centric Development Project

Welcome to Electronic Reviews - Simple review site for users to leave and read reviews of Smartphones (current) and Tablets & Laptops (coming soon). Press on any of the leave/read button to leave or read reviews. There are also amazon links for each item on the site. View the live site [here!](https://python-mobilephone-review.herokuapp.com/)

## The Goal of The Website

### The Goal

* The goal of the website is for users to be able to leave reviews and also read other users reviews of smartphones and soon also reviews of Tablets and Laptops.


# UX

* As a user, I want to be able to leave reviews on an item I used.
* As a user, I want to be able to read other users reviews on items.
* As a user, I want to see pictures of the item and links to purchase the item or find out more info about the item.

## Design

* The design is neat and user friendly with a theme from [startbootstrap]().


# Features

### Existing Features

* Sliding pictures of the different smartphones on the homepage. 
* Leave review button on each item on the homepage to leave reaview or read other users reviews.

### Features Left to Implement

* Want to create an membership feature, where people can register for free/log in with an personal account where they can see the reviews they left and also be able to edit them.
* Want to create an search bar, where users can search for different items and reviews.
* Want to create function where users can upload themselves their phone with pictures and content.
* Want to create Star Rating System for each user.
* Create one database colletcion for all products.


## Technologies Used

The technologies used in this project were:

* [HTML 5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)

* [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3)

* [Bootstrap](https://getbootstrap.com/)
  * Boostrap was used mainly to make the website responsive on multiple devices using bootstrap grid.

* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

* [AWS Cloud 9](https://aws.amazon.com/education/awseducate/)
  * Amazon Cloud 9 IDE was used to develop the project.

* [jQuery](https://jquery.com/)
  * The project uses JQuery to simplify DOM manipulation. 

* [Github](https://github.com/)
  * Github was used to document the project progress.

* [HTML & CSS Validator](https://validator.w3.org/)
  * This was used to validate the HTML and CSS code.

* [Python](https://www.python.org/)
  * Python was used to render the different html templates and to present data entrties.

* [MongoDB](https://www.mongodb.com/cloud/atlas)
  *MongoDB was used for creating databases for users leaving reviews.

* [Start Bootstrap](https://startbootstrap.com/templates/shop-homepage/)
  * The theme for the website.

* [Heroku](https://www.heroku.com/)
  * Heroku was used to deploy and host the project.

* [Flask](https://www.fullstackpython.com/flask.html)
  * The Flask framework was used.

* [Responsive Design Checker](https://responsivedesignchecker.com/)
  * Responsive Design Checker was used to check the responsivness of the site.

* [Google Dev Tools](https://developers.google.com/web/tools/chrome-devtools)
  * Google Dev Tools were used to check the responsiveness of the site.

# Testing

## Broswers

* The website was tested on the Google Chrome browser, Safari, Firefox Quantum and Brave broswer to make sure that everything loaded smoothly and looked proper across different browsers. Test were succesful on all browsers.
* Google Chrome Version 76.0.3809.132
* Brave Version 0.61.52 Chromium: 73.0.3683.86
* Safari Version 12.1.2 (14607.3.9)
* Firefox Quantum version 69.01
* Samsung Internet Browser on Samsung Galaxy S10, Version 10.1.00.27
* Chrome Broswer on Samsung Galaxy S10, version 77.0.3865.92

## Responsivness

* The site was tested on multiple devices using Google chrome developer tools to see the responsivness for different media devices. The devices that were tested were: Samsung S5, Pixel 2, Pixel 2 XL, iPhone X, iPhone 5/6/7/8, iPhone 6/7/8 Plus, iPad and iPad Pro.
* [Responsive Design Checker](https://responsivedesignchecker.com/) was used to test responsiveness on multiple devices. All test were succesful.

## Links & Review buttons

* All links and review buttons were tested to see if they redirected correctly.
* Carousel Picture Slider on home page was tested if were working.

## MongoDB

* Checked that all entries that users leave were showing in my MongoDB Atlas collection database.

## Bugs

* Only bug were with github when pushing the code to Github, I had set the global user name with quotes so first commits show "markofsuccess" instead of markofsuccess.

# Deployment

## Local using AWS & Github and MongoDB

1. Using AWS Cloud 9 to start the project. 
2. Creating a repository on Github
3. Using Ubuntu terminal in Cloud 9 and with command git init a local repository was created.
4. Installed required instalments with command: sudo pip3 install -r requirements.txt
5. Crate Procfile in Command terminal: echo web: python run.py > Procfile 
6. Create free [MongoDB account](https://www.mongodb.com/) - Create Cluster - and Collection.
7. Copy Your MongoDB atlas cluster.
7. Edit .bashrc file to hide MONGO URI secrtey key and values by:
    * In command terminal: cd .. (because .bashrc is in home directory)
    * In command terminal: nano .bashrc
    * In command terminal: export MONGO_URI="<”mongodb atlas mongodb+srv://<YOUR USER NAME>:<password>@<YOUR CLUSTER>-w59pp.mongodb.net/<YOUR COLLECTION>?retryWrites=true&w=majority”>"
    * Then use control x, y, enter to save settings.
    * Close terminal and reopen for change to take effect.
    * echo $MONGO_UR to see if your connection string is printed back.
8. Set up MONGO_URI app config in run.py.
9. In command terminal: git push origin master  - in order to push it to the Github resporitory.

## Heroku

1. Create a free account on [Heroku](https://www.heroku.com/)
2. In Dashboard - Click on New - Create New App
3. Name you App - Choose location closest to you.
5. In Ubuntu Terminal type in command line to find out your MONGO_URI: echo $MONGO_URI 
5. In Settings - Go to Reaval Config Vars - Add KEY = IP , VALUE = 0.0.0.0 , KEY = MONGO_URI , VALUE = <YOUR MONGO URI> , KEY = PORT , VALUE = 5000.
6. In Dashboard - Choose Deploy - I searched for my Github repository and connected with it.
7. In Deploy - Scroll Down to Manual deploy - Deploy a GitHub branch - Deploy Master Branch.
8. Scroll up to - Open APP to view the live site.

# Credits

## Acknowledgements

* Thanks to the amazing tutor on Code Institute for supporting me through the project.
* Thanks to my Mentor Anonija Simic for the support through the project.

## Media

### The pictures for the website was from [MediaMarkt](https://www.mediamarkt.se/)

## Content

### The Font was from [Font Awesome](https://fontawesome.com/)

### The theme for the website was from [Start Bootstrap](https://startbootstrap.com/templates/shop-homepage/)