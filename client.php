<?php


    $fp = stream_socket_client("tcp://127.0.0.1:11060", $errno, $errstr, 30);
    fwrite($fp, "bu test için bir yazıydı...");
    echo "Success";

    if (!$fp) {
        echo "ERROR: $errno - $errstr<br />\n";
    } 
?>