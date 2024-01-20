FROM node:16 AS base
WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend ./
EXPOSE 3000
CMD ["npm", "run", "dev"]

# ビルドステージ
FROM node:16 AS builder

WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend ./
RUN npm run build

# ランタイムステージ
FROM node:16

WORKDIR /app
COPY --from=builder /app/next.config.js ./
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package*.json ./
RUN npm install

EXPOSE 3000
CMD ["npm", "run", "dev"]