//Creating animations
var serial;          // variable to hold an instance of the serialport library
var portName = '/dev/tty.usbserial-1450';  // fill in your serial port name here
var inData;
//animations like p5 images should be stored in variables
//in order to be displayed during the draw cycle
var ghost;
var defaultDog;

//it's advisable (but not necessary) to load the images in the preload function
//of your sketch otherwise they may appear with a little delay
function preload() {

  ghost = loadAnimation('push_5.png', 'push_6.png','push_7.png','push_8.png');
  defaultDog = loadAnimation('de1.png','de2.png','de3.png','de4.png');
}

function setup() {
  createCanvas(1500, 800);
  ghost.frameDelay = 12;
  defaultDog.frameDelay = 12;
  
  
  serial = new p5.SerialPort();       // make a new instance of the serialport library
 
  serial.on('connected', serverConnected); // callback for connecting to the server
  serial.on('open', portOpen);        // callback for the port opening
  serial.on('data', serialEvent);     // callback for when new data arrives
  serial.on('error', serialError);    // callback for errors
  serial.on('close', portClose);      // callback for the port closing
 
  serial.list();                      // list the serial ports
  serial.open(portName); 
}

function serverConnected() {
  console.log('connected to server.');
}
 
function portOpen() {
  console.log('the serial port opened.')
}
 
function serialEvent() {
  inData = Number(serial.read());
 
}
 
function serialError(err) {
  console.log('Something went wrong with the serial port. ' + err);
}
 
function portClose() {
  console.log('The serial port closed.');
}

function draw() {
  background(245, 224, 64);
  
  if (inData >= 212) {    
  animation(ghost, 800, 350);
  } else{
    animation(defaultDog, 800, 350);
    
  
}
}
