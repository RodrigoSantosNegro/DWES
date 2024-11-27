<?php
// Conexión a la base de datos
$db = mysqli_connect('172.16.0.2', 'root', '1234', 'mysitedb') or die('Error de conexión');

// Obtener datos del formulario
$email_posted = $_POST['f_email'];
$password_posted = $_POST['f_password'];

// Consulta para verificar si el usuario existe
$query = "SELECT id, contraseña FROM tUsuarios WHERE email = '$email_posted'";
$result = mysqli_query($db, $query) or die('Error en la consulta');

if (mysqli_num_rows($result) > 0) {
    // Obtener la fila de resultados
    $only_row = mysqli_fetch_array($result);

    // Verificar la contraseña usando password_verify
    if (password_verify($password_posted, $only_row['contraseña'])) {
        session_start();
        $_SESSION['user_id'] = $only_row['id'];
        header('Location: main.php'); // Redirigir a la página principal en caso de éxito
        exit;
    } else {
        echo '<p>Contraseña incorrecta</p>';
    }
} else {
    echo '<p>Usuario no encontrado con ese email</p>';
}

// Cerrar la conexión
mysqli_close($db);
?>
