<!DOCTYPE html>

<?php
function start() {
  showTable();
}
function showTable() {
  $servername = "summer-2018.cs.utexas.edu";
  $username = "tct537";
  $password = "Cancer&Cab!merge";
  $dbname = "cs329e_tct537";
  $port = "3306";
  $connect = mysqli_connect ($servername, $username, $password, $dbname);
  if (empty($connect))
  {
    die("mysqli_connect failed: " . mysqli_connect_error());
  }
  print "Connected to ". mysqli_get_host_info($connect) . "<br /><br />\n";
  ?>
  <table>
    <tr>
      <th>
        ID
      </th>
      <th>
        Last
      </th>
      <th>
        First
      </th>
      <th>
        Major
      </th>
      <th>
        GPA
      </th>
    </tr>
  <?php
  //Get data from table
  $table = "STUDENTS";
  $result = mysqli_query($connect, "SELECT * FROM $table ORDER BY LAST ASC, FIRST ASC");
  while($row = $result->fetch_row()){
    ?>
    <tr>
      <td>
        <?php echo $row[0]; ?>
      </td>
      <td>
        <?php echo $row[1]; ?>
      </td>
      <td>
        <?php echo $row[2]; ?>
      </td>
      <td>
        <?php echo $row[3]; ?>
      </td>
      <td>
        <?php echo $row[4]; ?>
      </td>
    </tr>
    <?php
  }
  $result->free();
  ?>
  </table>
  <?php
  mysqli_close($connect);
  ?><a href="index.php"> Back to the homepage </a><?php
}
?>


<html>
<head>
<title> VIEW TABLE </title>
</head>
<body>
<h3> VIEW TABLE </h3>
<?php start(); ?>

</body>
</html>