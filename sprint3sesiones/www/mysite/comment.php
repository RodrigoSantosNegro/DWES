<?php
$db = mysqli_connect('172.16.0.2', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
<body>
<?php
// Iniciar o reanudar la sesión para comprobar si el usuario está logueado
session_start();

$libro_id = $_POST['libro_id'];
$comentario = $_POST['new_comment'];

// Determinar el usuario_id: NULL si no está logueado
$user_id_a_insertar = 'NULL';
if (!empty($_SESSION['user_id'])) {
    $user_id_a_insertar = $_SESSION['user_id'];
}

// Insertar el comentario con el usuario_id (si aplica)
$query = "INSERT INTO tComentarios(comentario, libro_id, usuario_id, fecha)
VALUES ('".$comentario."', ".$libro_id.", ".$user_id_a_insertar.", CURRENT_TIMESTAMP)";
mysqli_query($db, $query) or die('Error');

echo "<p>Nuevo comentario ";
echo mysqli_insert_id($db);
echo " añadido</p>";
echo "<a href='/detail.php?id=".$libro_id."'>Volver</a>";

// Cerrar la conexión
mysqli_close($db);
?>
</body>
</html>
