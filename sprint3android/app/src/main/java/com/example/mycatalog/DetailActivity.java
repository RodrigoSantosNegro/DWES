package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ImageView;

public class DetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);
        ImageView circularImageView = findViewById(R.id.circularImageView);
        circularImageView.setImageResource(R.drawable.);

        circularImageView.setScaleType(ImageView.ScaleType.CENTER_CROP);
        circularImageView.setBackground(getResources().getDrawable(R.drawable.circular_image_border));
    }
}