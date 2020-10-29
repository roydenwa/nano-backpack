FROM nikolaik/python-nodejs:python3.7-nodejs12

# install node-naoqi & update dependencies
RUN npm install naoqi --save && \
    sed -i 's/@ali\/socket.io-client/socket.io-client/' /node_modules/naoqi/lib/socket.js

CMD [ "node" ]
