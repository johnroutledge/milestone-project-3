# Hashmoney
**Backend Data Centric Milestone Project**

![Main Mockup](https://johnroutledge.github.io/milestone-project-3/static/images/readme/mockup.png "Main Mockup")
 
[Link to Live Website](https://hash-money.herokuapp.com)

[GitHub Repo](https://github.com/johnroutledge/milestone-project-3)

**Rationale**

With the ever increasing popularity of and interest in cryptocurrency, there are still a vast amount of people who are sceptical or unsure as to whether they should invest in it or not.
Such people need an app that is easy to understand, simple to use and gives them clear visual feedback as to how their investment is progressing.  All of these should take place in a risk-free environment.

Hashmoney meets such needs by providing them with the ability to trade and track some of the most popular crypotcurrencies without any financial investment. Having registered, users are given 100,000 USD 'credits' which they can spend on a selection of cryptocurrencies as they please.  

All of the prices are up-to-the-minute accurate and taken from coinmarketcap.com via an api. Users can track the progress of their portfolio and can buy, sell and exchange cryptocurrencies as often as they wish.  There is also the option to reset their account and start from scratch.

The typical user for the website would be someone who:
* Is completely new to crypto and just wants to follow the prices
* Is unsure about trading crypto and wants to try it for fun
* Is risk-averse and wants to see how much they could make without any financial investment
* Knows about cryptocurrencies but can't afford to invest their own money just yet
* Wants an imaginary crypto portfolio to show their friend/partner/client the risks/benefits of investing

People visiting this website are looking for:
* Increased knowledge of trading cryptocurrencies
* A quick, easy way to invest in crytocurrencies risk-free
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

Being a cryptocurrency trader myself, I remember the uncertainty and scepticism I had before I began. With that in mind, I decided to write an app that would enable people to dip into cryptocurrency trading risk-free. Along with that, I wanted it to be straightforward with clear feedback as to how their portfolio was growing (or not, as the case may be). I also wanted to give people the confidence to be able to make mistakes and to start from scratch again without financial penalties, hence the 'reset portfolio' option.


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

* [Homepage wireframes](https://johnroutledge.github.io/milestone-project-3/static/images/readme/wf_homepage.png)
* [Register page wireframes](https://johnroutledge.github.io/milestone-project-3/static/images/readme/wf_register.png)
* [Login page wireframes](https://johnroutledge.github.io/milestone-project-3/static/images/readme/wf_login.png)
* [Portfolio page wireframes](https://johnroutledge.github.io/milestone-project-3/static/images/readme/wf_portfolio.png)
* [Prices page wireframes](https://johnroutledge.github.io/milestone-project-3/static/images/readme/wf_prices.png)
* [Trade page wireframes](https://johnroutledge.github.io/milestone-project-3/static/images/readme/wf_trade.png)
* [Transactions page wireframes](https://johnroutledge.github.io/milestone-project-3/static/images/readme/wf_transactions.png)
* [Settings page wireframes](https://johnroutledge.github.io/milestone-project-3/static/images/readme/wf_settings.png)
* [Edit Settings Wireframes](https://johnroutledge.github.io/milestone-project-3/static/images/readme/wf_edit_settings.png)


**Surface**

The 'Monserrat' Google font was chosen to give a clean and modern feel, while the white/grey/blue colour scheme added to this style.

The colour scheme was chosen as it feels sharp and modern to match the world of cryptocurrencies. At the same time, it is both visually unintimidating and easy on the eye. I wanted the app to have this look so that it appeals to users who are risk-averse and who don't want to be overloaded with unecessary information. A shade of blue was chosen for the buttons as it is perceived as being a trustworthy,dependable, and responsible color. Blue is also popular among financial institutions, as conveys trust and stability. The button color is consistent throughout the app to maintain consistency and increase intuitivity.

The cryptocoin hero image was chosen for the landing page to make it immediately apparent that this is a financial app dealing with cryptocurrency. The large two sentence message underneath the hero image was used to give a clear, unambiguous description of what the app is about.

The cryptocoin images used in the title bars of all other pages were used to maintain consistency and also reaffirm that it is an app dealing with cryptocurrency.  

***


## Features

**Implemented**
* The navbar collapses to a burger menu on smaller screens to increase the available screen area
* The same footer appears on every page to maintain consistency and give quick access to relevant social media links 
* The home page incorporates content hinting by partially revealing an element just above the fold 
* Images on homepage include reveal text functionality behind questions enouraging people to explore further 
* People can register for free which also allocates them 100,000 dollars which they can trade with as they please 
* Users can reset there portfolio to zero at any point should they wish to start afresh. This also deletes their trading history
* Users can trade 17 of the top 20 cryptocurrencies
* A user's balance is clearly displayed on their portfolio screen and they can instantly see if they are in profit
* Users can also access their trading history on the transactions screen so they can see what they have bought and sold
* All cryptocurrency prices are accurate up to the second thanks to an api call to coinmarketcap.com
* Users can also access snippets of background information on each cryptocurrency through the use of reveal text functionality on the prices page

**Future Features to Implement**
* The ability to choose from a wider range of cryptocurrencies
* Unlimited access to cryptocurrency rates (currently it is limited to 300 api calls per day as the free API option was chosen)
* Give a choice of color schemes to add to the UX
* A portfolio balance leaderboard so traders can compete with each other regiestered users
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

**Schema**

**Model**

![ERD](https://johnroutledge.github.io/milestone-project-3/static/images/readme/hashmoney.png "ERD")


***


## Testing

|  Test Label                                   | Action         | Expected Outcome                                          | Test Outcome  |
|-----------------------------------------------|----------------|-----------------------------------------------------------|---------------|
|  Hashmoney navbar logo                        | Click          |  Navigate to homepage from all pages                      | PASS          |
|  Navbar 'Home' 'Sign In' 'Register' links     | Before login   |  See only these links if user not logged in               | PASS          |
|  Navbar 'Porftfolio' 'Prices' 'Trade' links   | After login    |  See only these links if user logged in                   | PASS          |
|  Navbar 'Transactions' 'Settings' 'Logout'    | After login    |  See only these links if user logged in                   | PASS          |
|  Navbar links                                 | Click          |  Navigate to the corresponding pages                      | PASS          |
|  Navbar links                                 | View on mobile |  Should be visible as hamburger icon                      | PASS          |
|  Homepage vertical ellipsis on 'Why Hashmoney' card     | Click          |  Reveal hidden text                                       | PASS          |
|  Homepage vertical ellipsis on 'How does it work' card  | Click          |  Reveal hidden text                                       | PASS          |
|  Social Media links in footer                 | Click          |  Navigate to the correct social media homepages           | PASS          |
|  Sign-in page input wrong data format         | Submit         |  Catch all incorrect data formats                         | PASS          |
|  Sign-in page input wrong login details       | Submit         |  Display incorrect email/password flash message           | PASS          |
|  Sign-in page successful login                | Submit         |  Display user welcome flash message                       | PASS          |
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
|  Trade page 'buy'currency select list         | Page Load      |  List all cryptocurrencies in database                    | PASS          |
|  Trade page 'purchase using' select list      | Page Load      |  List only cryptocurrencies user has positive balance of  | PASS          |
|  Trade page input wrong data format           | Click Submit   |  Catch all incorrect data formats                         | PASS          |
|  Trade page input duplicate currencies        | Click Submit   |  Display traded currencies must be different flash message       | PASS          |
|  Trade page successful trade                  | Click Submit   |  Display trade successfully processed flash message       | PASS          |
|  Trade page successful trade                  | Click Submit   |  Navigate to portfolio page and display new balances      | PASS          |
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
* Yes, it is clear from the home screen that the app is completely risk free. Once registered, users are allocated 100,000 credits which they can trade as they choose. They can also reset this balance and start from scratch at any point.
4. As a person who wants to invest in cryptocurrencies, but still has reservations, I want an app that shows me the realistic gains and losses that can be made.
* Yes, this is achieved by clearly showing a user's portfolio balance as well as an indication of how much it has grown or diminished since they started. 

**Testing Responsiveness**

![Responsiveness](https://johnroutledge.github.io/milestone-project-3/assets/images/gameplay_screenshots.png "Responsiveness")

The website was tested on various screen sizes using Chrome DevTools, from iPhone5 up to 5k screen. The image above shows the website on iPhone 5, iPad and laptop screens. The app renders as per the screenshot below on a 5k screen resolution.

![5k](https://johnroutledge.github.io/milestone-project-3/assets/images/5k_responsiveness.png "5k")

**Testing Browser Compatibility**

The website was successfully opened and rendered correctly in Chrome (both desktop and mobile versions), Edge and Safari.

**Code Validation**

The Python code from the app.py file was checked using [Pep8online](https://www.pep8online.com)

The first check brought back numerous errors which were all rectified and resulted with a clear check as per the screenshot below.

![HTML](https://johnroutledge.github.io/milestone-project-3/static/images/readme/pep8_check.png "Python")

![IF ERROR](https://johnroutledge.github.io/milestone-project-3/static/images/readme/marquee_error.png "IF ERROR")

Both the HTML and CSS were validated using the W3C Markup Validation Service. This was done using the 'Validate by Direct Input' option. For the HTML, this resulted in an error with IF ERROR (see screenshot above). This was rectified by IF FIXED .  Final checks were done resulting in no errors as per screenshot below.

![HTML](https://johnroutledge.github.io/milestone-project-3/static/images/readme/html_check.png "HTML")

All checks on the CSS file were clear on the first attempt as per screenshot below.

![CSS](https://johnroutledge.github.io/milestone-project-3/static/images/readme/css_check.png "CSS")

**Testing with Lighthouse in Google Chrome Devtools**

![Lighthouse](https://johnroutledge.github.io/milestone-project-3/static/images/readme/lighthouse_testing.png "Lighthouse")

* Performance: ADD RESULTS
* Accessibility: ADD RESULTS
* Best Practices: ADD RESULTS
* SEO: ADD RESULTS.

**Notable bug fixes**

1. Portfolio Balance Bug 

In an early version of the app, the portfolio screen was showing a balance which multiplied the USD amount by twenty. This resulted in an incorrect balance. Having examined the code within the app.py file, I discovered that there was an error within the loop that iterates through a user's currency balances to produce the total balance (see screenshots below). By moving the totalBalance variable outside of the else statement (but still within the loop), the bug was fixed. In the screenshots, the left image is with the bug and the right image is after the fix had been applied. Line numbers are different from what they are in the final version as much more code has been added.

![Portfolio Bug Screen](https://johnroutledge.github.io/milestone-project-3/static/images/readme/portfolio_bug_screen.png "Portfolio Bug")

![Portfolio Bug Code](https://johnroutledge.github.io/milestone-project-3/static/images/readme/portfolio_bug_code.png "Portfolio Bug Fix Code")

2. ADD
3. ADD
4. ADD
5. Heroku Deployment Bug

![Heroku Bug](https://johnroutledge.github.io/milestone-project-3/static/images/readme/heroku_app_error.png "Heroku Bug")

With the app not far from completion, I attempted to deploy it with Heroku. When trying to run the app, it produced the error is per the screenshot above. Having followed the onscreen instructions, I took a look at the application logs (shown below) and determined the error lay with importing requests. Having tried numerous suggestions from various webpages (which included freezing the requirements file) without success, I turned to tutor support for help. They also struggled, but suggested typing 'requests' directly into the requirements.txt file (no version number required - see second image below). Having done this and then re-deplying on Heroku again, the app ran as expected.

![Heroku Bug](https://johnroutledge.github.io/milestone-project-3/static/images/readme/heroku_error_log.png "Heroku Bug")

![Heroku Bug](https://johnroutledge.github.io/milestone-project-3/static/images/readme/requirements.png "Heroku Bug")


***

## Deployment 

**Deploying to [Heroku](https://dashboard.heroku.com/)**

* Go to your Gitpod CLI and create a requirements file by typing 'pip3 freeze --local > requirements.txt' in the root directory.
* Next, create the Procfile by typing 'echo web: python app.py > Procfile' into the CLI root directory.
* Open this new file and type the line 'web: python3 app.py'. Make sure you delete any blank lines at the bottom, then save the file.
* Add, commit and push your newly created files to your Github repository.
* Then, go to [Heroku](https://www.heroku.com) and create an account. 
* After logging in, click on 'create new app'.
* Select the closest region to your location and give the app a name.
* Select 'GitHub' as the deployment method.
* Within the GitHub profile, enter the name of the GitHub repository you want to deploy from and click 'search'.
* Once Heroku has found the repository, click to connect the app.
* Next, you will need to login to your [MongoDB Atlas](https://account.mongodb.com/account/login) account.
* Once in, select your databse cluster on the dashboard then click 'connect'.
* Then select 'connection your application' and copy the connection string from the 'connection string only' tab.
* You then need to login to your [CoinMarketCap](https://coinmarketcap.com) account.
* From the dashboard, copy the API key.
* Next, navigate back to [Heroku](https://www.heroku.com), go to the 'settings' tab for the app and click 'Reveal Config Vars'.
* Now set the environment variables by entering key:value pairs (leaving out any inverted commas) so that they match those in your env.py file:

|  Key                  | Value        |
|-----------------------|--------------|
|  IP                   | 0.0.0.0      |
|  PORT                 | 5000         |
|  MONGO_DBNAME         | 0.0.0.0      |
|  MONGO_URI            | 0.0.0.0      |
|  SECRET_KEY           | 0.0.0.0      |
|  COIN_MARKET_CAP_KEY  | 0.0.0.0      | 
  
* Go back to the 'deploy' tab and make sure 'enable automatic deploys' from the 'main' branch are selected. 
* Click 'deploy'.
* Once deployed, your app is now runnable by clicking 'view'.

**How to run this project locally**

1. Login to Github and navigate to this [repository](https://github.com/johnroutledge/milestone-project-3)
1. Under the repository name, click the 'code' button.
1. Next,choose HTTPS and copy the URL.
1. Open Gitbash and change the current working directory to the location for the cloned directory.
1. Type 'git clone ' and then paste the URL from step 2 above.
1. Press 'enter' to create your clone.
1. You can now access this new directory.


**The project can be deployed by following these steps**

1. Log into GitHub
1. Click "Settings" in the menu above the Repository.
1. Scroll down through the settings to the "GitHub Pages" Section.
1. Underneath "Source", click the dropdown labelled "None" and then select "Master Branch".
1. The page should refresh automatically and then deploy the website.
1. If the page refuses to load, scroll down to "template" and select a template underneath "source". 
1. Scroll back down to the section entitled "GitHub Pages" and the link to the deployed website should be available.

**How to run this project locally**

To clone this project into Gitpod you will need:
* A Github account. [Create a Github account here](https://github.com/)
* Use the Chrome browser 

Then follow these steps:
1. Install the [Gitpod Browser Extensions for Chrome](https://www.gitpod.io/docs/browser-extension/)
1. After installation, restart your browser
1. Log into your [Gitpod](https://gitpod.com) account.
1. Navigate to the [Project GitHub repository](https://github.com/johnroutledge/milestone-project-1)
1. Click the green "Gitpod" button located on the right of the repository
1. This initiates a fresh gitpod workspace allowing you to work locally on the code.

**Adding and committing files**

Adding files to the Github repository is done as follows:

Type the following into the command line:

        git add .  
        git commit -m "this is what I have done"
        git push

Using the '.' will add all files to the repository staging area. Single files are added using file path names, i.e.: about.html or assets/images/hero.png.
Be clear and consistent with your commit comments - it's a good idea to use imperatives to explain your changes. 
Pushing moves your work from the staging area to your repository.

***

## Credits

**Content**

- Coinmarketcap.com for all crypto prices (accessed via API)
- Cryptocurrency coin descriptions taken from wikipedia.com and investopedia.com

**Media**

- The background arcade image was downloaded from INSERT
- Cryptocurrency icons taken from cryptologos.cc and iconarchive.com
- All other icons used in the app are from FontAwesome.com

**Code**

- Basic template setup, use of Flask, linking to MongoDB and Heroku taken from the Code Institute's Backend Development Task-Manager Mini-Project
- Code for Materialize elements taken and modified from materialize.com
- Pretty Printed's YouTube channel video 'Adding a Favivon to a Flask App'
- How to float an image to right of div taken from stackoverflow.com

**Acknowledgements**

- To my wife, Chonchanok Routledge, and several work colleagues for testing the app on various devices.
- To Jo at Tutor Assistance, for helping me fix the Heroku Deployment bug.
- To Brian Machiara, my Code Institute mentor, for giving me invaluable tips and insight throughout the whole process.
