# Rafael Ecommerce - Milestone Project 

This project is dedicated to users who are willing to buy and sell their goods through internet, and the transfer of money and data to execute these transactions.
It contains various categories like clothes, cosmetics, accessories etc.
 
## UX
 
This website consists of a user friendly layout. 

It's built for two kind of users:

1. One who wants to sell their products (Seller)
2. One who wants to buy product (Buyer)

Some Users will visit the site to buy the products whereas others visit to upload their products to sell and earn.

## Features

- Users can add their product detail like description,cost,features and images to sell.
- Users can view/shop all products in website uploaded seller.
- Users can add their selected items into cart to buy later
- Users can add/remove/update items in cart.
- Payment transactions via stripe to buy product.
- View/Edit their Order Summary
- Login/Signup/Change Password/Forgot Password

### Features Left to Implement
We can implement various features to improve the site like:

- Comment section
So that users can post a comment to clear their doubts realted to any product.

- Ratings
So that users can rate the products to help others whether this product is good or bad.

- Filter and Search Section
So that users can easily get/filter whatever they want out of thousand of products.

## Technologies Used

- [Python](https://www.python.org/doc/)
    - The project uses **Python** as backend.
    
- [Django](https://docs.djangoproject.com/en/3.1/)
    - The project uses **Django** framework to built a website.
  
 - [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
   
 - [Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
    - The project uses **Bootstrap** to build responsive and creative site.
    
- [Sqlite3](https://docs.python.org/3/library/sqlite3.html)
    - The project uses **Sqlite3** to store and retrieve the data.
    
- [Stripe](https://stripe.com/docs)
    - The project uses **Stripe** as payment gateway.
    

### Testing

1. Login Page:
    For users to login their account using email and password.
    One time login if user select **Remember Me**
    
2. Signup Page:
    For users to create their account using name, email and password.
    
3. Change Password / Forgot Password
    For users if they already registered but forgot their passsword.

4. Home Page: 
  - It contains **All Categories** section to visit the required categories.
  - **Trending** section to view all kinds of latest, trending and new products.

  If you **click on any product** it will take you to the product detail page showing all details(Features, Cost, Images, Reviews etc)  of that specific product. 

  If you click on any category present at header will take you to the page which will show you all products belong to that specific category .

5. CategoryDetail: To View
    - All Products belong to that category along with their price and ratings.
    
6. ProductDetail: To View
    - All Details of that product like images, description, features, cost, reviews etc.
    - Add to cart button to add it to the cart
    - Actual Price 
    - Price With Discount (if any)
    - User can add/subtract Quantity of product
    - Size and Color Options
    - Some Related Products visited by users who liked that product.
    
7. Add to Cart Page: To View
    - Login Required to go to cart page. If user is not logged in he/she will be redirected to login page.
    - All Products list along with their actual price, quantity,total price and saved amount.
    - Total calculated amount for all products. 
    - Remove button to remove item from cart
    - Continue Shopping button to view more items to shop by saving all items in cart
    - Checkout Button for payment to buy the product.
 
8. CheckoutAddress Page:
    - After clicking on checkout button user will go to  checkout form to fill their address details. 
    - It contains all order details along with their cost and grand total.
    - It contains **Save this information for next time** Button to store the address to reuse for future purchases.
    
9. Payment Page:
    - Payment page to add your card details for payment.
    - Order Summary Along with grand total
    - Submit Payment Button for final payment from linked card.
   
   
#### Deployment

This app is deployed on heroku
Heroku is a cloud platform as a service supporting several programming languages. 

**Here are pros/benefits of using Heroku:**

- Allows the developer to focus on code instead of infrastructure
- Enhance the productivity of cloud app development team
- Offers single billing for all projects broken down by team
- Monitor and enhance performance though rich application monitoring
- Helps your development, QA, and business stakeholders create a unified dashboard.
- Simple Horizontal & Vertical Scalability
- Heroku operation and security team is instantly ready to help you 24/7
- Leading Platform tools and Services Ecosystem
- Helps you to focus on innovation, not operations
- The Heroku Enterprise architecture offers minimal or no downtime during the system updates.
- Fast application lifecycle management and permissions
- Allows you to remove friction from the development
- Offers a powerful dashboard and CLI
- Integrates with familiar developer workflows
- Predictability and insight into the cost of application development and maintenance
- A bunch of supportive tools
- Beginner and startup-friendly
- It allows you to create a new server in just 10 seconds by using the interface of Heroku Command Line.
- The deployed version is available here: https://rafael-ecommerce.herokuapp.com/

## PLUS POINTS
- Using Heroku Config Vars: 
An app’s environment-specific configuration should be stored in environment variables (not in the app’s source code). This lets you modify each environment’s configuration in isolation, and prevents secure credentials from being stored in version control. So here i use heroku config vars.

- App is running in two different environments
On local machine (i.e. development).
Deployed to the Heroku platform (i.e., production)

for running the app’s test suite safely in isolation
Staging, for running a new build of the app in a production-like setting before promoting it


### RUN LOCALLY

1. clone the project using command :
      git clone https://github.com/Assugeni/Rafael-Ecommerce.git
      
2. create and activate virtualenv in project directory using commands:

    For Windows :
      virtualenv venv
      source venv/Scripts/activate
      
    For Linux :
      virtualenv venv
      source venv/bin/activate
      
3 install Requirements from requirements.txt file. Run command:
    pip install -r requirements.txt
    
4 Go to project folder using command:
    cd shopping/

5. Migrate the data using command
   python manage.py migrate

6. Then run app using command:
    python manage.py runserver
    
Open link : http://127.0.0.1:8000/

## Credits

### Content
- The text/images for home section and ecommerce data was copied from the  [GOOGLE]https://www.google.com/

### Media
- The photos used in this site were obtained from [GOOGLE]https://www.google.com/

### Acknowledgements


