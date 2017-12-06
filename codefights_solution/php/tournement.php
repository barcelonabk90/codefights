<?php

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

function chessClockSumOfDigits($initialTime, $k) {
    $a = toSec($initialTime[0]);
    $b = toSec($initialTime[1]);
    $min = sumOfDigits($a) + sumOfDigits($b);
    $max = $min;
    for ($i = 0; $i <= $k; $i++) {
        for ($j = 0; $j <= $k - $i; $j++) {
            $tmp = sumOfDigits($a - $i) + sumOfDigits($b - $j);
            $min = min($tmp, $min);
            $max = max($tmp, $max);
        }
    }
    return [$min, $max];
}

/**
 * Ex : $time = '2.59'
 * result = 2 * 60 + 59 = 179
 * @param type $time
 * @return type
 */
function toSec($time) {
    $arr = explode('.', $time);
    return $arr[0] * 60 + $arr[1];
}

/**
 * Ex : $time = 179
 * m = 3, s = 179 - 60 * 3 = 59
 * result = 3 + 5 + 9 = 17
 * @param int $time
 * @return type
 */
function sumOfDigits($time) {
    $tmp = floor($time / 60);
    $time %= 60;
    return $tmp % 10 + floor($tmp % 10) + $time % 10 + floor($time % 10);
}

/**
 * Given array of integers, find its mode.

  Example

  For sequence = [1, 3, 3, 3, 1], the output should be
  arrayMode(sequence) = 3;
  For sequence = [1, 3, 2, 1], the output should be
  arrayMode(sequence) = 1.
 * @param type $sequence
 * @return type
 */
function arrayMode($sequence) {
    $a = array_count_values($sequence);
    return array_search(max($a), $a);
}
