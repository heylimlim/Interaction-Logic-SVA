import processing.serial.*;
Serial myPort;
PImage img0;
PImage img1;
PImage img2;
PImage img3;
PImage img4;
PImage img5;
float bb;void setup()
 {
 fullScreen();
 background(0,0,0);
 img0 = loadImage(“smile0.png”);
 img1 = loadImage(“smile1.png”);
 img2 = loadImage(“smile2.png”);
 img3 = loadImage(“smile3.png”);
 img4 = loadImage(“smile4.png”);
 img5 = loadImage(“smile5.png”);
 myPort = new Serial(this, “/dev/cu.usbserial-1450”, 9600);
 myPort.bufferUntil( ‘\n’);
}void serialEvent (Serial myPort) {
bb = float(myPort.readStringUntil( ‘\n’));
}void draw()
 {
 println(bb);
 if (bb >= 834) {
 imageMode(CENTER);
 image(img5,displayWidth/2,displayHeight/2,1020,1020);
 } else if (bb >= 668 && bb < 834){
   imageMode(CENTER);
   image(img4,displayWidth/2,displayHeight/2,1020,1020);
 } else if (bb >= 502 && bb < 668){
   imageMode(CENTER);
   image(img3,displayWidth/2,displayHeight/2,1020,1020);
 } else if (bb >= 336 && bb < 502){
   imageMode(CENTER);
   image(img2,displayWidth/2,displayHeight/2,1020,1020);
 } else if (bb >= 170 && bb < 336){
   imageMode(CENTER);
   image(img1,displayWidth/2,displayHeight/2,1020,1020);
 } else{
   imageMode(CENTER);
   image(img0,displayWidth/2,displayHeight/2,1020,1020);
 }
}