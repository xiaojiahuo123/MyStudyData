<?php
error_reporting(0);
function filter($name)
{
    $safe = array(
        "flag",
        "php"
    );
    $name = str_replace($safe, "hack", $name);
    echo $name;
    return $name;
}
class test
{
    var $user;
    var $pass = 'daydream';
    function __construct($user)
    {
        $this->user = $user;
    }
}
echo serialize(new test());
filter("");
