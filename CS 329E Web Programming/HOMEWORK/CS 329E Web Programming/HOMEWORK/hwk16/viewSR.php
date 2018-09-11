<!DOCTYPE html>

<?php
function start() {
  showTable();
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
  $table = "STUDENTS";
  // $result = mysqli_query($connect, "SELECT * from $table");
  // while ($row = $result->fetch_row())
  // {
  //   print "Last = " . $row[0] . " FirstName = " . $row[1].
  // 	" Major = " . $row[2] . " Birthday = " . $row[3] . "<br /><br />\n";
  // }
  //
  // $result->free();
  $id = $_POST["ID"];
  $last = $_POST["LAST"];
  $first = $_POST["FIRST"];
  if ($id != "") {
    $result = mysqli_query($connect, "SELECT * from $table WHERE ID = $id");
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
  } else {
      if ($last != "" && $first == "") {
        $result = mysqli_query($connect, "SELECT * from $table WHERE LAST = \"$last\"");
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
      }
      if ($last != "" && $first != "") {
        $result = mysqli_query($connect, "SELECT * from $table WHERE LAST = \"$last\" AND FIRST = \"$first\"");
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
      }
      if ($last == "" && $first != "") {
          $result = mysqli_query($connect, "SELECT * from $table WHERE FIRST = \"$first\"");
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
      }
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

  <tr><td><input type="submit" name="submit" value="Retrieve"/></td>
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
<title> Retrieve from TABLE </title>
</head>
<body>
<h3> Retrieve from TABLE </h3>
<?php start(); ?>
<a href="viewAllSR.php">View All Student Record</a><br />
</body>
</html>