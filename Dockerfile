# Use Node.js 18 Alpine as base image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files first
COPY frontend/package*.json ./frontend/
COPY requirements.txt ./

# Install Python dependencies
RUN apk add --no-cache python3 py3-pip
RUN pip3 install --break-system-packages -r requirements.txt

# Install Node.js dependencies
WORKDIR /app/frontend
RUN npm install

# Copy source code
COPY . .

# Expose ports
EXPOSE 3000 8000

# Start the application
CMD ["sh", "-c", "cd /app/frontend && npm run dev & cd /app/backend && python3 main.py"] 