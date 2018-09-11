<!DOCTYPE html>
<html>
<head>
<title> LOGGED OUT </title>
</head>
<body>
<h3> LOGGED OUT </h3>
You have been logged out. <a href="index.php"> Back to the homepage </a>

</body>
</html>


<?php
setcookie("id", $username, time()-3600);
setcookie("timeloggedin", time(), time()-3600);
destroySession();
?>