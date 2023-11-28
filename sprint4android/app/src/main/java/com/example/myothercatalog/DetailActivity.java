package com.example.myothercatalog;

import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;


public class DetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        // Obtén datos del intent
        Intent intent = getIntent();
        String itemName = intent.getStringExtra("itemName");
        String itemImageUrl = intent.getStringExtra("itemImageUrl");
        String itemDescription = intent.getStringExtra("itemDescription");

        // Referencias a las vistas en el layout
        ImageView detailImageView = findViewById(R.id.detailItemImageView);
        TextView detailTitleTextView = findViewById(R.id.detailNameTextView);
        TextView detailDescriptionTextView = findViewById(R.id.detailItemDescriptionTextView);

        // Configurar las vistas con los datos recibidos
        detailTitleTextView.setText(itemName);
        detailDescriptionTextView.setText(itemDescription);

        // Cargar la imagen con Glide
        Glide.with(this).load(itemImageUrl).into(detailImageView);
    }
}
