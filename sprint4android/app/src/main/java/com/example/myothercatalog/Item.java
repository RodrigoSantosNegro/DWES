package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

public class Item {
    private String itemName;
    private String itemDescription;
    private String itemUrl;

    public Item(JSONObject data) throws JSONException {
        this.itemName = data.getString("name");
        this.itemDescription = data.getString("description");
        this.itemUrl = data.getString("image_url");
    }

    public String getItemName() {
        return itemName;
    }

    public String getItemDescription() {
        return itemDescription;
    }

    public String getItemUrl() {
        return itemUrl;
    }
}

