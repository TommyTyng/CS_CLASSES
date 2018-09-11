<?php

$names = array();

$file = fopen('signup.txt', 'r');
  while(!feof($file)) {
    $line = trim(fgets($file));
    if(!empty($line)) {
      list($time, $name) = explode(',', $line);
      $names[$time] = $name;
    }
  }
        fclose($file);

if ($_SERVER["REQUEST_METHOD"] == "POST") {
                $count = 0;
                foreach ($_POST as $time => $name) {
                        if (!(empty($name)) && $time != "submit") {
                                $count++;
                                $newName = $name;
                                list($num, $ampm) = explode("_",$time);
                                $newTime = "$num $ampm";
                        }
                }
                if ($count != 1) {
                        echo "<script type='text/javascript'>alert('Please sign up for one slot');</script>";
                } elseif (!(empty($names[$newTime]))) {
                        echo "<script type='text/javascript'>alert('Sorry! That slot has been taken.');</script>";
                } else {
                        updatedPage($names, $newTime, $newName);
                }
        }

        $file = fopen('signup.txt', 'r');
  while(!feof($file)) {
    $line = trim(fgets($file));
    if(!empty($line)) {
      list($time, $name) = explode(',', $line);
      $names[$time] = $name;
    }
  }
        fclose($file);
        signup($names);

function signup($names)
  {
    $script = $_SERVER['PHP_SELF'];
    print <<<PAGE1_TOP
    
    <html>
    <head>
        <title> Sign-Up Sheet </title>
        <link rel = "stylesheet" title = "basic style" type = "text/css" href = "./signup.css"/>
        <link href="https://fonts.googleapis.com/css?family=IBM+Plex+Mono" rel="stylesheet">
    </head>
    <body>
        <br>
        <form id="return">
            <input type="submit" formaction="../index.html" value="Back to Index" class="button"/>
        </form>
        <br>
        <h1>Sign-Up Sheet</h1>
        <form action="$script" method="post">
            <table border="1px">
                <tr>
                    <th> Time </th><th> Name </th>
                </tr>

PAGE1_TOP;

                foreach ($names as $key => $value) {
                        if (empty($value)) {
                                print "<tr><td class='time'>$key</td><td><input type='text' name='$key'/></td></tr>";
                        } else {
                                print "<tr><td class='time'>$key</td><td>$value</td></tr>";
                        }
                }
                print <<<PAGE1_BOTTOM

<tr>
                    <td width="150"> 8:00 am </td><td> <input type="textbox" size="25" id="8" name="8"> </td>
                </tr>
                <tr>
                    <td width="150"> 9:00 am </td><td> <input type="textbox" size="25" id="9" name="9"> </td>
                </tr>
                <tr>
                    <td width="150"> 10:00 am</td><td> <input type="textbox" size="25" id="10" name="10"></td>
                </tr>
                <tr>
                    <td width="150"> 11:00 am</td><td> <input type="textbox" size="25" id="11" name="11"></td>
                </tr>
                <tr>
                    <td width="150"> 12:00 pm</td><td> <input type="textbox" size="25" id="12" name="name12"></td>
                </tr>
                <tr>
                    <td width="150"> 1:00 pm </td><td> <input type="textbox" size="25" id="1" name="1"> </td>
                </tr>
                <tr>
                    <td width="150"> 2:00 pm </td><td> <input type="textbox" size="25" id="2" name="2"> </td>
                </tr>
                <tr>
                    <td width="150"> 3:00 pm </td><td> <input type="textbox" size="25" id="3" name="3"> </td>
                </tr>
                <tr>
                    <td width="150"> 4:00 pm </td><td> <input type="textbox" size="25" id="4" name="4"> </td>
                </tr>
                <tr>
                    <td width="150"> 5:00 pm </td><td> <input type="textbox" size="25" id="5" name="5"> </td>
                </tr>
                <tr>
                    <td width="100"> <input type="submit" value="Submit"> </td><td width="100"> <input type="reset" value="Reset"></td>
                </tr>
            </table>
        </form>
    </body>
</html>

PAGE1_BOTTOM;
  }

  function updatedPage($names, $newTime, $newName) {
                $file = fopen('signup.txt', 'w');
                foreach ($names as $time => $name) {
                        if (substr($newTime,0,2) == substr($time,0,2)) {
                                $name = $newName;
                        }
                        $newLine = $time.",".$name."\n";
                        fwrite($file,$newLine);
                }
                fclose($file);
        }
