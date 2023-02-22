<?php
$name = "Nikita";
$profession = "Data scientist";
$city = "Moscow";
$email = "egdxgjyt1@ya.ru";
$phone = "+79562344576";
$skills = [
	[
    	"name" => "python",
        "percent" => 60,
    ],
    [
    	"name" => "sql",
        "percent" => 70,
    ],
    [
    	"name" => "java_script",
        "percent" => 50,
    ],
    ];
$language = [
	[
    	"name" => "English",
        "percent" => 90,
    ],
    [
    	"name" => "Japanese",
        "percent" => 60,
    ],
    [
    	"name" => "China",
        "percent" => 70,
    ],
    ];
$jobs = [
	[
    	"position" => "Data scientist \ yandex.ru",
        "start" => "29 Jan 2023",
        "end" => "Current",
        "description" => "Глажу котиков и получаю денежку",
    ],
    [
    	"position" => "Python Developer",
        "start" => "17 Jul 2021",
        "end" => "9 Jan 2023",
        "description" => "梨の花
						月に踏み読む
						女あり",	
    ],
    [
    	"position" => "Web Developer",
        "start" => "25 Feb 2020",
        "end" => "23 May 2021",
        "description" => "sergsergh",
    ],
];
$education = [
	[
    	"name" => "gb.ru",
        "data" => "Forever",
        "about" => "Data scientist",
    ],
    [
    	"name" => "London Business School",
        "data" => "2018-2020",
        "about" => "Master Degree",
    ],
    [
    	"name" => "School of Coding",
        "data" => "2014-2018",
        "about" => "Bachelor Degree",
    ],
    ];
    
?>
<!DOCTYPE html>
<html>
<head>
  <title>Мое резюме</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Jost:wght@300&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <style>
    html,
    body,
    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
      font-family: 'Jost', sans-serif;
    }
  </style>
</head>
<body class="w3-light-grey">
  <!-- Page Container -->
  <div class="w3-content w3-margin-top" style="max-width:1400px;">
    <!-- The Grid -->
    <div class="w3-row-padding">
      <!-- Left Column -->
      <div class="w3-third">
        <div class="w3-white w3-text-grey w3-card-4">
          <div class="w3-display-container">
            <img src="https://imgfon.ru/Images/Details_img_880px/Animals/glaza-belyy_fon-kotik-morda-polosatyy.webp"
              style="width:100%" alt="Avatar">
            <div class="w3-display-bottomleft w3-container w3-text-black">
              <h2><?php echo $name; ?> </h2>
            </div>
          </div>
          <div class="w3-container">
            <p><i class="fa fa-briefcase fa-fw w3-margin-right w3-large w3-text-teal"></i><?= $profession; ?></p>
            <p><i class="fa fa-home fa-fw w3-margin-right w3-large w3-text-teal"></i><?= $city; ?></p>
            <p><i class="fa fa-envelope fa-fw w3-margin-right w3-large w3-text-teal"></i><?= $email; ?></p>
            <p><i class="fa fa-phone fa-fw w3-margin-right w3-large w3-text-teal"></i><?= $phone; ?></p>
 
            <hr>
 
            <p class="w3-large"><b><i class="fa fa-asterisk fa-fw w3-margin-right w3-text-teal"></i>Навыки</b></p>
            <?php for ($i = 0; $i < count($skills); $i++): ?>
            	<p><?php echo $skills[$i]["name"]; ?></p>
            	<div class="w3-light-grey w3-round-xlarge w3-small">
              	<div class="w3-container w3-center w3-round-xlarge w3-teal" style="width:<?php echo $skills[$i]["percent"];?>%"><?php echo $skills[$i]["percent"];?> %</div>
            	</div>
            <?php endfor; ?>
            <br>
 
            <p class="w3-large w3-text-theme"><b><i class="fa fa-globe fa-fw w3-margin-right w3-text-teal"></i>Языки</b>
            </p>
            <?php for ($i = 0; $i < count($skills); $i++): ?>
            <p><?= $language[$i]["name"];?> </p>
            <div class="w3-light-grey w3-round-xlarge">
              <div class="w3-round-xlarge w3-teal" style="height:24px;width:<?= $language[$i]["percent"];?>%"></div>
            </div>
            <?php endfor; ?>
            </div>
            <br>
          </div>
        <br>
        <!-- End Left Column -->
      </div>
      <!-- Right Column -->
      <div class="w3-twothird">
        <div class="w3-container w3-card w3-white w3-margin-bottom">
          <h2 class="w3-text-grey w3-padding-16"><i
              class="fa fa-suitcase fa-fw w3-margin-right w3-xxlarge w3-text-teal"></i>Опыт работы</h2>
          <div class="w3-container">
          <?php for ($i = 0; $i < count($jobs); $i++): ?>
            <h5 class="w3-opacity"><b><?= $jobs[$i]["position"];?> </b></h5>
            <h6 class="w3-text-teal"><i class="fa fa-calendar fa-fw w3-margin-right"></i><?= $jobs[$i]["start"];?> - <?php if($jobs[$i]["end"] == $jobs[0]["end"]) { 
            echo '<span class="w3-tag w3-teal w3-round">Current</span>';} 
            else {
            	echo '<i class="fa w3-round-xlarge"></i>', $jobs[$i]["end"];}?></h6>
            <p><?= $jobs[$i]["description"];?></p>
            <?php endfor;?>
            <div class="w3-container">
        </div>
            </div>
          </div>
 
        <div class="w3-container w3-card w3-white">
          <h2 class="w3-text-grey w3-padding-16"><i
              class="fa fa-certificate fa-fw w3-margin-right w3-xxlarge w3-text-teal"></i>Образование</h2>
          <div class="w3-container">
          <?php for ($i = 0; $i < count($jobs); $i++): ?>
            <h5 class="w3-opacity"><b><?= $education[$i]["name"];?></b></h5>
            <h6 class="w3-text-teal"><i class="fa fa-calendar fa-fw w3-margin-right"></i><?= $education[$i]["data"];?></h6>
            <p><?= $education[$i]["about"];?></p>
            <?php endfor;?>
          </div>
          <div class="w3-container">
            </div>
          </div>
   
        <!-- End Right Column -->
      </div>
      <!-- End Grid -->
    </div>
    <!-- End Page Container -->
  </div>
  <!-- Footer -->
  <footer class="w3-container w3-teal w3-center w3-margin-top">
    <p>Find me on social media.</p>
    <i class="fa fa-pinterest-p w3-hover-opacity"></i>
    <i class="fa fa-twitter w3-hover-opacity"></i>
    <i class="fa fa-linkedin w3-hover-opacity"></i>
    <!-- End footer -->
  </footer>
</body>
</html>