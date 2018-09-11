<?php
  $username = $_GET["username"];
  $file = fopen("passwd", "r");
  $userlist = Array();
  while(!feof($file)){
    $line = fgets($file);
    $line_pieces = explode(":", $line);
    $userlist[$line_pieces[0]] = $line_pieces[1];
  }
  fclose($file);
  if(array_key_exists($username, $userlist)){
    $response = "true";
    echo $response;
  }else{
    $response = "false";
    echo $response;
  }
?>