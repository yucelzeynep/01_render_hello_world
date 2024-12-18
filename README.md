# TODO: Hello World 
You can create a "Hello World" application on Heroku without entering payment information by following these steps. Heroku offers a free tier that allows you to deploy simple applications without requiring a credit card.

### Step 1: Sign Up for Heroku

1. **Visit the Heroku Website**: Go to [Heroku](https://www.heroku.com/).
2. **Create an Account**: Click on the "Sign Up for Free" button and fill in the required information. You should be able to create a free account without needing to enter payment information.

### Step 2: Install the Heroku CLI

1. **Download and Install the Heroku CLI**: Depending on your operating system, you can find installation instructions [here](https://devcenter.heroku.com/articles/heroku-cli#download-and-install). Make sure to install it on your machine.

### Step 3: Create a Simple Application

1. **Create a New Directory**: Open your terminal or command prompt and create a new directory for your application.
   ```bash
   mkdir hello-world
   cd hello-world
   ```

2. **Create a Simple Web Application**:
   - You can create a simple Node.js application. First, create a `package.json` file:
   ```bash
   npm init -y
   ```
   - Install the `express` package:
   ```bash
   npm install express
   ```
   - Create an `index.js` file and add the following code:
   ```javascript
   const express = require('express');
   const app = express();
   const PORT = process.env.PORT || 3000;

   app.get('/', (req, res) => {
       res.send('Hello World!');
   });

   app.listen(PORT, () => {
       console.log(`Server is running on port ${PORT}`);
   });
   ```

3. **Create a `Procfile`**: This file tells Heroku how to run your app. Create a file named `Procfile` (with no file extension) and add the following line:
   ```
   web: node index.js
   ```

### Step 4: Deploy to Heroku

1. **Log in to Heroku**: Run the following command and follow the prompts:
   ```bash
   heroku login
   ```

2. **Create a New Heroku App**:
   ```bash
   heroku create
   ```

3. **Deploy Your Application**:
   - Initialize a git repository:
   ```bash
   git init
   ```
   - Add your files to the repository:
   ```bash
   git add .
   git commit -m "Initial commit"
   ```
   - Deploy to Heroku:
   ```bash
   git push heroku master
   ```

### Step 5: Open Your App

Once the deployment is complete, you can open your application in your web browser using:
```bash
heroku open
```

You should see "Hello World!" displayed in your browser.

### Notes

- **Free Tier Limitations**: The free tier has some limitations, such as sleeping after 30 minutes of inactivity, but it's great for simple projects.
- **No Payment Info Required**: As long as you are using the free tier and do not exceed the limits, you should not be prompted for payment information.

By following these steps, you should have a simple "Hello World" application running on Heroku without needing to enter any payment information.
