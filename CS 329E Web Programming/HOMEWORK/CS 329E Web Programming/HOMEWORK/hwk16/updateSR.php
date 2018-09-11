<!DOCTYPE html>

<?php
function start() {
  showTable();
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
  print "Connected to ". mysqli_get_host_info($connect) . "<br /><br />\n";
  $table = "STUDENTS";
  // $result = mysqli_query($connect, "SELECT * from $table");
  // while ($row = $result->fetch_row())
  // {
  //   print "ID = " . $row[0] . " LastName = " . $row[1].
  //   " First = " . $row[2] . " Major = " . $row[3] . "<br /><br />\n";
  // }
  //
  // $result->free();
  $id = $_POST["ID"];
  $last = $_POST["LAST"];
  $first = $_POST["FIRST"];
  $major = $_POST["MAJOR"];
  $gpa = $_POST["GPA"];
  if (($id != "") && ($last != "" || $first != "" || $major != "" || $gpa != "")) {
    //
    // $sql = "UPDATE $table SET last=?, first=?, major=?, gpa=? WHERE id= $id";
    //
    // $stmt = $db_usag->prepare($sql);
    //
    // $stmt->bind_param('ssssi', $last, $first, $major, $gpa);
    // $stmt->execute();
    if ($last != "") {
      $stmt = mysqli_prepare ($connect, "UPDATE $table SET LAST=? WHERE id= $id");
      mysqli_stmt_bind_param ($stmt, 's', $last);
      mysqli_stmt_execute($stmt);
      mysqli_stmt_close($stmt);
      echo("updated\n\n");
    }
    if ($first != "") {
      $stmt = mysqli_prepare ($connect, "UPDATE $table SET FIRST=? WHERE id= $id");
      mysqli_stmt_bind_param ($stmt, 's', $first);
      mysqli_stmt_execute($stmt);
      mysqli_stmt_close($stmt);
      echo("updated\n\n");
    }
    if ($major != "") {
      $stmt = mysqli_prepare ($connect, "UPDATE $table SET MAJOR=? WHERE id= $id");
      mysqli_stmt_bind_param ($stmt, 's', $major);
      mysqli_stmt_execute($stmt);
      mysqli_stmt_close($stmt);
      echo("updated\n\n");
    }
    if ($gpa != "") {
      $stmt = mysqli_prepare ($connect, "UPDATE $table SET GPA=? WHERE id= $id");
      mysqli_stmt_bind_param ($stmt, 'd', $gpa);
      mysqli_stmt_execute($stmt);
      mysqli_stmt_close($stmt);
      echo("updated\n\n");
    }
    // $result = mysqli_query($connect, "SELECT * from $table");
    // while ($row = $result->fetch_row())
    // {
    //   print "ID = " . $row[0] . " LastName = " . $row[1].
    // 	" First = " . $row[2] . " Major = " . $row[3] . "<br /><br />\n";
    // }
    //
    // $result->free();
    ?><a href="index.php"> Back to the homepage </a><?php
  } else {
    echo("empty field(s)");
  }
}
function showTable() {?>
  <form method="post">
  <table border="0">
  <tr><td>ID</td>
  <td><input type="text" name="ID" /></td>
  </tr>
  <tr><td>LAST</td>
  <td><input type="text" name="LAST" /></td>
  </tr>
  <tr><td>FIRST</td>
  <td><input type="text" name="FIRST" /></td>
  </tr>

  <tr><td>MAJOR</td>
  <td><input type="text" name="MAJOR" /></td>
  </tr>
  <tr><td>GPA</td>
  <td><input type="text" name="GPA" /></td>
  </tr>
  <tr><td><input type="submit" name="submit" value="Submit"/></td>
  <td><input type="reset" name="reset" value="Reset" /></td>
  </tr>
  </table>
  </form>
<?php
}
// Close connection to the database
mysqli_close($connect);
?>


<html>
<head>
<title> UPDATE TABLE </title>
</head>
<body>
<h3> UPDATE TABLE </h3>
<?php start(); ?>

</body>
</html>