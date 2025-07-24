# Use Node.js 18 Alpine as base image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files first
COPY frontend/package*.json ./frontend/
COPY requirements.txt ./

# Install Python dependencies
RUN apk add --no-cache python3 py3-pip
RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Install Node.js dependencies
WORKDIR /app/frontend
RUN npm install

# Copy source code
COPY . .

# Expose ports
EXPOSE 5173 8000

# Start the application (frontend only for now)
CMD ["sh", "-c", "cd /app/frontend && npm run dev"] 