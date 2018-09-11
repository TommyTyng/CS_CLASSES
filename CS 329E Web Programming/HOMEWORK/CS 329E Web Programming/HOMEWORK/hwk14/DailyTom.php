<?php

if (isset($_COOKIE["loggedIn"]) && !isset($_POST["logOut"]))
        {
                successfulLogIn();
        }
        else if (isset($_POST["logOut"]))
        {
                setcookie("loggedIn", "hello", time() - 3600 * 24 * 365);
                logOut();
        }
        else if (isset($_POST["log-in"]) && !isset($_COOKIE["loggedIn"]))
        {
                logIn();
        }
        else if (isset($_POST["register"]) && !isset($_COOKIE["loggedIn"]))
        {
                createAccount();
        }
        else
        {
                welcome();
        }
        function successfulLogIn()
        {
                print <<<GREETINGS
               <!DOCTYPE html>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name = "author" content = "Tommy Tyng" />
<meta name = "description" content = "The Daily Tom" />
<link rel="stylesheet" href="mainpage.css">
<html>
<body>
        <form>
                <input type="submit" formaction="../index.html" value="Back to Index" class="button" id="return"/>
        </form>
        <div class = "header">
            <h1> The Daily Tom</h1>
            <script> document.write(new Date().toDateString()); </script>
            - Austin, TX
        </div>

        <div class="navBar">
            <a href="./NATMITT.html">National</a> | <a href="./jap.html">International</a> <a href="./bird.html">Business</a> | <a href="./FIFA.html">Sports</a> | <a href="./DP2.html">Arts &amp; Leisure</a>  <a 
        </div>

        

            
    </body>
</html>
GREETINGS;
        }

        function welcome()
        {
                print <<<HELLO
                <!DOCTYPE html>
                <html lang = "en">
                <head>
                        <meta charset = "UTF-8">
                        <title> Bae's Times </title>
                        <link rel = "stylesheet" title = "Basic Style" type = "text/css" href = "./mainpage.css" media = "all" />
                </head>
                <body>
                        <h1 id = "first"> <em> Bae's Times </em> </h1>
                        <ul>
                                <li> <a href = "./logIn.html"> Mitt Romney</a> </li>
                                <li> <a href = "./logIn.html"> DeadPool 2</a> </li>
                                <li> <a href = "./logIn.html"> Fifa Kickoff</a> </li>
                                <li> <a href = "./logIn.html"> eJapan Satelit</a> </li>
                                <li> <a href = "./logIn.html"> Birds!</a> </li>
                        </ul>
                </body>
                </html>
HELLO;
        }
        function logOut()
        {
                print('You have logged out successfully. <a href = "./DailyTom.php"> Log-out </a>');
        }

        function logIn()
        {
                $username = trim($_POST["username"]);
                $password = trim($_POST["password"]);
                $matched = FALSE;
                $file = fopen("./passwd.txt", "r");
                $accounts = array();
                while (!feof($file))
                {
                        $line = fgets($file);
                        if (strlen($line) > 0)
                        {
                                $elements = explode(":", $line);
                                $accounts[$elements[0]] = $elements[1];
 }
                        if ($elements[0] == $username && trim($elements[1]) == $password)
                        {
                                $matched = TRUE;
                                break;
                        }
                }
                if ($matched)
                {
                        print('Log-in successful. <a href = "./DailyTom.php"> Have fun! </a>');
                        setcookie("loggedIn", $username, time() + 120);
                }
                else
                {
                        print("$matched");
                        print('Incorrect username or password..... <a href = "./logIn.html"> Log-In </a>');
                }
                fclose($file);
        }

        function createAccount()
        {
                $username = trim($_POST["username"]);
                $password = trim($_POST["password"]);
                $rePassword = trim($_POST["rePassword"]);
                $existUsername = FALSE;
                if ($password != $rePassword)
                {
                        print('Passwords aint addup <a href = "./register.html"> Register </a>');
                }
                else if ($username == "" || $password == "")
                {
                        print('Not a username or password.  <a href = "./register.html"> Register Again </a>');

 }
                else
                {
                        $file = fopen("./passwd.txt", "a+");
                        while (!feof($file))
                        {
                                $line = fgets($file);
                                if (strlen($line) > 0)
                                {
                                        $elements = explode(":", $line);
                                        $accounts[$elements[0]] = $elements[1];
                                }
                                if ($elements[0] == $username)
                                {
                                        $existUsername = TRUE;
                                        break;
                                }
                        }
                        if ($existUsername)
                        {
                                print('Username already exists sucka! Be more clever. <a href = "./register.html"> Create Username </a>');
                        }
                        else
                        {
                                fwrite($file, "$username:$password\n");
                                print('Registration successful! <a href = "./DailyTom.php"> Wohoo! </a>');
                                setcookie("loggedIn", $username, time() + 120);
                        }
                        fclose($file);
                }
        }
?>
                                                      
  