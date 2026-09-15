FROM node:20-alpine AS deps

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm ci --omit=dev

FROM node:20-alpine AS runner

WORKDIR /app

COPY --from=deps /app/node_modules ./node_modules

COPY server.js ./
COPY package.json ./

USER node

EXPOSE 3001

CMD ["node", "server.js"]
