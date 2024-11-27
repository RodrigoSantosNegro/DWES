<?php
// Conectar a la base de datos
$db = mysqli_connect('172.16.0.2', 'root', '1234', 'mysitedb') or die('Error de conexión');

// Obtener todos los libros
$query = 'SELECT * FROM tLibros';
$result = mysqli_query($db, $query) or die('Error en la consulta');
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de Libros</title>
    <style>
        /* Estilos */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 20px;
        }
        .book-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
        }
        .book {
            background-color: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 10px;
            width: 200px;
            margin: 10px;
            text-align: center;
        }
        .book img {
            max-width: 150px;
            max-height: 200px;
            object-fit: cover;
        }
        .book h2 {
            font-size: 18px;
            margin-bottom: 5px;
        }
        .book p {
            font-size: 14px;
            color: #555;
        }
        .book a {
            text-decoration: none;
            color: #007bff;
        }
	.enlace{
	    text-decoration: none;
	}
	.enlace:hover{
	    color: white;
	    background-color: grey;
	    padding: 5px;
	    border-radius: 5rem;
	}
    </style>
</head>
<body>

<h1>Lista de Libros</h1>

<div class="book-container">
    <?php
    // Mostrar los libros
    while ($row = mysqli_fetch_array($result)) {
        echo '<div class="book">';
        echo '<h2>' . $row['nombre'] . '</h2>';
        echo '<p>Autor: ' . $row['autor'] . '</p>';
        echo '<p>Año: ' . $row['año_publicacion'] . '</p>';
        echo '<img src="' . $row['url_imagen'] . '" alt="Imagen de ' . $row['nombre'] . '">';
        echo '<br>';
        // Enlace a detail.php con IDs
        echo '<a href="detail.php?id=' . $row['id'] . '">Ver detalles</a>';
        echo '</div>';
    }
    ?>

</div>
<a class="enlace"  href="/logout.php">Logout</a>
</body>
</html>
<?php
mysqli_close($db);
?>
