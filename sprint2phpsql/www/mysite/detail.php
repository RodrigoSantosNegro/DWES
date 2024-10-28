<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>

<html>
<body>
<?php
if (!isset($_GET['id'])) {
    die('No se ha especificado un libro');
}

$libro_id = $_GET['id'];

$query = "SELECT * FROM tLibros WHERE id = $libro_id";
$result = mysqli_query($db, $query) or die('Error en la consulta del libro');
$libro = mysqli_fetch_array($result);

if (!$libro) {
    die('Libro no encontrado');
}

// Mostramos detalles del libro
echo '<h1>'.$libro['nombre'].'</h1>';
echo '<img src="'.$libro['url_imagen'].'" alt="Imagen de '.$libro['nombre'].'" style="width:200px;height:300px;"><br>';
echo '<p>Autor: '.$libro['autor'].'</p>';
echo '<p>Año de publicación: '.$libro['año_publicacion'].'</p>';
?>

<h3>Comentarios:</h3>
<ul>
<?php
$query2 = "SELECT * FROM tComentarios WHERE libro_id = $libro_id";
$result2 = mysqli_query($db, $query2) or die('Error en la consulta de comentarios');


while ($comentario = mysqli_fetch_array($result2)) {
    echo '<li>'.$comentario['comentario'].'</li>';
}
?>
</ul>

<h3>Deja un nuevo comentario:</h3>
<form action="comment.php" method="post">
    <textarea rows="4" cols="50" name="new_comment" placeholder="Escribe tu comentario aquí..."></textarea><br>
    <input type="hidden" name="libro_id" value="<?php echo $libro_id; ?>">
    <input type="submit" value="Comentar">
</form>


<?php
mysqli_close($db);
?>
</body>
</html>
