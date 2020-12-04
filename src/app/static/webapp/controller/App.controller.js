sap.ui.define([
  "sap/ui/core/mvc/Controller",
  "sap/m/MessageToast",
  "sap/ui/model/json/JSONModel",
  "../model/models"
], function(Controller, MessageToast, JSONModel, models) {
  "use strict";

  return Controller.extend("nao-nano-backpack.controller.App", {
    onInit: function() {
      this.getView().setModel(models.createModel());
    },

    callPrintMsg: function() {
      console.log(testMsg);
      printMsg();
    },

    callInitQiSession: function(ip) {
      initQiSession(ip);
    },

    callSpeak: function(msg) {
      speak(msg);
    },

    callWalk: function(x, y, theta) {
      walk(x, y, theta);
    }
  });

});
