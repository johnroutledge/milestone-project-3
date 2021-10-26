# Hashmoney
**Backend Data Centric Milestone Project**

![Main Mockup](https://johnroutledge.github.io/milestone-project-3/readme-assets/hashmoney_mockup.png "Main Mockup")
 
[Link to Live Website](https://hash-money.herokuapp.com)

[GitHub Repo](https://github.com/johnroutledge/milestone-project-3)

**Rationale**

With the ever increasing popularity of and interest in cryptocurrency, there are still a vast amount of people who are skeptical or unsure as to whether they should invest in it or not.
Such people need an app that is easy to understand, simple to use and gives them clear visual feedback as to how their investment is progressing.  All of these should take place in a risk-free environment.

Hashmoney meets such needs by providing them with the ability to trade and track some of the most popular cryptocurrencies without any financial investment. Having registered, users are given 100,000 USD 'credits' which they can spend on a selection of cryptocurrencies as they please.  

All of the prices are up-to-the-minute accurate and taken from coinmarketcap.com via an api. Users can track the progress of their portfolio and can buy, sell and exchange cryptocurrencies as often as they wish.  There is also the option to reset their account and start from scratch.

The typical user for the website would be someone who:
* Is completely new to crypto and just wants to follow the prices
* Is unsure about trading crypto and wants to try it for fun
* Is risk-averse and wants to see how much they could make without any financial investment
* Knows about cryptocurrencies but can't afford to invest their own money just yet
* Wants an imaginary crypto portfolio to show their friend/partner/client the risks/benefits of investing

People visiting this website are looking for:
* Increased knowledge of trading cryptocurrencies
* A quick, easy way to invest in cryptocurrencies risk-free
* The potential profits/losses which could be made in the short and long-term
* An introduction to cryptocurrencies

Hashmoney is the ideal site for such people because:
* It includes all of the above in one place
* It has intuitive controls and layout
* It is both clear and concise in its layout
* The information it provides is kept to a minimum to avoid cognitive overload

***

## Index – Table of Contents

* [User Experience (UX)](#user-experience) 
* [Features](#features)
* [Technologies Employed](#technologies-employed)
* [Database](#database)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

***

## UX

**Strategy**

User needs:  simple to navigate, quick to register, straightforward to trade, intuitive design, unintimidating and modern appearance.

Being a cryptocurrency trader myself, I remember the uncertainty and skepticism I had before I began. With that in mind, I decided to write an app that would enable people to dip into cryptocurrency trading risk-free. Along with that, I wanted it to be straightforward with clear feedback as to how their portfolio was growing (or not, as the case may be). I also wanted to give people the confidence to be able to make mistakes and to start from scratch again without financial penalties, hence the 'reset portfolio' option.


**Scope**

User Stories:
1. As someone who is new to cryptocurrency trading, I want an app which gives me clear and concise information.
2. As someone who is new to cryptocurrency trading, I want an app which is intuitive to use.
3. As a person who is risk-averse, I want an app that allows me to trade cryptocurrencies without any financial investment.
4. As a person who wants to invest in cryptocurrencies, but still has reservations, I want an app that shows me the realistic gains and losses that can be made.


**Structure**

To make sure the content/functionality is intuitive to navigate, I maintained consistency throughout the different pages by using the same layout/structure (landing page sections matched the order of menu items) and header and footer elements.

On the landing and gallery pages, I used content hinting so that users would be encouraged to scroll further down the page.

**Skeleton**

To make sure the app is intuitive to navigate and use, I decided to keep all of the buttons options fairly centrally placed and slightly to the right-hand side. This is very important for mobile users they are predominantly right-handed and allows for one-handed operation of the app. By minimizing the amount of visual content past the landing page, I also reduced distraction and maximized engagement.

Wireframes

* [Homepage wireframes](https://johnroutledge.github.io/milestone-project-3/readme-assets/wireframes_homepage.png)
* [Register page wireframes](https://johnroutledge.github.io/milestone-project-3/readme-assets/wireframes_register.png)
* [Login page wireframes](https://johnroutledge.github.io/milestone-project-3/readme-assets/wireframes_login.png)
* [Portfolio page wireframes](https://johnroutledge.github.io/milestone-project-3/readme-assets/wireframes_portfolio.png)
* [Prices page wireframes](https://johnroutledge.github.io/milestone-project-3/readme-assets/wireframes_prices.png)
* [Trade page wireframes](https://johnroutledge.github.io/milestone-project-3/readme-assets/wireframes_trade.png)
* [Transactions page wireframes](https://johnroutledge.github.io/milestone-project-3/readme-assets/wireframes_transactions.png)
* [Settings page wireframes](https://johnroutledge.github.io/milestone-project-3/readme-assets/wireframes_settings.png)
* [Edit Settings Wireframes](https://johnroutledge.github.io/milestone-project-3/readme-assets/wireframes_edit_settings.png)


**Surface**

The 'Monserrat' Google font was chosen to give a clean and modern feel, while the white/grey/blue color scheme added to this style.

The color scheme was chosen as it feels sharp and modern to match the world of cryptocurrencies. At the same time, it is both visually unintimidating and easy on the eye. I wanted the app to have this look so that it appeals to users who are risk-averse and who don't want to be overloaded with unnecessary information. A shade of blue was chosen for the buttons as it is perceived as being a trustworthy, dependable, and responsible color. Blue is also popular among financial institutions, as conveys trust and stability. The button color is consistent throughout the app to maintain consistency and increase the intuitiveness of the page.

The cryptocoin hero image was chosen for the landing page to make it immediately apparent that this is a financial app dealing with cryptocurrency. The large two sentence message underneath the hero image was used to give a clear, unambiguous description of what the app is about.

The cryptocoin images used in the title bars of all other pages were used to maintain consistency and also reaffirm that it is an app dealing with cryptocurrency.  

***


## Features

**Implemented**
* The navbar collapses to a burger menu on smaller screens to increase the available screen area
* The same footer appears on every page to maintain consistency and give quick access to relevant social media links 
* The home page incorporates content hinting by partially revealing an element just above the fold 
* Images on homepage include reveal text functionality behind questions encouraging people to explore further 
* People can register for free which also allocates them 100,000 dollars which they can trade with as they please 
* Users can reset their portfolio to zero at any point should they wish to start afresh. This also deletes their trading history
* Users can trade 17 of the top 20 cryptocurrencies
* A user's balance is clearly displayed on their portfolio screen and they can instantly see if they are in profit
* Users can also access their trading history on the transactions screen so they can see what they have bought and sold
* All cryptocurrency prices are accurate up to the second thanks to an api call to coinmarketcap.com
* Users can also access snippets of background information on each cryptocurrency through the use of reveal text functionality on the prices page

**Future Features to Implement**
* The ability to choose from a wider range of cryptocurrencies
* Unlimited access to cryptocurrency rates (currently it is limited to 333 api calls per day as the free API option was chosen)
* Give a choice of color schemes to add to the UX
* A portfolio balance leaderboard so traders can compete with each other registered users
* Add 'forgot password' functionality
* Price charts for prices and portfolio history to add to the UX
* Links to real-money cryptocurrency exchanges so the site can earn commission

***

## Technologies Employed

* Python
* HTML
* CSS
* JavaScript
* JQuery
* MongoDB
* Flask
* Jinja
* Heroku
* Github/Gitpod
* Materialize 1.0.0
* Google Fonts
* Google Dev Tools 
* Google Lighthouse
* Pep8online.com (to check Python code for PEP 8 requirements)
* W3C Validator (to check validity of HTML and CSS)
* Code Beautify (to beautify JavaScript)
* dbdiagram.io (to produce the MongoDB ERD)

***

## Database


Having gone over my ideas for the database schema with my mentor Brian Macharia, the data was allocated across the following tables within a MongoDB database:

* Users - stores a user's personal information and undergoes CREATE, READ and UPDATE operations.
* Transactions - stores a user's transaction history has a many-to-one relation with the users table on the email address field. It undergoes CREATE, READ and DELETE operations.
* Balances - stores a user's current balances for each currency has a one-to-one relation with the users table on the email address field. It undergoes CREATE, READ and UPDATE operations.  
* Currencies - stores additional information about all of the cryptocurrencies and undergoes READ operations.


**Schema**

![ERD](https://johnroutledge.github.io/milestone-project-3/readme-assets/hashmoney_erd.png "ERD")


***


## Testing

|  Test Label                                   | Action         | Expected Outcome                                          | Test Outcome  |
|-----------------------------------------------|----------------|-----------------------------------------------------------|---------------|
|  Hashmoney navbar logo                        | Click          |  Navigate to homepage from all pages                      | PASS          |
|  Navbar 'Home' 'Sign In' 'Register' links     | Before login   |  See only these links if user not logged in               | PASS          |
|  Navbar 'Portfolio' 'Prices' 'Trade' links   | After login    |  See only these links if user logged in                   | PASS          |
|  Navbar 'Transactions' 'Settings' 'Logout'    | After login    |  See only these links if user logged in                   | PASS          |
|  Navbar links                                 | Click          |  Navigate to the corresponding pages                      | PASS          |
|  Navbar links                                 | View on mobile |  Should be visible as hamburger icon                      | PASS          |
|  Homepage ellipsis on 'Why Hashmoney' card    | Click          |  Reveal hidden text                                       | PASS          |
|  Homepage ellipsis on 'How does it work' card | Click          |  Reveal hidden text                                       | PASS          |
|  Homepage register now link in reveal text    | Click          |  Navigate to register page                                | PASS          |
|  Homepage call to action register button      | Click          |  Navigate to register page                                | PASS          |
|  Homepage registered user login button        | Click          |  Navigate to sign-in page                                 | PASS          |
|  Social Media links in footer                 | Click          |  Navigate to the correct social media homepages           | PASS          |
|  Register page input wrong data format        | Submit         |  Catch all incorrect data formats                         | PASS          |
|  Register page existing email address in db  | Submit         |  Display email already registered flash message           | PASS          |
|  Register page passwords not matching         | Submit         |  Display passwords do not match flash message             | PASS          |
|  Register page successful register            | Submit         |  Display registration successful flash message                       | PASS          |
|  Register page successful register            | Submit         |  Navigate to user's portfolio page                        | PASS          |
|  Register page link to login page             | Click          |  Navigate to sign-in page                                 | PASS          |
|  Sign-in page input wrong data format         | Submit         |  Catch all incorrect data formats                         | PASS          |
|  Sign-in page input wrong login details       | Submit         |  Display incorrect email/password flash message           | PASS          |
|  Sign-in page successful login                | Submit         |  Display user welcome back flash message                  | PASS          |
|  Sign-in page successful login                | Submit         |  Navigate to user's portfolio page                        | PASS          |
|  Sign-in page link to register page           | Click          |  Navigate to register page                                | PASS          |
|  Portfolio page member information            | Page load      |  Display name, join date, balance, loss/gain %            | PASS          |
|  Portfolio page portfolio change %            | Page load      |  Render in green text if gain, red text if loss           | PASS          |
|  Portfolio page cryptocurrency data           | Page load      |  Display logo, name, USD balance, coin quantity & code    | PASS          |
|  Portfolio page trade buttons                 | Click          |  Navigate to trade page and auto select chosen crypto     | PASS          |
|  Prices page cryptocurrency data              | Page load      |  Display logo, name, code, coin price, loss/gain %        | PASS          |
|  Prices page cryptocurrency change %          | Page load      |  Render in green text if gain, red text if loss           | PASS          |
|  Prices page extra cryptocurrency information | Click          |  Reveal/Hide hidden text when clicking on cryptocurrency  | PASS          |
|  Trade page (via portfolio 'trade' button)    | Page Load      |  Display correct 'buy' currency                           | PASS          |
|  Trade page 'buy' currency select list         | Page Load      |  List all cryptocurrencies in database                    | PASS          |
|  Trade page 'purchase using' select list      | Page Load      |  List only cryptocurrencies user has positive balance of  | PASS          |
|  Trade page input wrong data format           | Click Submit   |  Catch all incorrect data formats                         | PASS          |
|  Trade page input zero amount                 | Click Submit   |  Display amount entered cannot be zero flash message      | PASS          |
|  Trade page input duplicate currencies        | Click Submit   |  Display traded currencies must be different flash message| PASS          |
|  Trade page not enough cryptocurrency         | Click Submit   |  Display not enough cryptocurrency flash message          | PASS          |
|  Trade page successful trade                  | Click Submit   |  Display trade successfully processed flash message       | PASS          |
|  Trade page successful trade                  | Click Submit   |  Navigate to portfolio page and display new balances      | PASS          |
|  Transactions page user transactions          | Page load      |  Show no transactions text if no transaction history      | PASS          |
|  Transactions page user transactions          | Page load      |  List all user's transactions since registered/reset      | PASS          |
|  Transactions page user transactions          | Page load      |  Show date/time, amount bought, crypto logo & code        | PASS          |
|  Transactions page user transactions          | Page load      |  Show bought with crypto logo & code, price per coin      | PASS          |
|  Settings page                                | Page load      |  Display user first name, last name and portfolio balance | PASS          |
|  Settings page 'edit' button                  | Click          |  Navigate to edit settings page                           | PASS          |
|  Edit Settings page input wrong data format   | Click Save     |  Catch all incorrect data formats                         | PASS          |
|  Edit Settings page reset balance switch      | Set to 'off'   |  Not reset user's portfolio when saving                   | PASS          |
|  Edit Settings page reset balance switch      | Set to 'on'    |  Reset user's portfolio when saving                       | PASS          |
|  Edit Settings page successful save           | Click Save     |  Display settings successfully updated flash message      | PASS          |
|  Edit Settings page successful save           | Click Save     |  Display account reset flash message if reset balance on  | PASS          |
|  Edit Settings page successful save           | Click Save     |  Navigate back to settings page and display new data      | PASS          |
|  Edit Settings page 'cancel' button           | Click          |  Navigate back to settings page and display existing data | PASS          |
|  Logout navbar link                           | Click          |  Display log out successful flash message                 | PASS          |
|  Logout navbar link                           | Click          |  Navigate to sign-in page                                 | PASS          |
|  Media Query mobile screen size               | Resize screen  |  Page should render correctly on mobile screen            | PASS          |
|  Media Query tablet screen size               | Resize screen  |  Page should render correctly on tablet screen            | PASS          |
|  Media Query desktop screen size              | Resize screen  |  Page should render correctly on 14 inch screen           | PASS          |
|  Media Query 5k screen size                   | Resize screen  |  Page should render correctly on 5k screen                | PASS          |


## CRUD Testing

|  Test Label                                   | CRUD Action    |  Expected Outcome                                         | Test Outcome  |
|-----------------------------------------------|----------------|-----------------------------------------------------------|---------------|
|  New user register                            | Create         |  Create new record in users table in db                   | PASS          |
|  New user register                            | Create         |  Create new record in balance table in db                 | PASS          |
|  Porftolio page                               | Read           |  Correctly list all balances from db                      | PASS          |
|  Prices page                                  | Read           |  Correctly list all prices from db and api call           | PASS          |
|  Prices page reveal text                      | Read           |  Correctly list all info from currencies table in db      | PASS          |
|  Trade page                                   | Read           |  List all cryptocurrencies from currencies table in db    | PASS          |
|  Trade page successful trade                  | Update         |  Correctly update transactions and balances tables in db  | PASS          |
|  Transactions page                            | Read           |  Correctly list all data from transactions table in db    | PASS          |
|  Edit settings page successful edit           | Update         |  Correctly update user table in db                        | PASS          |
|  Edit settings page successful reset balance  | Update         |  Correctly update balances table in db                    | PASS          |
|  Edit settings page successful reset balance  | Delete         |  Correctly delete all data from transactions table in db  | PASS          |

**Testing User Stories**

1. As someone who is new to cryptocurrency trading, I want an app which gives me clear and concise information.
* Yes, app presents all of the cryptocurrency names, logos and prices very clearly. There is also concise information about each one available to trade on the app.
2. As someone who is new to cryptocurrency trading, I want an app which is intuitive to use.
* Yes, it is very straightforward to trade on the app and users can also access all of their trades easily.
3. As a person who is risk-averse, I want an app that allows me to trade cryptocurrencies without any financial investment.
* Yes, it is clear from the home screen that the app is completely risk free. Once registered, users are allocated 100,000 USD credits which they use to buy and sell any of the listed cryptocurrencies they wish. They can also reset this balance and start from scratch at any point.
4. As a person who wants to invest in cryptocurrencies, but still has reservations, I want an app that shows me the realistic gains and losses that can be made.
* Yes, this is achieved by clearly showing a user's portfolio balance as well as an indication of how much it has grown or diminished since they started. 

**Testing Responsiveness**

The website was tested on various screen sizes using Chrome DevTools, from iPhone5 up to 5k screen. It was also tested using [Am I Responsive](http://ami.responsivedesign.is/) and the results were as per the following image:

![Responsiveness](https://johnroutledge.github.io/milestone-project-3/readme-assets/hashmoney_mockup.png "Responsiveness")


**Testing Browser Compatibility**

The website was successfully opened and rendered correctly in Chrome (both desktop and mobile versions), Edge and Safari.

**Code Validation**

Python code from the app.py file was checked using [Pep8online](https://www.pep8online.com)

The first check brought back numerous errors which were all rectified and resulted with a clear check as per the screenshot below.

![HTML](https://johnroutledge.github.io/milestone-project-3/readme-assets/pep8_validation.png "Python")


HTML and CSS were validated using the W3C Markup Validation Service. This was done using the 'Validate by Direct Input' option.

For the HTML, all pages except for the login page resulted in a warning caused by the flash messages section in the base.html template (see screenshot below). Having researched solutions on stackoverflow.com, I didn't change my code as the section already contained an h6 element as recommended by the warning (see below).

![HTML Section Warning](https://johnroutledge.github.io/milestone-project-3/readme-assets/html_section_warning.png "HTML")

![Flash Section Code](https://johnroutledge.github.io/milestone-project-3/readme-assets/flash_section_code.png "HTML")


The trade screen html threw up an interesting error relating to the select inputs:
![Trade screen error](https://johnroutledge.github.io/milestone-project-3/readme-assets/trade_html_error.png "HTML")

This was fixed by adding a size property to the inputs and giving it a value of 18 which allows for the number of currencies options in the app.


The login page was the only one without any errors or warnings as it doesn't reference the flash message section in base.html:

![Login Page Checks](https://johnroutledge.github.io/milestone-project-3/readme-assets/login_html_check.png "HTML")


All checks on the CSS file were clear on the first attempt as per screenshot below.

![CSS](https://johnroutledge.github.io/milestone-project-3/readme-assets/css_validation.png "CSS")


**Testing with Lighthouse in Google Chrome Devtools**

The results shown are for the homepage and portfolio pages on both mobile and desktop. These were chosen as they produced the lowest figures and best illustrate the gains made by implementing Lighthouse's recommended changes.

* Homepage (see images below): Running the test initially recommended changing the color of the copyright text to improve 'accessibility', add a meta description of the page to improve the 'SEO' and to resize of the 'Why Hash Money' image to improve the 'best practices' score. Having done all of these resulted in improvements across the board.

![Homepage Mobile Results](https://johnroutledge.github.io/milestone-project-3/readme-assets/lighthouse_home_mob.png "Homepage Mobile Results")

![Homepage Desktop Results](https://johnroutledge.github.io/milestone-project-3/readme-assets/lighthouse_home_desk.png "Homepage Desktop Results")


* Portfolio page (see images below): Running the test initially recommended changing the color of the copyright text to improve the 'accessibility' score (as it did for all pages) and to reduce the crypto logo file sizes to improve the 'performance' score. Results improved once these changes were implemented. However, there is still room for improvement with performance by using HTTP2 which is something I would look at doing in a future version.

![Portfolio Page Mobile Results](https://johnroutledge.github.io/milestone-project-3/readme-assets/lighthouse_portfolio_mob.png "Portfolio Page Mobile Results")

![Portfolio Page Mobile Results](https://johnroutledge.github.io/milestone-project-3/readme-assets/lighthouse_portfolio_desk.png "Portfolio Page Desktop Results")


**Notable bug fixes**

1. Portfolio Balance Bug 

In an early version of the app, the portfolio screen was showing a balance which multiplied the USD amount by twenty. This resulted in an incorrect balance. Having examined the code within the app.py file, I discovered that there was an error within the loop that iterates through a user's currency balances to produce the total balance (see screenshots below). By moving the totalBalance variable outside of the else statement (but still within the loop), the bug was fixed. In the screenshots, the left image is with the bug and the right image is after the fix had been applied. Line numbers are different from what they are in the final version as much more code has been added.

![Portfolio Bug Screen](https://johnroutledge.github.io/milestone-project-3/readme-assets/portfolio_page_screens.png "Portfolio Bug")

![Portfolio Bug Code](https://johnroutledge.github.io/milestone-project-3/readme-assets/portfolio_page_code.png "Portfolio Bug Code")


2. Heroku Deployment Bug

![Heroku Bug](https://johnroutledge.github.io/milestone-project-3/readme-assets/heroku_bug.png "Heroku Bug")

With the app not far from completion, I attempted to deploy it with Heroku. When trying to run the app, it produced the error is per the screenshot above. Having followed the onscreen instructions, I took a look at the application logs (shown below) and determined the error lay with importing requests. Having tried numerous suggestions from various webpages (which included freezing the requirements file) without success, I turned to tutor support for help. They also struggled, but suggested typing 'requests' directly into the requirements.txt file (see second image below). They also stated I did not have to include a version number. Having done this and then re-deploying on Heroku again, the app ran as expected.

![Heroku Bug](https://johnroutledge.github.io/milestone-project-3/readme-assets/heroku_log.png "Heroku Bug")

![Heroku Bug](https://johnroutledge.github.io/milestone-project-3/readme-assets/requirements_file.png "Heroku Bug")


3. Available Balance Bug

As a result of user testing, a bug was discovered in the flash message on the trade screen. It was displaying a zero available balance for DOGE when in reality, the balance was over 5000 USD. Having examined the code, the error was found in line 419 of app.py where additional number formatting was resulting in a balance being multiplied by zero. Removing the conversion to integer resulted in the correct format being applied. Running the fixed code confirmed the correct balance is now displayed in the flash message. See below images for all details:

![Avilable Balance Bug](https://johnroutledge.github.io/milestone-project-3/readme-assets/available_balance_bug.png "Heroku Bug")

***

## Deployment 


**Creation on GitHub**

1. Login to [GitHub](https://github.com/)
1. Create a new repository by clicking the green 'new' button and choose the Code Institute full template
1. Click on the green 'Gitpod' button to initiates a fresh workspace

Adding files to the Github repository is done as follows:

Type the following into the command line:

        git add .  
        git commit -m "this is what I have done"
        git push

Using the '.' will add all files to the repository staging area. Single files are added using file path names, i.e.: about.html or assets/images/hero.png.
Be clear and consistent with your commit comments - it's a good idea to use imperatives to explain your changes. 
Pushing moves your work from the staging area to your repository.


**Deploying to [Heroku](https://dashboard.heroku.com/)**

1. Go to your Gitpod CLI and create a requirements file by typing 'pip3 freeze --local > requirements.txt' in the root directory.
1. Next, create the Procfile by typing 'echo web: python app.py > Procfile' into the CLI root directory.
1. Open this file and type the line 'web: python3 app.py'. Make sure you delete any blank lines at the bottom, then save the file.
1. Add, commit and push your newly created files to your Github repository.
1. Then, go to [Heroku](https://www.heroku.com) and create an account. 
1. After logging in, click on 'create new app'.
1. Select the closest region to your location and give the app a name.
1. Select 'GitHub' as the deployment method.
1. Within the GitHub profile, enter the name of the GitHub repository you want to deploy from and click 'search'.
1. Once Heroku has found the repository, click to connect the app.
1. Go to the 'settings' tab for the app and click 'Reveal Config Vars'.
1. Set the environment variables by entering key-value pairs (leaving out any inverted commas) so that they match those in your env.py file (see section below for further details).
1. Go back to the 'deploy' tab and make sure 'enable automatic deploys' from the 'main' branch are selected. 
1. Click 'deploy'.
1. Once deployed, your app is now runnable by clicking 'view'.


**Forking this project**

This creates a copy of the original repository in your GitHub account so you can make changes without impacting the original.

1. Log in to GitHub and navigate to this [repository](https://github.com/johnroutledge/milestone-project-3)
1. Click the 'fork' button located at the top of the repository.
1. A copy of the repository will be created in your own GitHub account.

**How to clone this project locally**

1. Login to Github and navigate to this [repository](https://github.com/johnroutledge/milestone-project-3)
1. Under the repository name, click the 'code' button.
1. Next, choose HTTPS and copy the URL.
1. Open Gitbash and change the current working directory to the location for the cloned directory.
1. Type 'git clone ' and then paste the URL from step 3 above.
1. Press 'enter' to create your clone.
1. You can now access this new directory and run the project locally.

**Values for the env.py file**

The finished env.py file should look as follows:

        import os

        os.environ.setdefault("IP", "0.0.0.0")
        os.environ.setdefault("PORT", "5000")
        os.environ.setdefault("SECRET_KEY", "paste secret key here")
        os.environ.setdefault("MONGO_URI", "paste connection string here")
        os.environ.setdefault("MONGO_DBNAME", "enter db name here")
        os.environ.setdefault("COIN_MARKET_CAP_KEY", "paste API key here")

* Set the IP key value to '0.0.0.0'
* Set the PORT key value to '5000'
* Navigate to [Randomkeygen.com](https://https://randomkeygen.com/) and copy one of the Fort Knox Passwords.
* Paste it into the key value for SECRET_KEY.

MONGO DB KEYS

* Login to your [MongoDB Atlas](https://account.mongodb.com/account/login) account.
* Once in, select your database cluster on the dashboard then click 'connect'.
* Then select 'connect your application' and copy the connection string from the 'connection string only' tab as per the screenshot below:

![Mongo URI](https://johnroutledge.github.io/milestone-project-3/readme-assets/mongodb_uri.png "Mongo URI")

* Paste the string into the value for the MONGO_URI key.
* Make sure to replace PASSWORD with your database password and replace 'myFirstDatabase' with the name of the database (in this case, 'hashmoney')
* Set the MONGO_DBNAME key value to the name of the database ('hashmoney' in this case).
* Save the file.

COIN_MARKET_CAP_KEY

* Navigate to [Coinmarketcap](https://coinmarketcap.com) and create a free account.
* Once logged in, go to the dashboard and copy the api key by hovering over it and clicking the blue 'copy key' button as shown in the image below:

![Coinmarketcap API Key](https://johnroutledge.github.io/milestone-project-3/readme-assets/coinmarketcap_dashboard.png "Coinmarketcap API Key")

* Paste the key into the value for the COIN_MARKET_CAP_KEY in the env.py file.
* Save the file.

***

## Credits

**Content**

- Coinmarketcap.com for all crypto prices (accessed via API)
- Cryptocurrency coin descriptions taken from wikipedia.com and investopedia.com

**Media**

- The homepage hero cryptocoins image was taken from pngwing.com and then edited
- The two reveal text card images were re-formatted from photos by Art Rachen and Michael Förtsch on Unsplash.com
- The cryptocoin images used in the title cards on portfolio, prices, trade, transactions and settings pages were taken from pngegg.com and citypng.com and have also been edited
- Cryptocurrency icons taken from cryptologos.cc and iconarchive.com
- All other icons used in the app are from FontAwesome.com

**Code**

- Basic template setup, use of Flask, linking to MongoDB and Heroku taken from the Code Institute's Backend Development Task-Manager Mini-Project
- Code for Materialize elements taken and modified from materialize.com
- Pretty Printed's YouTube channel video 'Adding a Favicon to a Flask App'
- How to float an image to right of div taken from stackoverflow.com

**Acknowledgements**

- To my wife, Chonchanok Routledge, my sister, Julie Jobburn and several work colleagues for testing the app on various devices.
- To Jo at Tutor Assistance, for helping me fix the Heroku Deployment bug.
- To Brian Macharia, my Code Institute mentor, for giving me invaluable tips and insight throughout the whole process.
