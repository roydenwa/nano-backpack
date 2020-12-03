sap.ui.define([
  "./models",
], function() {
    return {
      createModel: function() {
        var oData = {
          robotIp = ""
        }
        var oModel = new sap.ui.model.json.JSONModel(oData);

        return oModel;
      }
    }
});
