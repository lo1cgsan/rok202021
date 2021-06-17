<!DOCTYPE html>
<html lang="pl">

<head>
    <meta charset="utf-8" />
    <title>Podstawy skryptów PHP</title>
    <style>
        body {
            font-family: Arial,sans-serif;
            font-size: 16px;
        }
        h1 {
            font-size: 2rem;
        }
    </style>
</head>

<body>

GET
https://www.google.com/
search?
q=j%C4%99zyk+php&
safe=strict&
source=hp&
ei=R7fJYKZn5LryAq_YtuAE&iflsig=AINFCbYAAAAAYMnFVx1rqc9-U5nFEHw85GUJwIH9xMMy&oq=j%C4%99zyk+php&gs_lcp=Cgdnd3Mtd2l6EAMyAggAMgIIADICCAAyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoLCAAQsQMQxwEQowI6CAgAELEDEIMBOggILhCxAxCDAToCCC46CAgAEMcBEK8BOggILhCxAxCTAjoFCAAQsQM6BQguELEDOgcIABCxAxAKOgQIABAKUNkkWIs0YJtPaABwAHgAgAFpiAGxBpIBAzguMZgBAKABAaoBB2d3cy13aXo&sclient=gws-wiz&ved=0ahUKEwjmpt2G35vxAhVknVwKHS-sDUwQ4dUDCAc&
uact=5

<form method="POST">

</form>

<?php

    $a = 10;
    $b = 5;

    echo "<h1>Podstawy skryptów PHP</h1>";
    echo "<p>Jakaś treść</p>";
    echo "<p>Suma 10 i 5 to: ".($a + $b)."</p>";

?>

</body>

</html>
