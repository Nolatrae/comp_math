<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="./style.css" />
  <title>Document</title>
</head>
<body>
  <table class='multyTable'>
    <?php
    for($i = 0; $i < 10; $i++) {
      echo "<tr>";
      for($j = 0; $j < 10; $j++) {
        if ($i == 0){
          if ($j == 0) {
            echo "<td class='cell top left'>"$j"</td>";
            continue;
          }
          echo "<td class='cell top'>"$j"</td>";
          continue;
        }
        if ($j == 0){
          echo "<td class='cell left'>"$j"</td>";
          continue;
        }
        if($j == $i){
          echo "<td class='cell diagonal'>"$j * $i"</td>";
          continue;
        }
        echo "<td class='cell'>"$j * $i"</td>";
        continue;
    }
    echo "</tr>";
  }
    ?>
  </table>
</body>
</html>