package com.example.myothercatalog;

import android.os.Bundle;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;


public class DetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        String itemName = getIntent().getStringExtra("itemName");

        TextView detailTextView = findViewById(R.id.detailTextView);
        detailTextView.setText(itemName);
    }
}
