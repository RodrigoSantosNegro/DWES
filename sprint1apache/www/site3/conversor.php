<html>
<body>
<h1>Conversor de longitudes</h1>
<p>Convierte de la unidad especificada a metros</p>
<p>
<?php
if ($_GET["unidad"] == "pulgada") {
$v_pulgadas = $_GET["cantidad"];
$v_metros = $v_pulgadas * 0.0254;
echo $v_pulgadas."pulgada(s) = ".$v_metros." metro(s)";
} else {
echo "Unidad no soportada";
}
?>
</p>
</body>
</html>
