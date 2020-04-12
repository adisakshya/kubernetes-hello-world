FROM node:latest
EXPOSE 8081
COPY server.js .
CMD [ "node", "server.js" ]