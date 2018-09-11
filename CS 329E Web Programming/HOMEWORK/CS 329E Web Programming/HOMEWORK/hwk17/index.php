<!DOCTYPE html>

<html>
<head>
  <script src="script.js"></script>
</head>
<body>
  <h1>Registration</h1>
  <?php
  if($_SERVER['REQUEST_METHOD'] === 'POST'){
    $username = $_POST["username"];
    $password = $_POST["password"];
    $file = fopen("passwd", "r");
    $userlist = Array();
    while(!feof($file)){
      $line = fgets($file);
      $line_pieces = explode(":", $line);
      $userlist[$line_pieces[0]] = $line_pieces[1];
    }
    fclose($file);
    if(!array_key_exists($username, $userlist)){
      $file2 = fopen("passwd", "a");
      //Encryption
      $key = 'CS329';
      $method = 'aes-128-cbc';
      $password_encrypted = openssl_encrypt ($password, $method, $key);
      fwrite($file2, $username.":".$password_encrypted."\n");
      fclose($file2);
      echo "<p>User Registered</p>";
    }else{
      echo "<p>User Already Taken</p>";
    }
  }
  ?>
  <!-- onkeyup onchange oninput -->
  <form method="post">
    <span>Username :</span><input type="text" id="usename" name="username" onkeyup="checkName(this.value)" /><br />
    <span>Password :</span><input type="text" id="password" name="password" /><br />
    <input type="submit" name="submit" />
    <input type="reset" name="reset" />
  </form>
  <p><a href="passwd"> List of usernames </a></p>
</body>
</html>