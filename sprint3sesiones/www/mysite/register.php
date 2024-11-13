<?php
// Conexión a la base de datos
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Error de conexión');

// Obtener datos del formulario
$email_posted = $_POST['email'];
$password_posted = $_POST['password'];
$confirm_password = $_POST['confirm_password'];
$nombre_posted = $_POST['nombre'];
$apellidos_posted = $_POST['apellidos'];

// Validaciones
if (empty($email_posted) || empty($password_posted) || empty($confirm_password) || empty($nombre_posted) || empty($apellidos_posted)) {
    echo "<p>Todos los campos son obligatorios.</p>";
    exit;
}

if ($password_posted !== $confirm_password) {
    echo "<p>Las contraseñas no coinciden.</p>";
    exit;
}

// Verificar si el correo ya existe
$query = "SELECT id FROM tUsuarios WHERE email = '$email_posted'";
$result = mysqli_query($db, $query) or die('Error en la consulta');
if (mysqli_num_rows($result) > 0) {
    echo "<p>El correo ya está registrado.</p>";
    exit;
}

// Cifrar la contraseña y guardar el usuario
$hashed_password = password_hash($password_posted, PASSWORD_DEFAULT);
$query = "INSERT INTO tUsuarios (nombre, apellidos, email, contraseña) VALUES ('$nombre_posted', '$apellidos_posted', '$email_posted', '$hashed_password')";
if (mysqli_query($db, $query)) {
    header('Location: main.php'); // Redirigir a la página principal en caso de éxito
    exit;
} else {
    echo "<p>Error al registrar el usuario.</p>";
}

// Cerrar la conexión
mysqli_close($db);
?>
