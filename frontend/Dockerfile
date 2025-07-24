# Use official Node.js LTS (Alpine) image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package.json and lock files first (for better caching)
COPY frontend/package*.json ./

# Install dependencies
RUN npm install

# Copy application source
COPY frontend ./

# Expose Vite dev port
EXPOSE 5173

# Start dev server (use --host to listen on 0.0.0.0 so it is reachable outside container)
CMD ["npm", "run", "dev", "--", "--host", "--port", "5173"]