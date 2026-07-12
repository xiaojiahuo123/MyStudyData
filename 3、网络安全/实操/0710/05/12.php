<?php
error_reporting(0);
if (isset($_GET['file'])) {
    if (!strpos($_GET["file"], "flag")) {
        include $_GET["file"];
    } else {
        echo "No No No!!!";
    }
} else {
    highlight_file(__FILE__);
}
