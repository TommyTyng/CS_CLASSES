<?php
/**
 * Created by PhpStorm.
 * User: tommytyng
 * Date: 8/13/18
 * Time: 12:18 PM
 */

writeAndDisplayResults();


function writeAndDisplayResults()
{
    if ($_SESSION["uniqueID"] = "true") {
        $username = $_POST['userName'];
        $password = $_POST["password"];
        $file = fopen("./passwd.txt", "a");
        fwrite($file, ($username . ":" . crypt($password) . "\n"));
        fclose($file);

        session_unset();     // unset $_SESSION variable for the run-time
        session_destroy();
        //header('Location: https://spring-2018.cs.utexas.edu/cs329e-mitra/aqluna/hwk17/ajaxLogin.html');
print "<h1><p>Thank you for registering.</p></h1>
               <a href=\"ajaxLogin.html\">Go Back to Registration</a>";
        die;
        

    }
    else {
        echo "<script type='text/javascript'>alert('Username is not unique');</script>";
    }   
    

}
