const fs = require('fs');
const THREE = require('three');

var stats = fs.statSync(process.argv[2])
console.log(stats)
var raw = fs.readFileSync(process.argv[2], 'utf-8');

//console.log(data);

//split by row and delete garbage
//console.log(raw)
data = raw.split(/\n/);
//console.log(data.length);
loops = data.length
//console.log(data[loops-1])
for(var i=0; i < loops; i++){
  //console.log(data[i]);
  data[i] = data[i].split(',');
}

var interp_steps = 5; //何分割するか

//console.log(rows.length)
for (var i=0; i<loops-1; i++){
  var stepi = i*interp_steps;
  //console.log(i)
  //console.log(data.length)
  interp = []

  for (var j=0; j<interp_steps-1; j++){

    var portion = [];

    for (var k=0; k*3<data[0].length; k++){
      var stepk = k*3;
      var eust = new THREE.Euler(THREE.Math.degToRad(data[stepi][stepk+1]), THREE.Math.degToRad(data[stepi][stepk+2]), THREE.Math.degToRad(data[stepi][stepk]));
      //if(k==50) console.log(data[stepi][stepk+1] + ", " +  data[stepi][stepk+2] + ", " + data[stepi][stepk])
      var euend = new THREE.Euler(THREE.Math.degToRad(data[stepi+1][stepk+1]), THREE.Math.degToRad(data[stepi+1][stepk+2]), THREE.Math.degToRad(data[stepi+1][stepk]));
      //if(k==50) console.log(data[stepi+1][stepk+1] + ", " +  data[stepi+1][stepk+2] + ", " + data[stepi+1][stepk])
      var qtst = new THREE.Quaternion().setFromEuler(eust);
      var qtend = new THREE.Quaternion().setFromEuler(euend);

      var qtmid = qtst.normalize().slerp(qtend.normalize(), (1/interp_steps)*(j+1));
      var eumid = new THREE.Euler().setFromQuaternion(qtmid.normalize());

      portion.push(THREE.Math.radToDeg(eumid.z), THREE.Math.radToDeg(eumid.x), THREE.Math.radToDeg(eumid.y));
    }
    interp.push(portion)
  }

  for (var l=0; l<interp_steps-1; l++){
    data.splice(stepi+1+l, 0, interp[l]);
  }
  //console.log(interp[0].length)
  
  //console.log(data.length)
  //return;
}

for(var i=0; i<data.length; i++){
  for(var j=0; j<data[i].length; j++){
    data[i][j] = parseFloat(data[i][j]).toFixed(6);
  }
  data[i] = data[i].join(',');
  //console.log(data[i]);
}

data = data.join('\n');
//bvh.framedata = data;
//console.log(interp_data)
//console.log(data.length);
//console.log(data[200].length);
output = process.argv[2].replace(".csv", "_out.csv")
fs.writeFile(output, data, function(err){
  if(err){
    return console.log(err);
  }
  console.log("output saved to" +  output);
});
console.log(loops)
return;

