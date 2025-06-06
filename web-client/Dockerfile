# Stage 1: Build the React app
FROM node:18-alpine as builder
WORKDIR /app
COPY package*.json ./
# We will run npm install later or expect it to be run manually for now
# RUN npm install
COPY . .
# RUN npm run build

# Stage 2: Serve the static files with Nginx
FROM nginx:stable-alpine
# COPY --from=builder /app/dist /usr/share/nginx/html
# For now, just put a placeholder index.html to signify successful setup
RUN echo "<html><body><h1>Web Client (Awaiting Build)</h1></body></html>" > /usr/share/nginx/html/index.html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
