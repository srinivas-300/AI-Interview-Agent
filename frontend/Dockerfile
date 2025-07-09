FROM node:18

WORKDIR /app

# Copy both package files before installing
COPY package.json package-lock.json ./
RUN npm install

# Now copy the actual source files
COPY . .

EXPOSE 3000
CMD ["npm", "start"]
