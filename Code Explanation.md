# Project 1: simple web server

### What This Code Does:
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