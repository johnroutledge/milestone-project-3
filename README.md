# Hashmoney
**Backend Data Centric Milestone Project**

![Main Mockup](https://johnroutledge.github.io/milestone-project-3/assets/images/main_mockup.png "Main Mockup")
 
[Link to Live Website](https://hash-money.herokuapp.com)

[GitHub Repo](https://github.com/johnroutledge/milestone-project-3)

**Rationale**

With the ever increasing popularity and interest in cryptocurrency, there are still a vast amount of people who are sceptical or unsure as to whether they should invest in it or not.
Such people need an app that is easy to understand, simple to use and gives them clear visual feedback as to how their investment is progressing.  All of these should take place in a risk-free environment.

This website meets such needs by providing them with the ability to trade and track some of the most popular crypotcurrencies without any financial investment. Having registered, users given 100,000 credits which they can spend on a selection of cryptocurrencies as they please.  

All of the prices are up-to-the-minute accurate and taken from coinmarketcap.com via an api. Users can track the progress of their portfolio and can buy, sell and exchange cryptocurrencies as often as they wish.  There is also the option to reset their account and start from scratch.

The typical user for the website would be someone:
* Is completely new to crypto and just wants to follow the prices
* Is unsure about trading crypto and wants to try it for fun
* Is risk-averse and wants to see how much they could make without any financial investment
* Knows about cryptocurrencies but can't afford to invest their own money just yet
* Wants an imaginary crypto portfolio to show their friend/partner/client the risks/benefits of investing

People visiting this website are looking for:
* Increased knowledge of trading cryptocurrencies
* A quick, easy way to invest in crytocurrencies risk-free
* The different profits which could be made in the short and long-term
* An introduction to cryptocurrencies

Hashmoney is the ideal site for such people because:
* It includes all of the above in one place
* It has intuitive controls and layout
* It is both clear and concise in its layout

***

## Index – Table of Contents

* [User Experience (UX)](#user-experience) 
* [Features](#features)
* [Technologies Employed](#technologies-employed)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

***

## UX

**Strategy**

User needs:  simple to navigate, quick to register, straightforward to trade, intuitive design, unintimidating and modern appearance.

Being a big mobile gamer myself who only has a few minutes to spend playing a game, I decided that the game should fulfil the following needs: be visually pleasing, provide quick feedback and gratification, and be extremely easy to pick up.


**Scope**

User Stories:
1. As someone who is new to cryptocurrency trading, I want an app which gives me clear and concise information.
2. As someone who is new to cryptocurrency trading, I want an app which is intuitive to use.
3. As a person who is risk-averse, I want an app that allows me to trade cryptocurrencies without any financial investment.
4. As a person who wants to invest in cryptocurrencies, but still has reservations, I want an app that shows me the realistic gains and losses that can be made.


**Structure**

As it is a very straightforward and intuitive game, the website is consequently a very simple one-page, no-scroll design.


**Skeleton**

![Wireframes](https://johnroutledge.github.io/milestone-project-2/assets/images/ms2_gameplay_wireframes.png "Wireframes")

To make sure the game intuitive to navigate and play, I kept the controls in a central position. This is very important for 
mobile users as it allows for one-handed gameplay and also for desktop users as it keeps mouse-movement to a single movement, whatever the screen size and resolution.
Through a minimum of visual content, I also reduced distraction and maximized engagement.

**Surface**

The 'Moserrat' Google font was chosen to give a clean and modern feel, while the grey and white colour scheme added to this style.

The colour scheme was chosen as it feels sharp and modern to match the world of cryptocurrencies. At the same time, it is both visually unintimidating and easy on the eye. I wanted the app to have this look so that it appeals to users who are risk-averse and who don't want to be overloaded with unecessary information.

The cryptocoin hero image was chosen for the landing page to make it immediately apparent that this is a financial app dealing with cryptocurrency. The large two sentence message underneath the hero image was used to give a clear, unambiguous description of what the app is about.

The cryptocoin images used in the title bars of all other pages were used to maintain consistency and also reaffirm that it is an app dealing with cryptocurrency.  

***


## Features

**Implemented**
* CHANGE 
* CHANGE 
* CHANGE 
* CHANGE 
* CHANGE 
* CHANGE 
* CHANGE 

**Future Features to Implement**
* The ability to choose from a wider range of cryptocurrencies
* Unlimited access to cryptocurrency rates (currently it is limited as the free API option was chosen)
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

## Database Schema

## Database Model

![ERD](https://johnroutledge.github.io/milestone-project-3/static/images/readme/hashmoney.png "ERD")

## CRUD

***

## Testing

|  Test Label                                   | Action         | Expected Outcome                                          | Test Outcome  |
|-----------------------------------------------|----------------|-----------------------------------------------------------|---------------|
|  Initial page load                            | Page load      |  Instruction modal should appear on top                    | PASS          |
|  Instruction modal close button               | Click          |  Instruction modal should close when clicked              | PASS          |
|  Marquee text                                 | Page load      |  Should scroll consistently at all times                  | PASS          |
|  Help button                                  | Pre-play       |  Should be enabled and highlighted on focus               | PASS          |
|  Play button                                  | Pre-play       |  Should be enabled and highlighted on focus               | PASS          |
|  Help button                                  | Click          |  Instruction modal should appear on top                    | PASS          |
|  Play button                                  | Click          |  Countdown should trigger followed by game start          | PASS          |
|  Eight circle buttons                         | Pre-play       |  Should be disabled pre-play                              | PASS          |
|  Help button                                  | In-play        |  Should be disabled in-play                               | PASS          |
|  Play button                                  | In-play        |  Should be disabled in-play                               | PASS          |
|  Eight circle buttons                         | In-play        |  Should be enabled and highlighted on focus               | PASS          |
|  Countdown timer                              | In-play        |  Should perform a three-second countdown then 'Ready?'    | PASS          |
|  Gameplay timer                               | In-play        |  Should run for 30 seconds unless incorrect button click  | PASS          |
|  Action word                                  | In-play        |  Should change to new action if correct button clicked    | PASS          |
|  Action word color                            | In-play        |  Should change colour if correct button clicked           | PASS          |
|  Game score update                            | In-play        |  Should increment by one if correct button clicked        | PASS          |
|  Correct click sound                          | In-play        |  Should be audible if correct button clicked              | PASS          |
|  Incorrect click sound                        | In-play        |  Should be audible if incorrect button clicked            | PASS          |
|  Highlight correct circle                     | In-play        |  Correct circle should blink if incorrect button clicked  | PASS          |
|  Game over sound                              | In-play        |  Should be audible if time runs out                       | PASS          |
|  High score update                            | Game end       |  Should update if new high score achieved                 | PASS          |
|  Countdown timer                              | Game end       |  Should reset to zero                                     | PASS          |
|  Action word                                  | Game end       |  Should display 'Game over' or 'New High'                 | PASS          |
|  Game score                                   | Game end       |  Should reset to zero                                     | PASS          |
|  Media Query mobile screen size               | Resize screen  |  Page should display correctly on mobile screen           | PASS          |
|  Media Query tablet screen size               | Resize screen  |  Page should display correctly on tablet screen           | PASS          |
|  Media Query desktop screen size              | Resize screen  |  Page should display correctly on 14 inch screen          | PASS          |
|  Media Query 5k screen size                   | Resize screen  |  Page should display correctly on 5k screen               | PASS          |
|  Marquee text                                 | Resize screen  |  Should fit partial width of screens above mobile size    | PASS          |
|  Marquee text                                 | Resize screen  |  Should fit entire width of mobile screen                 | PASS          |
|  Copyright text                               | Resize screen  |  Should be visible on screens above mobile size           | PASS          |
|  Copyright text                               | Resize screen  |  Should not be visible mobile screens                     | PASS          |

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

![Responsiveness](https://johnroutledge.github.io/milestone-project-2/assets/images/gameplay_screenshots.png "Responsiveness")

The website was tested on various screen sizes using Chrome DevTools, from iPhone5 up to 5k screen. The image above shows the website on iPhone 5, iPad and laptop screens. On a 5k screen resolution (see image below), the gameplay area remained the same size as on a laptop (and didn't scale up) to retain ease of gameplay when using a mouse.

![5k](https://johnroutledge.github.io/milestone-project-2/assets/images/5k_responsiveness.png "5k")

**Testing Browser Compatibility**

The website was successfully opened and rendered correctly in Chrome (both desktop and mobile versions), Edge and Safari.

**Code Validation**

pep8online.com

![Marquee](https://johnroutledge.github.io/milestone-project-2/assets/images/marquee_error.png "Marquee")

Both the HTML and CSS were validated using the W3C Markup Validation Service. This was done using the 'Validate by Direct Input' option. For the HTML, this resulted in an error with the marquee element (see screenshot above). This was rectified by recreating the effect using CSS (code credit listed in credits at the end of this readme file).  Final checks were done resulting in no errors as per screenshot below.

![HTML](https://johnroutledge.github.io/milestone-project-2/assets/images/html_check.png "HTML")

All checks on the CSS file were clear on the first attempt as per screenshot below.

![CSS](https://johnroutledge.github.io/milestone-project-2/assets/images/css_check.png "CSS")

**Testing with Lighthouse in Google Chrome Devtools**

![Lighthouse](https://johnroutledge.github.io/milestone-project-2/assets/images/lighthouse_testing.png "Lighthouse")

* Performance: this was initially 91% which was acceptable (see top Lighthouse results in image above). However, to improve load speed further, the 
background image was saved at a reduced resolution as it doesn't detract from the gameplay UX. Also, references to JavaScript files in the index.html file were moved from the head element down to the end of the body element. Having 
done both of these, performance was tested again and increased to 95% on mobile (see middle Lighthouse results in image above) and 99% on desktop (see lower Lighthouse results in image above).
* Accessibility: was 98% after first test (see top Lighthouse results in image above). This was due to the contrast between the font color and 
background on the instruction modal. Having changed the font color used on the instruction modal from a neon pink to a neon green, it went up to 100% on both mobile and desktop versions (see middle and bottom Lighthouse results in image above).
* Best Practices: was 100% after first test, so no changes needed.
* SEO: was 100% after first test, so no changed needed.

**Notable bug fixes**

1. When the first play() function is called, there is a noticeable delay before the audio file is played. 
All subsequent audio files play without delay. Having tried various fixes (using MP3 files instead of WAV) without success, I decided to just play an empty sound before the start of the game. This fixed the problem as now the sounds are immediate when clicking circles during gameplay.
2. Having played the game numerous times to make sure it played correctly, I noticed that when landing on circle number 0 (in the 12 o'clock position) from an anti-clockwise direction, if the next action word was 'boing' then the game flagged up wrong when clicking on the correct circle (number six). Having done a console.log to see which circle it was expecting, it turned out to be circle seven rather than circle six.  After looking at the code to see what the error could be, I discovered that I had miscalculated when experiencing a negative number in my if...else if statement in the 'calculateCorrectCircle' function.
3. The three-second countdown timer on game start was very buggy initially.  Having researched this and discussing it with my mentor, this issue was found to be synchronicity
within the JavaScript.  The countdown timer was originally within its own function, but calling this prior to starting the main game timer resulted in both timers running concurrently which caused multiple DOM updates at the same time.  To rectify this, I took the countdown timer out of its own function and put it into a loop in the 'playGame' function which eradicated any synchronicity issues and fixed the bug.
4. After clicking the play button, it was discovered that it could be clicked again before becoming disabled and so causing further instances of the 'resetGame' function being called. This resulted in it being possible to start multiple games at the same time. Having inspected the code, it was discovered that both the play and help buttons were being disabled within the countdown timer loop. To fix the bug, the code which disables both the play and help buttons was simply moved to the top of the 'resetGame' function.
5. When running the game with the DevTools console open, the error 'Uncaught (in promise) DOMException: The play() request was interrupted by a new load request' was flagged up (see image below). Originally, the audio files for the game sounds were played through an audio element in the index.html file using code in the index.js file. To fix this bug, I removed the audio element from the index.html file coded all game sounds to play purely via the index.js file.

![Audio Bug](https://johnroutledge.github.io/milestone-project-2/assets/images/audio_bug.png "Audio Bug")

***

## Deployment 

**Deploying to [Heroku](https://dashboard.heroku.com/)**

* First, create an account at [Heroku](https://www.heroku.com)
* After logging in, click on 'create new app'.
* Select the closest region to your location and give the app a name.
* Select 'GitHub' as the deployment method.
 ![Heroku connected to  github](static/images/deployment/heroku-github.png)
* Navigate to [GitHub](https://www.github.com) and login.
* Select the repository you want to deploy from.
* Next, go to settings and click 'Reveal Config Vars' and set the environment variables so they match the values in your env.py file (leave out the inverted commas)
* Before deploying, ensure your Procfile is correctly set up and that you have updated your requirements.txt file
 - Enable automatic deploys 
      ![Heroku github automatic deploys](static/images/deployment/heroku-automatic-deploys.png)
* Once deployed, your app is now runnable

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
- ADD

**Acknowledgements**

- To my wife, Chonchanok Routledge, and several work colleagues for testing the app on various devices.
- ADD
- To Brian Machiara, my Code Institute mentor, for giving me invaluable tips and insight throughout the whole process.
