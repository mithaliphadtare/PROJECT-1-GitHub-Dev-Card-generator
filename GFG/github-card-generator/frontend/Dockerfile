# Use Nginx as a base image for serving static files
FROM nginx:alpine

# Copy the custom Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy the frontend files into the Nginx html directory
COPY . /usr/share/nginx/html

# Expose port 80
EXPOSE 80
