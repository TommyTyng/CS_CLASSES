<!DOCTYPE html>

<html>
<head>
  <title>Potluck Dinner</title>
  <link rel="stylesheet" type="text/css" href="dinner.css" />
  <script src="dinner.js"></script>
</head>

<?php
function start(){
  if(!isset($_COOKIE["id"])){
    if($_SERVER['REQUEST_METHOD'] === 'POST'){
      if(isset($_POST["username"])){
        $username = $_POST["username"];
        $password = $_POST["password"];
        $key = 'CS329';
        $method = 'aes-128-cbc';
        $cipher_text = openssl_encrypt ($password, $method, $key);
        if($username == "guest" && $cipher_text == "hQDYoS65GjgMhWIlyamyfQ=="){
          setcookie("id", $username, time()+3600);
          setcookie("timeloggedin", time(), time()+3600);
          showSubmit();
        }else{ ?>
          <p style="text-align:center;">Bad authentication</div>
          <p style="text-align:center;"><a href="dinner.php"> Back to the mainpage </a></p>
          <?php
        }
      }
    }else{
      showLogin();
    }
  }else{
    if($_SERVER['REQUEST_METHOD'] === 'POST'){ //Insert in db
      if(isset($_POST["username"])){
        $username = $_POST["username"];
        $items = $_POST["items"];
        $host = "summer-2018.cs.utexas.edu";
        $user = "tct537";
        $pwd = "Cancer&Cab!merge";
        $dbs = "cs329e_tct537";
        $port = "3306";
        $connect = mysqli_connect ($host, $user, $pwd, $dbs, $port);
        if (empty($connect))
        {
          die("mysqli_connect failed: " . mysqli_connect_error());
        }
        //print "Connected to ". mysqli_get_host_info($connect) . "<br /><br />\n";
        $table = "final";
        if($username != "" && $items != ""){
          $stmt = mysqli_prepare ($connect, "INSERT INTO $table VALUES (?, ?)");
          mysqli_stmt_bind_param ($stmt, 'ss', $username, $items);
          mysqli_stmt_execute($stmt);
          mysqli_stmt_close($stmt);
        }
        echo "<h1>Thank you!</h1>";
        ?>
        <p style="text-align: center;"><a href="dinner.php"> Back to the mainpage </a></p>
        <?php
      }
    }else{
      showSubmit();
    }
  }
}
function showSubmit(){
  ?>
  <form method="post">
    <table class="main_table">
      <tr>
        <td>
          Name:
        </td>
        <td>
          Items:
        </td>
      </tr>
      <tr>
        <td>
          <input type="text" id="username" name="username" maxlength="20" onkeyup="checkItems()" />
        </td>
        <td>
          <input type="text" id="items" name="items" maxlength="100" onkeyup="checkItems()" />
        </td>
      </tr>
      <tr>
        <td>
          <input type="submit" id="submit" name="submit" disabled="true" />
        </td>
        <td>
          <input type="reset" name="reset" />
        </td>
      </tr>
      <?php
        $username = $_POST["username"];
        $items = $_POST["items"];
        $host = "summer-2018.cs.utexas.edu";
        $user = "tct537";
        $pwd = "Cancer&Cab!merge";
        $dbs = "cs329e_tct537";
        $port = "3306";
        $connect = mysqli_connect ($host, $user, $pwd, $dbs, $port);
        if (empty($connect))
        {
          die("mysqli_connect failed: " . mysqli_connect_error());
        }
        //print "Connected to ". mysqli_get_host_info($connect) . "<br /><br />\n";
        $table = "final";
        $result = mysqli_query($connect, "SELECT * from $table");
        while($row = $result->fetch_row()){
          ?>
          <tr>
            <td>
              <?php echo $row[0]; ?>
            </td>
            <td>
              <?php echo $row[1]; ?>
            </td>
          </tr>
          <?php
        }
        $result->free();
      ?>
    </table>
  </form>
  <?php
}
function showLogin(){
  ?>
  <form method="post">
    <table style="margin: auto; background-color: lightgrey;">
      <tr>
        <td>
          Name:
        </td>
        <td>
          <input type="text" id="username" name="username" />
        </td>
      </tr>
      <tr>
        <td>
          Password:
        </td>
        <td>
          <input type="password" id="password" name="password" />
        </td>
      </tr>
      <tr>
        <td>
          <input type="submit" name="submit" />
        </td>
        <td>
          <input type="reset" name="reset" />
        </td>
      </tr>
    </table>
  </form>
  <?php
}
?>

<body class="main_body">
  <h1>Potluck Dinner</h1>
  <?php start(); ?>
</body>
</html>