# Stage 1: Build React App
FROM node:22.11.0-alpine AS builder

WORKDIR /app
COPY . .

# Install dependencies and build
RUN npm install
RUN npm run build

# Stage 2: Serve with Nginx
FROM nginx:alpine

# Copy production build to Nginx's public directory
COPY --from=builder /app/build /usr/share/nginx/html

# Copy nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Optional: Default fallback config
COPY public/config.js /usr/share/nginx/html/config.js

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
