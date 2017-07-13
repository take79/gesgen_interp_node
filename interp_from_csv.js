const fs = require('fs');
const THREE = require('three');
const readline = require('readline');

var numFrames;
var secsPerFrame;
var bvhdata = [];
var lin;

fs.readFile('input_vec.csv', 'utf-8', function (err,raw) {
  if (err) {
    console.log("hage")
    return console.log(err);
  }
  console.log("hoge");
  //console.log(data);

  //split by row and delete garbage
  data = raw.split(/\r?\n/)
  //console.log(data.length);
  for(var i=0; i < data.length; i++){
    //console.log(data[i]);
    data[i] = data[i].split(',');
  }

  var interp_steps = 2; //何分割するか

  //console.log(rows.length)
  for (var i=0; i*interp_steps<data.length-interp_steps-1; i++){
    var stepi = i*interp_steps;
    interp = []

    for (var tmp=0; tmp<interp_steps-1; tmp++){
      var portion = [];
      for (var j=0; j*3<data[0].length; j++){
        var stepj = j*3;
        //console.log(stepj)
        var eust = new THREE.Euler(THREE.Math.degToRad(data[stepi][stepj+1]), THREE.Math.degToRad(data[stepi][stepj+2]), THREE.Math.degToRad(data[stepi][stepj]));
        var euend = new THREE.Euler(THREE.Math.degToRad(data[stepi+interp_steps-1][stepj+1]), THREE.Math.degToRad(data[stepi+interp_steps-1][stepj+2]), THREE.Math.degToRad(data[stepi+interp_steps-1][stepj]));
        var qtst = new THREE.Quaternion().setFromEuler(eust);
        var qtend = new THREE.Quaternion().setFromEuler(euend);
        var mid = qtst.slerp(qtend, (1/interp_steps)*(tmp+1));
        var mid_eu = new THREE.Euler().setFromQuaternion(mid);
        portion.push(THREE.Math.radToDeg(mid_eu.z), THREE.Math.radToDeg(mid_eu.x), THREE.Math.radToDeg(mid_eu.y));
      }
      interp.push(portion)
    }

    console.log(interp[0].length)
    for (var l=0; l<interp_steps-1; l++){
      data.splice(stepi+(interp_steps-1), 0, interp[l]);
    }
    console.log(data.length)
    //return;
  }
  for(var i=0; i<data.length; i++){
    data[i] = data[i].join(',');
    console.log(data[i]);
  }
  data = data.join('\n');
  //bvh.framedata = data;
  //console.log(interp_data)
  //console.log(data.length);
  //console.log(data[200].length);
  fs.writeFile("output_vec.csv", data, function(err){
    if(err){
      return console.log(err);
    }
    console.log("output saved to output_vec.csv");
  });
  return;
});

