<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora PHP</title>
</head>
<body>

<h1>Calculadora</h1>
<form action="calculadora.php" method="post">
    <label for="numero1">Número 1:</label><br>
    <input type="number" id="numero1" name="numero1" step="any" required>
	<br><br>

    <label for="numero2">Número 2:</label>
	<br>
    <input type="number" id="numero2" name="numero2" step="any" required>
	<br><br>

    <label for="operacion">Operación:</label>
	<br>
    <select id="operacion" name="operacion" required>
        <option value="suma">Suma</option>
        <option value="resta">Resta</option>
        <option value="multiplicacion">Multiplicación</option>
        <option value="division">División</option>
    </select>
	<br><br>

    <input type="submit" value="Calcular">
</form>

<p>
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $numero1 = $_POST["numero1"];
    $numero2 = $_POST["numero2"];
    $operacion = $_POST["operacion"];
    $resultado = 0;

    // Validar que los números sean válidos
    if (!is_numeric($numero1) || !is_numeric($numero2)) {
        echo "Por favor, ingresa números válidos.";
    } else {
        // Usamos switch para determinar la operación
        switch ($operacion) {
            case "suma":
                $resultado = $numero1 + $numero2;
                echo "$numero1 + $numero2 = $resultado";
                break;
            case "resta":
                $resultado = $numero1 - $numero2;
                echo "$numero1 - $numero2 = $resultado";
                break;
            case "multiplicacion":
                $resultado = $numero1 * $numero2;
                echo "$numero1 * $numero2 = $resultado";
                break;
            case "division":
                // Validar que no se divida entre 0
                if ($numero2 == 0) {
                    echo "Error: No se puede dividir entre 0.";
                } else {
                    $resultado = $numero1 / $numero2;
                    echo "$numero1 / $numero2 = $resultado";
                }
                break;
            default:
                echo "Operación no válida.";
                break;
        }
    }
}
?>
</p>

</body>
</html>
