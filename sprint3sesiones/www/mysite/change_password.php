<?php
session_start();
if (!isset($_SESSION['user_id'])) {
    echo "<p>Error: Debes iniciar sesión para cambiar tu contraseña.</p>";
    exit;
}

$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Error de conexión');

$current_password = $_POST['current_password'];
$new_password = $_POST['new_password'];
$confirm_new_password = $_POST['confirm_new_password'];
$user_id = $_SESSION['user_id'];

// Validamos que la nueva contraseña y su confirmación coincidan
if ($new_password !== $confirm_new_password) {
    echo "<p>Las nuevas contraseñas no coinciden.</p>";
    exit;
}

// Obtenemos la contraseña actual del usuario desde la base de datos
$query = "SELECT contraseña FROM tUsuarios WHERE id = $user_id";
$result = mysqli_query($db, $query) or die('Error en la consulta');
$row = mysqli_fetch_assoc($result);

if (!$row || !password_verify($current_password, $row['contraseña'])) {
    echo "<p>La contraseña actual es incorrecta.</p>";
    exit;
}

// Ciframos la contraseña
$hashed_new_password = password_hash($new_password, PASSWORD_DEFAULT);

// Actualizamos en la bd
$update_query = "UPDATE tUsuarios SET contraseña = '$hashed_new_password' WHERE id = $user_id";
if (mysqli_query($db, $update_query)) {
    echo "<p>Contraseña actualizada correctamente.</p>";
} else {
    echo "<p>Error al actualizar la contraseña.</p>";
}

mysqli_close($db);
?>
