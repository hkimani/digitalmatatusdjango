FROM nginx:1.13.3

# Copy the Nginx configuration
RUN rm -f /etc/nginx/sites-enabled/default
COPY nginx.conf /etc/nginx/sites-enabled/default.conf

RUN ls

RUN mkdir -p /etc/nginx/certs

# Expose website on port
EXPOSE 80
EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]