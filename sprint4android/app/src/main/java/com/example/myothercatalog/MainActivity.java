package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.app.Activity;
import android.os.Bundle;

import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    private RecyclerView recyclerView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        recyclerView = findViewById(R.id.recyclerView);

        // Llamada a la función para obtener y mostrar los datos JSON
        petition();
    }

    private void petition() {

        List<Item> itemList = new ArrayList<>();

        // Creamos una nueva solicitud JSON usando Volley
        JsonArrayRequest request = new JsonArrayRequest(
                Request.Method.GET,
                "https://raw.githubusercontent.com/RodrigoSantosNegro/DWES/main/resources/catalog.json",
                null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        // Respuesta JSON

                        try {
                            // Iteramos a través de los elementos del array JSON
                            for (int i = 0; i < response.length(); i++) {
                                // Obtener objeto JSON en la posición i
                                JSONObject jsonItem = response.getJSONObject(i);

                                Item item = new Item(jsonItem);
                                itemList.add(item);
                            }

                            // Actualizar el RecyclerView con los datos obtenidos
                            MyAdapter myAdapter = new MyAdapter(itemList, MainActivity.this);
                            recyclerView.setAdapter(myAdapter);
                            recyclerView.setLayoutManager(new LinearLayoutManager(MainActivity.this));

                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // Respuesta de error de la solicitud
                        error.printStackTrace();
                    }
                });

        // Agregamos la solicitud a la cola de Volley
        Volley.newRequestQueue(this).add(request);
    }

}