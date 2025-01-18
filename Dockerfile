# Use the official Nginx image as the base
FROM nginx:latest

# Copy the index.html file into the container's /usr/share/nginx/html directory
COPY index.html /usr/share/nginx/html/

# Expose port 80 so it can be accessed outside the container
EXPOSE 80