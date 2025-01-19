# Project 1: Simple Web Server
# Project 2: Simple Flask Demo

## Table of Contents
- [Project 1 Explanation](#project-1-explanationindexhtml)
- [Project 2 Explanation](#project-2-simple-flask-project)

### Project 1 Explanation(index.html):
This HTML code creates a **login page** for a website. It includes a form where users can input their **username** and **password** and submit them. The page has simple styling to make the form look neat and centered on the screen. It also provides a "Forgot Password?" link below the form.

---

### Explanation of Each Tag:

1. **`<!DOCTYPE html>`**: 
   - Declares the document type and version of HTML (HTML5).

2. **`<html lang="en">`**: 
   - Specifies that the document is written in English (`lang="en"`).

3. **`<head>`**: 
   - Contains metadata and other head elements like the title, character set, and viewport settings.

4. **`<meta charset="UTF-8">`**: 
   - Defines the character encoding for the document as UTF-8, which supports all characters.

5. **`<meta name="viewport" content="width=device-width, initial-scale=1.0">`**: 
   - Ensures the page is responsive and adjusts to different screen sizes on mobile devices.

6. **`<title>`**: 
   - Sets the title of the webpage that appears on the browser tab.

7. **`<style>`**: 
   - Contains internal CSS to style the elements on the page.

8. **`<body>`**: 
   - Contains the content of the webpage that is visible to users.

9. **`<div class="login-container">`**: 
   - A container for the login form with some styling (centered on the page).

10. **`<h2>`**: 
   - Displays the heading "Login" at the top of the page, centered.

11. **`<form action="/login" method="POST">`**: 
   - Defines the form for user input, sending data to the `/login` route using the POST method.

12. **`<div class="form-group">`**: 
   - A wrapper for each form input field with some spacing.

13. **`<label for="username">`**: 
   - Provides a label for the username input field.

14. **`<input type="text" id="username" name="username" required>`**: 
   - Defines a text input field for the username with `required` validation.

15. **`<div class="form-group">`**: 
   - Another wrapper for the password input field.

16. **`<label for="password">`**: 
   - Provides a label for the password input field.

17. **`<input type="password" id="password" name="password" required>`**: 
   - Defines a password input field (masked text) with `required` validation.

18. **`<button type="submit">Log In</button>`**: 
   - A button that submits the form when clicked.

19. **`<p>`**: 
   - Contains text or links, here it holds the "Forgot Password?" link.

20. **`<a href="/forgot-password">`**: 
   - A hyperlink that leads to the "forgot-password" page.


### Explanation of Each Line in the Dockerfile:

1. **`FROM nginx:latest`**: 
   -  It pulls the latest version of the official NGINX image from Docker Hub and sets it as the starting point for your Docker image. This image includes everything needed to run NGINX.

2. **`COPY index.html /usr/share/nginx/html/`**: 
   - It copies the `index.html` file from the same directory as the Dockerfile to the `/usr/share/nginx/html/` directory in the container. This is the default directory NGINX serves files from, so this makes your `index.html` accessible when the container runs.

3. **`EXPOSE 80`**: 
   - By exposing port 80, the NGINX server running inside the container will be able to receive web traffic on port 80, which is the default HTTP port. This makes the NGINX server accessible to the outside world.

---

## **Steps for Running a Simple NGINX Web Page with Docker**

1. **Write the `index.html` (Login Page)**:
   - You create the `index.html` file for the login page, which contains the structure and styling of the page (using HTML and CSS).

2. **Write the `Dockerfile`**:
   - The **Dockerfile** defines the base image (NGINX), copies the `index.html` into the container's NGINX directory, and exposes port 80 to allow access to the web page in the browser.

3. **Build the Docker Image**:
   - You use the following command to build the Docker image:
     ```bash
     docker build -t login-page .
     ```
     - `-t` specifies the **tag** for the image (in this case, `login-page`).
     - `.` refers to the current directory where the `Dockerfile` is located.
   
4. **Run the Docker Container**:
   - Once the image is built, you run the Docker container with this command:
   
     ```bash
     docker run -d --name loginpage -p 8080:80 login-page
     ```
     - `-d` runs the container in **detached** mode (in the background).

     - `--name loginpage` gives the container a custom **name** (`loginpage`).

     - `-p 8080:80` binds port 8080 on your **host machine** to port 80 in the **container** so that the web page can be accessed from your browser.

     - `login-page` specifies the **image** to use, which you previously built.

---

### **Summary**:

1. You create an **HTML login page** (`index.html`).
2. You write a **Dockerfile** to use the NGINX image, copy the login page, and expose port 80.
3. You **build** the Docker image with the `docker build` command.
4. You **run** the Docker container, making the login page accessible on your browser by mapping port 8080 to port 80.

This is how you use Docker to deploy a simple **login page** with **NGINX**!

# Project 2: Simple Flask Project

### **Project 2 Explanation(app.py)**

This project is a basic **Flask web application** that runs a simple web server. The app responds with **"Hello World"** when you visit the root URL (`/`). It is a very basic example of how to use the Flask framework in Python to create a web application. Means vThis simple project demonstrates how to create and run a **Flask web application** with a single route that returns a basic response.

### **Line-by-Line Explanation:**

1. **`from flask import Flask`**:
   Python used to build web applications.
   - You need this to create and configure a Flask app.

2. **`app = Flask(__name__)`**:
   - `Flask(__name__)` initializes the Flask application. The app will use the current module (`__name__`) to set up routes and handle requests.

3. **`@app.route('/')`**:
    - This tells Flask that the following function should run when a user visits the root URL (`/`), which is typically the homepage of a web application.

4. **`def hello_world():`**:
    - This function simply returns the string `'Hello World'`, which is displayed to the user in the browser when they access the app.

5. **`return 'Hello World'`**:
   - When you visit `http://localhost:5000/` in a browser, it will display the text `Hello World`.

6. **`if __name__ == '__main__':`**:
   - If the script is being executed directly (not imported), the following block of code will run.

7. **`app.run(host='0.0.0.0', port=5000)`**:
   - `host='0.0.0.0'` allows the app to be accessible from any machine on the network. `port=5000` specifies the port number to run the server on. By default, Flask runs on port 5000.
   
   - **Note**: This is useful during development to test the application in the browser by visiting `http://localhost:5000/`.

---
### **Requirements.txt**

These are version specifications for the Python libraries **Flask** and **Werkzeug** in a **requirements.txt** file. Here's what each part means:

---

### **Flask==2.0.1**
- **Flask** is a lightweight web framework for Python used to build web applications.
- **Version 2.0.1** specifies that you want to use version **2.0.1** of Flask.
- **Why it matters**: Specifying the exact version ensures that the project will use this specific version of Flask, which helps maintain compatibility and avoid issues from potential breaking changes in newer versions.

---

### **Werkzeug==2.0.0**
- **Werkzeug** is a comprehensive WSGI (Web Server Gateway Interface) utility library that Flask relies on. It provides utilities for HTTP request/response handling, routing, and many other underlying web framework functions.
- **Version 2.0.0** indicates that you want to use version **2.0.0** of Werkzeug. 
- **Why it matters**: Specifying the version ensures compatibility between Flask and Werkzeug. As both libraries are closely tied together, it’s important that you match versions correctly to avoid any incompatibility.

---

### requirements.txt 
- This file is used to specify the Python dependencies for your project.
- By including the versions (e.g., `Flask==2.0.1` and `Werkzeug==2.0.0`), you ensure that anyone who installs your project dependencies will get the exact versions you’ve used, preventing version mismatch issues.
- You can install all dependencies listed in the `requirements.txt` file with the following command:

  ```bash
  pip install -r requirements.txt
  ```

---

## **Steps to Create the Dockerfile for Flask Application**

### **Create a Dockerfile**:
  
### **Dockerfile Example for Flask Application**:

```dockerfile
# Step 1: Use the official Python image as the base image
FROM python:3.9-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the local requirements.txt file into the container
COPY requirements.txt /app/

# Step 4: Install the dependencies from the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of your application code into the container
COPY . /app/

# Step 6: Expose the port that your Flask app will run on
EXPOSE 5000

# Step 7: Define the command to run the Flask application
CMD ["python", "app.py"]
```

---
### **Steps to Build and Run the Docker Container:**

1. **Build the Docker Image**:
    ```bash
     docker build -t flask-app .
     ```

2. **Run the Docker Container**:
   - After the image is built, run the container with:
     ```bash
     docker run -d -p 5000:5000 --name flask-container flask-app
     ```
     - `-d`: Runs the container in detached mode.
     - `-p 5000:5000`: Maps port 5000 on your local machine to port 5000 in the container.
     - `--name flask-container`: Gives the container a name (`flask-container`).
     - `flask-app`: The name of the image you created in the previous step.

---

### **Accessing Your Flask App**:

Once the container is running, open your web browser and go to:

```http
http://localhost:5000
```

You should see the Flask application running, and it will display **"Hello World"**.

---
With this approach, Docker helps ensure that your Flask application runs in a consistent environment across different machines.

