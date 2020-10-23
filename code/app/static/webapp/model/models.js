sap.ui.define([
  "./models",
], function() {
    return {
      createModel: function() {
        var oData = {
          features: [
            "Enterprise-Ready Web Toolkit",
            "Powerful Development Concepts",
            "Feature-Rich UI Controls",
            "Consistent User Experience",
            "Free and Open Source",
            "Responsive Across Browsers and Devices"
          ]
        }

        var oModel = new sap.ui.model.json.JSONModel(oData);

        return oModel;
      }
    }
});
