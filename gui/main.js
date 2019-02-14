const electron = require('electron');
const url = require ('url');
const path = require('path');

const {app, BrowserWindow} = electron;

let mainWindow;

app.on('ready', function(){

  mainWindow = new BrowserWindow({width:1800,height:800,frame:false});

  mainWindow.loadURL(url.format({
    pathname: path.join(__dirname, 'index.html'),
    protocol:'file:',
    slashes:true
  }));

});