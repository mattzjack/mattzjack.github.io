var calories = 0;

$(document).ready(function(){
  $(".70").click(function(){
    calories += 7;
  });
  $(".120").click(function(){
    calories += 12;
  });
  $(".130").click(function(){
    calories += 13;
  });
  $(".140").click(function(){
    calories += 14;
  });
  $(".200").click(function(){
    calories += 20;
  });
  $(".210").click(function(){
    calories += 21;
  });
});

var canvas = document.getElementById("canvas");

var CANVAS_WIDTH = canvas.width;
var CANVAS_HEIGHT = canvas.height;


var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(75, CANVAS_WIDTH / CANVAS_HEIGHT, 0.1, 1000);

var renderer = new THREE.WebGLRenderer();
renderer.setSize(CANVAS_WIDTH, CANVAS_HEIGHT);
document.body.appendChild(canvas);
canvas.appendChild(renderer.domElement);

var geometry = new THREE.BoxGeometry(1, 1, 1);
var material = new THREE.MeshBasicMaterial({color: 0xff0000, wireframe: true});
var cube = new THREE.Mesh(geometry, material);
scene.add(cube);

camera.position.y = 1;
camera.position.z = 5;

function render() {
  requestAnimationFrame(render);

  cube.rotation.y += 0.01;

  renderer.render(scene, camera);
}

render();
