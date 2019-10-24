// https://kylemcdonald.github.io/cv-examples/
// hello mel

var capture;
var previousPixels;
var flow;
var w = 640,
    h = 480;
var step = 5;

var uMotionGraph, vMotionGraph;

function setup() {
    createCanvas(w, h);
    capture = createCapture({
        audio: false,
        video: {
            width: w,
            height: h
        }
    }, function() {
        console.log('capture ready.')
    });
    capture.elt.setAttribute('playsinline', '');
    capture.hide();
    //flow = new FlowCalculator(step);
    //uMotionGraph = new Graph(100, -step / 2, +step / 2);
    //vMotionGraph = new Graph(100, -step / 2, +step / 2);
}

function copyImage(src, dst) {
    var n = src.length;
    if (!dst || dst.length != n) dst = new src.constructor(n);
    while (n--) dst[n] = src[n];
    return dst;
}

function same(a1, a2, stride, n) {
    for (var i = 0; i < n; i += stride) {
        if (a1[i] != a2[i]) {
            return false;
        }
    }
    return true;
}

function draw() {
    capture.loadPixels();
    size = 16;
  
    fill(245, 245, 245);
    rect(0, 0, w, h);
  
    strokeWeight(0);
  
    for (i = 0; i < w; i += size) {
        for (j = 0; j < h; j += size) {
            baseIndex = 4 * (w * j + i);
            r = capture.pixels[baseIndex];
            g = capture.pixels[baseIndex+1];
            b = capture.pixels[baseIndex+2];
            a = capture.pixels[baseIndex+3];
            
            //shape and color
            if (r > g && r > b ) {
              fill(r, 0, b-100, 150);
              ellipse(i+size/2, j+size/2, size/1.1, size/1.1);
            } else if (g > r && g > b) {
              fill(b, g, b, a);
              ellipse(i+size/2, j+size/2, size, size);
            } else if (r == g && g == b) {
              fill(r, g, b, a);
              ellipse(i+size/2, j+size/2, size, size);
            } else if (g == r && g > b) {
              fill(r, b, g, a);
              rect(i, j, size/1.1, size/1.1);
            } else if (b > r && b > g) {
              fill(r, g, b, a);
              arc(i+size/2, j+size/2, size, size,TWO_PI, PI); 
            } else {
              fill(0, 0, b-100, a);
              triangle(i+size/2, j, i, j+size, i+size, j+size);
            }
        }
    }
}