var calories = 1;

var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(75, canvas.offsetWidth / canvas.offsetHeight, 0.1, 1000);

var renderer = new THREE.WebGLRenderer();
renderer.setSize(canvas.offsetWidth * .95, canvas.offsetHeight * .95);

container = document.getElementById("canvas");
document.body.appendChild(container);
container.appendChild(renderer.domElement);

var geometry = new THREE.SphereGeometry(calories, 20, 20, 0, Math.PI * 2);
var material = new THREE.MeshBasicMaterial({color: 0xff0000, wireframe: true});
var cube = new THREE.Mesh(geometry, material);
scene.add(cube);

camera.position.y = 10;
camera.position.z = 50;

var render = function () {
  requestAnimationFrame(render);

  cube.rotation.y += 0.01;
  cube.updateMatrix();

  renderer.render(scene, camera);
};

var updateSphere = function(newRadius) {
  cube.scale.x += newRadius;
  cube.scale.y += newRadius;
  cube.scale.z += newRadius;
};

$(document).ready(function(){
  $(".70").click(function(){
    updateSphere(.7);
  });
  $(".120").click(function(){
    updateSphere(1.2);
  });
  $(".130").click(function(){
    updateSphere(1.3);
  });
  $(".140").click(function(){
    updateSphere(1.4);
  });
  $(".200").click(function(){
    updateSphere(2.0);
  });
  $(".210").click(function(){
    updateSphere(2.1);
  });
});

requestAnimationFrame(render);
