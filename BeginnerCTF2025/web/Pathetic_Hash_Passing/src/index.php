<?php
$content = <<<HTML
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pathetic Hash Passing</title>
    </head>
    <body>
        <h1>HashBot</h1>
        <p>Hiya, I'm hashbot and the MD5 hash of my favorite string is 0e565476994437051230891734799446</p>
    
        <p id="result">
            <!-- HASH_PLACEHOLDER -->
        </p>
        <form id="hashForm" method="GET" action="">
            <label for="input">Enter your favorite string:</label>
            <input type="text" id="input" name="hash" required>
            <button type="submit">Check hash</button>
        </form>
    </body>
</html>
HTML;

if (isset($_GET['hash'])) {
    $hash = md5($_GET['hash']);
    $result;
    if ($hash === false) {
        echo "Error generating hash.";
        exit;
    }

    if ($hash == "0e565476994437051230891734799446") { 
        $result = "Thats my favorite string as well, given we're basicly the same person now you can have my flag"
            . " <br> Flag:<b>"
            . getenv('FLAG')
            ."</b>";
    } else{
        $result = "So your favorite string's hash is: <b>" . $hash . "</b> <br> But it is not my favorite string, so you get nothing.";
    }

    $content = str_replace('<!-- HASH_PLACEHOLDER -->', $result, $content);
} 

echo $content;
?>
