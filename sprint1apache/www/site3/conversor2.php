<html>
<body>
<h1>Conversor de longitudes</h1>
<p>Convierte de la unidad especificada a metros</p>
<p>
<?php
if (isset($_POST["funidad"])) {
    $cantidad = $_POST["fcantidad"];
    
    if (!is_numeric($cantidad)) {
        echo "Por favor ingresa una cantidad válida.";
    } else {
        if ($_POST["funidad"] == "pulgada") {
            $v_metros = $cantidad * 0.0254;
            echo $cantidad." pulgada(s) = ".$v_metros." metro(s)";
        } elseif ($_POST["funidad"] == "pie") {
            $v_metros = $cantidad * 0.3048;
            echo $cantidad." pie(s) = ".$v_metros." metro(s)";
        } else {
            echo "Unidad no soportada";
        }
    }
}
?>
</p>
<p>Realiza una nueva conversión:</p>
<form action="/conversor2.php" method="post">
    <label for="cantidad_input">Cantidad:</label><br>
    <input type="text" id="cantidad_input" name="fcantidad"><br><br>
    
    <input type="radio" id="pulgada_input" name="funidad" value="pulgada">
    <label for="pulgada_input">Pulgada(s)</label><br>
    
    <input type="radio" id="pie_input" name="funidad" value="pie">
    <label for="pie_input">Pie(s)</label><br>
    
    <input type="radio" id="otro_input" name="funidad" value="otro">
    <label for="otro_input">Otro</label><br><br>
    
    <input type="submit" value="Convertir">
</form>
</body>
</html>

