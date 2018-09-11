
<?php
    extract ($_POST);
 $username = $_POST['username'];
 $password = $_POST['password'];

    // Add person to the passwd.txt file
    $file = fopen("passwd.txt", "a");
    fwrite($file, $username.":".md5($password)."\n");
    fclose($file);
print <<<THANKS
<p> Thank you for creating an account! </p>
THANKS;


?>