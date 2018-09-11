<?php
  $myDict = array();
  $username = $_GET["username"];

  $fh = fopen ("passwd.txt", "r");
  while (!feof($fh)) {
   $line = fgets($fh);
   $line = rtrim($line);
   $altLine = explode(":", $line);
   $myDict[$altLine[0]] = $altLine[1];

}  fclose($fh);

  if (array_key_exists($username, $myDict)){
    $response = "1";
  }else {
    $response = "0";

  }

  echo($response);

?>
