FROM node:12.19.0-buster

# install node-naoqi & update dependencies
RUN npm install naoqi --save && \
    sed -i 's/@ali\/socket.io-client/socket.io-client/' /node_modules/naoqi/lib/socket.js

CMD [ "node" ]
