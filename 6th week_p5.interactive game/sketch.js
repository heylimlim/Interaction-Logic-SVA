var img1;
var img2;

var imgchoice;

function preload() {
  bg = loadImage("tree3.png");
  img1 = loadImage("bird1.png");
  img2 = loadImage("bird2.png");
  img3 = loadImage("bird3.png");
  img4 = loadImage("berry1.png");
  img5 = loadImage("berry2.png");
  img6 = loadImage("berry3.png");
  imgchoice = int (random(0,5));
}

function setup() {
  createCanvas(800, 800);
  strokeWeight(0)
  background(235);
  
  background(800);
  image(bg, width/2 - 300, height/2 - 300, 600, 600);
  
}

function mouseDragged() {
  
  if (mouseX<=130 && mouseY<=90) {
  return;
  }
  
    else if (imgchoice == 0){
    image(img1, mouseX - 25, mouseY - 25, 40, 42);
  } else if (imgchoice ==1){
    image(img2, mouseX - 25, mouseY - 25, 35, 40);
  } else if (imgchoice ==2){
    image(img3, mouseX - 25, mouseY - 25, 80, 40);
  } else if (imgchoice ==3){
    image(img4, mouseX - 25, mouseY - 25, 52, 38);
  } else if (imgchoice ==4){
    image(img5, mouseX - 25, mouseY - 25, 54, 58);
  } else {
    image(img6, mouseX - 25, mouseY - 25, 83, 40);
  }
}

function mouseClicked() {

  if (mouseX>=20 && mouseX<=62 && mouseY>=0 && mouseY<=75) {
  imgchoice = 0;
  }
  else if (mouseX>=62 && mouseX<=100 && mouseY>=0 && mouseY<=75) {
  imgchoice = 1;
  }
  else if (mouseX>=100 && mouseX<=200 && mouseY>=0 && mouseY<=75) {
  imgchoice = 2;
  }
  else if (mouseX>=200 && mouseX<=300 && mouseY>=0 && mouseY<=75) {
  imgchoice = 3;
  }
  else if (mouseX>=300 && mouseX<=350 && mouseY>=0 && mouseY<=75) {
  imgchoice = 4;
  }
  else if (mouseX>=350 && mouseX<=500 && mouseY>=0 && mouseY<=75) {
  imgchoice = 5;
  }
  
    else if (imgchoice == 0){
    image(img1, mouseX - 25, mouseY - 25, 42, 40);
  } else if (imgchoice ==1){
    image(img2, mouseX - 25, mouseY - 25, 35, 40);
  } else if (imgchoice ==2){
    image(img3, mouseX - 25, mouseY - 25, 80, 40);
  } else if (imgchoice ==3){
    image(img4, mouseX - 25, mouseY - 25, 52, 38);
  } else if (imgchoice ==4){
    image(img5, mouseX - 25, mouseY - 25, 54, 58);
  } else {
    image(img6, mouseX - 25, mouseY - 25, 83, 40);
  }
  
}


function draw() {

  fill(240,240,240);
  rect(0,0,1000,75);
  image(img1, 20,15,42,40);
  image(img2, 80,15,35,40);
  image(img3, 135,19,80,40);
  image(img4, 220,19,52,38);
  image(img5, 300,5,54,58);
  image(img6, 380,15,83,40);
  
}