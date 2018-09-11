<?php
/**
 * Created by PhpStorm.
 * User: tommytyng
 * Date: 8/13/18
 * Time: 12:13 PM
 */
//change
//change2
checkUserName();

function checkUserName()
{
    $username = $_POST["username"];
    //echo "<script> alert ($username)</script>";

    //$userNameFound = "";
    $existingUser = "false";

    if ($file = fopen("./passwd.txt", "r")) {
        while ((!feof($file)) && ($existingUser == "false")) {
            $newLine = trim(fgets($file));
            list($readUsername, $readPassword) = explode(":", $newLine);
            //echo "<script> alert ('read username $readUsername[0]')</script>";
            if ($readUsername == $username) {
                //$userNameFound = "true";
                $existingUser = "true";
            }
        }
    }
    fclose($file);
    if ($existingUser == "true") {
        echo "TRUE";
        die;
    } else
    {
        $_SESSION["uniqueID"] = true;
//        $response = "false";
//        echo $response;
        echo "FALSE";
        die;
    }


}
//        echo "<script> alert ('There was an issue with login form, please try again')</script>";
//        echo "<script> location.href='https://spring-2018.cs.utexas.edu/cs329e-mitra/aqluna/hwk17/ajaxLogin.php'</script>";
//        exit;
                           