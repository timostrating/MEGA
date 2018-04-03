<?php 

$ch = curl_init ("https://www.hanze.nl/assets/instituut-voor-communicatie-media-it/Documents/Hanze-PL-ST/Tentamenrooster/2017-2018%20P3%20wk%207-16%20Tentamens-Exams.xlsx");
curl_setopt ($ch, CURLOPT_COOKIEFILE, "cookie.txt");
curl_setopt ($ch, CURLOPT_RETURNTRANSFER, true);
$output = curl_exec ($ch);

echo $output;