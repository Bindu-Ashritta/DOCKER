## Project 1: simple web server
## Technologies used: Docker, Nginx, Markup Language
### Table of contents
- [Nginx and Installation](#nginx-and-installation)
- [Docker and Installation](#1-install-docker-on-windows)
- [Language]()

### Step-by-step instructions
- Install Docker: Make sure Docker is installed on your system.

- Create the project directory: Create a new folder and an index.html file inside it that will be served by Nginx.

- Write the Dockerfile: A Dockerfile is a script that defines the environment of the container. It tells Docker what base image to use, what files to include, and what ports to expose:

## Nginx and Installation

#### NGINX - Definition and Explanation

#### Technical Definition:
**NGINX** is an open-source web server software that also functions as a reverse proxy, load balancer, and HTTP cache. It is designed to handle high traffic websites and services with ease and efficiency.

#### Simple Explanation:
NGINX is like a **super-efficient traffic manager** for websites. It handles requests from users, serves them the correct web pages (like HTML files), and can distribute the traffic across multiple servers to ensure no single server gets overwhelmed.

---

### When to Use NGINX:
- **Web Servers**: When you need a fast and lightweight server to serve static content (like HTML, CSS, JS).
- **Reverse Proxy**: When you want to forward requests from the internet to other internal services (e.g., apps or databases).
- **Load Balancer**: When you need to distribute traffic evenly across multiple servers to improve performance and prevent overload.
- **API Gateway**: When you need a system to manage, monitor, and route API requests.

---

### Why Use NGINX:
- **Performance**: NGINX is known for its speed and efficiency, especially in handling many simultaneous connections. It’s much faster and uses less memory than traditional web servers like Apache.
- **Scalability**: It allows you to scale your application seamlessly by distributing traffic across multiple servers.
- **Reliability**: It ensures that your application remains available and performant even during high traffic periods.

---

### Topics to Cover for a Good Understanding of NGINX:
1. **Basic NGINX Configuration**: How to set up and configure NGINX as a web server and reverse proxy.
2. **Load Balancing**: Understanding how NGINX distributes traffic between multiple backend servers.
3. **SSL/TLS Configuration**: How to enable HTTPS for secure communication.
4. **Caching**: Implementing caching to improve performance and reduce server load.
5. **Security**: Configuring NGINX to protect against security threats like DDoS attacks, bot traffic, and more.
6. **Logs and Monitoring**: Using NGINX logs to monitor traffic, errors, and performance.

---

### Companies Using NGINX and for What Purpose:
1. **Netflix**: Uses NGINX for its **reverse proxy and load balancing** to handle millions of users streaming content simultaneously.
2. **Dropbox**: Uses NGINX as a **web server** and **load balancer** to manage requests and ensure fast file synchronization.
3. **Airbnb**: Utilizes NGINX to handle **HTTP requests** and serve dynamic content at scale.
4. **GitHub**: Uses NGINX to manage **API requests**, distribute traffic across multiple servers, and optimize performance.

---

### Steps to Install NGINX:

1. **Update System Packages**:
   Open your terminal and update the system packages.
   ```bash
   sudo apt update
   ```

2. **Install NGINX**:
   Install NGINX from the official repository.
   ```bash
   sudo apt install nginx
   ```

3. **Start and Enable NGINX**:
   Start the NGINX service and enable it to run on system boot.
   ```bash
   sudo systemctl start nginx
   sudo systemctl enable nginx
   ```

4. **Check NGINX Status**:
   Verify that NGINX is running properly.
   ```bash
   sudo systemctl status nginx
   ```

5. **Allow HTTP/HTTPS Traffic**:
   Allow traffic on ports 80 (HTTP) and 443 (HTTPS) through the firewall.
   ```bash
   sudo ufw allow 'Nginx Full'
   ```

6. **Access NGINX Web Page**:
   Open your web browser and enter the server's IP address. You should see the default NGINX welcome page.
   ```text
   http://your-server-ip
   ```

7. **Configure NGINX**:
   You can configure NGINX by editing its configuration file at `/etc/nginx/nginx.conf` or create new server blocks for your websites at `/etc/nginx/sites-available/`.

8. **Test NGINX Configuration**:
   Before restarting NGINX after configuration changes, test if the configuration file is valid.
   ```bash
   sudo nginx -t
   ```

9. **Restart NGINX**:
   Restart NGINX to apply any changes.
   ```bash
   sudo systemctl restart nginx
   ```

---

### Steps to Install NGINX on Windows

While NGINX is primarily designed for Linux, you can still install it on Windows for development or testing purposes. Here’s how to do it:

---

### 1. **Download NGINX for Windows**
   - Visit the official NGINX website: [NGINX Download Page](https://nginx.org/en/download.html).
   - Download the **stable version** of NGINX for Windows (usually in `.zip` format).

### 2. **Extract the NGINX Files**
   - Once downloaded, **extract** the `.zip` file to a folder on your system, such as `C:\nginx`.

### 3. **Run NGINX**
   - Open **Command Prompt** (as Administrator).
   - Navigate to the directory where you extracted NGINX:
     ```bash
     cd C:\nginx
     ```
   - Start NGINX by running the following command:
     ```bash
     start nginx
     ```

### 4. **Verify NGINX is Running**
   - Open your **web browser** and go to `http://localhost`. If NGINX is running correctly, you should see the default NGINX welcome page.

### 5. **Stop NGINX**
   - To stop NGINX, return to the Command Prompt and run:
     ```bash
     nginx -s stop
     ```

### 6. **Start NGINX Again**
   - If you need to restart NGINX, use:
     ```bash
     nginx -s reload
     ```
---

### Summary:
- **Download** and **extract** the NGINX files.
- Use **Command Prompt** to **start NGINX**.
- **Verify** by visiting `http://localhost` in your browser.
- **Edit** the `nginx.conf` file for custom configurations.

NOTE:

NGINX on Windows is typically used for development, and it is not recommended for production use, as NGINX for Windows does not have the same performance and reliability as on Linux-based systems.

### Summary:
- **NGINX** is a fast, efficient web server and reverse proxy.
- Use it when you need performance, scalability, and load balancing.
- Companies like Netflix, Dropbox, and GitHub use NGINX for serving content and distributing traffic.
- Installation is straightforward and involves updating packages, installing NGINX, and configuring the server.

## Steps for Docker Installation
---

### **1. Install Docker on Windows**

#### **Step 1: Check System Requirements**
- **Windows 10 64-bit**: Pro, Enterprise, or Education edition (for Hyper-V support).
- **Windows 11**: Any edition that supports Hyper-V.

#### **Step 2: Download Docker Desktop for Windows**
- Visit the official Docker download page: [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop).
- Download the installer for Docker Desktop.

#### **Step 3: Install Docker Desktop**
1. Once the download is complete, run the installer (`Docker Desktop Installer.exe`).
2. Follow the installation wizard, accepting the default settings.
3. During installation, Docker will install **WSL 2** (Windows Subsystem for Linux version 2) if it’s not already enabled.
   
#### **Step 4: Start Docker Desktop**
- After installation, search for “Docker Desktop” in the **Start Menu** and open it.
- Docker will initialize, and you should see the Docker icon in your system tray.

#### **Step 5: Verify Installation**
- Open a **Command Prompt** or **PowerShell** and run:
  ```bash
  docker --version
  ```
- You should see the Docker version installed.

#### **Step 6: Enable Virtualization (if necessary)**
- Docker for Windows relies on **Hyper-V** and **Windows Subsystem for Linux 2 (WSL 2)**. If virtualization is not enabled, follow these steps:
  1. Go to **Control Panel > Programs > Turn Windows Features On or Off**.
  2. Enable **Hyper-V** and **Virtual Machine Platform**.
  3. Restart your computer.

---

### **2. Install Docker on Linux (Ubuntu)**

#### **Step 1: Update System Packages**
Before installing Docker, it’s a good idea to update the system’s package index.
```bash
sudo apt update
```

#### **Step 2: Install Required Dependencies**
Install required packages for Docker installation.
```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

#### **Step 3: Add Docker’s Official GPG Key**
This step ensures that the software you're installing is trusted.
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

#### **Step 4: Add Docker Repository**
Add the Docker repository to your list of sources so you can install Docker from it.
```bash
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

#### **Step 5: Update Package Index Again**
Now, update your package index to include the Docker packages.
```bash
sudo apt update
```

#### **Step 6: Install Docker**
Install the Docker package using `apt`.
```bash
sudo apt install docker-ce
```

#### **Step 7: Start and Enable Docker**
Enable Docker to start automatically with the system and then start the Docker service.
```bash
sudo systemctl enable docker
sudo systemctl start docker
```

#### **Step 8: Verify Docker Installation**
To ensure Docker is installed correctly, run:
```bash
docker --version
```
You should see the version of Docker installed.

#### **Step 9: Run Docker Without sudo (Optional)**
By default, Docker commands require `sudo` to run. If you want to run Docker commands without `sudo`, add your user to the `docker` group:
```bash
sudo usermod -aG docker $USER
```
Then, log out and log back in or restart the system.

#### **Step 10: Verify Docker is Running**
You can verify if Docker is running by using the following command:
```bash
sudo systemctl status docker
```
It should show Docker as "active" or "running."

---

After installation, you can start running Docker containers and images!


## Languages

- **HTML** is used to structure web content.
- **CSS** is used to style and design that content.
- A **Dockerfile** automates the creation of a Docker image by defining the environment and software needed for an application.


