sap.ui.define([
  "sap/ui/core/mvc/Controller",
  "sap/m/MessageToast",
  "sap/ui/model/json/JSONModel",
  "../model/models"
], function(Controller, MessageToast, JSONModel, models) {
  "use strict";

  return Controller.extend("nao-nano-backpack.controller.App", {
    onPress: function() {
      MessageToast.show("Hello UI5!");
      this.byId("app").to(this.byId("page2"));
    },

    goBack: function() {
      this.byId("app").to(this.byId("page1"));
    },

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
    },

    onChange: function(oEvent) {
      var bState = oEvent.getParameter("state");
      this.byId("ready").setVisible(bState);
    }
  });

});
