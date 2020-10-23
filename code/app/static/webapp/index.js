// handles your app startup, routing and other functions of your application
// and does require other modules to add functionality
sap.ui.define([
  "sap/ui/core/mvc/XMLView"
], function(XMLView) {
  "use strict";

  XMLView.create({viewName: "nao-nano-backpack.view.App"}).then(function(oView) {
    oView.placeAt("content");
  });
});
