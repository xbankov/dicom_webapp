# Use an official Node.js runtime as the base image
FROM node:14

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json into the container
COPY package*.json ./

# Install Node.js dependencies
RUN npm install

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the Vue.js app will run on (default: 8080)
EXPOSE 8080

# Command to run the Vue.js application
CMD ["npm", "run", "serve"]
