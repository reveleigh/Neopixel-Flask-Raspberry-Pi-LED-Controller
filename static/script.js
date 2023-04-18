var redButton = document.getElementById("red-button");
var orangeButton = document.getElementById("orange-button");
var yellowButton = document.getElementById("yellow-button");
var greenYellowButton = document.getElementById("green-yellow-button");
var greenButton = document.getElementById("green-button");
var greenCyanButton = document.getElementById("green-cyan-button");
var cyanButton = document.getElementById("cyan-button");
var blueCyanButton = document.getElementById("blue-cyan-button");
var blueButton = document.getElementById("blue-button");
var blueMagentaButton = document.getElementById("blue-magenta-button");
var magentaButton = document.getElementById("magenta-button");
var redMagentaButton = document.getElementById("red-magenta-button");
var whiteButton = document.getElementById("white-button");
var warmWhiteButton = document.getElementById("warm-white-button");
var coolWhiteButton = document.getElementById("cool-white-button");
var offButton = document.getElementById("off-button");
var rainbowButton = document.getElementById("rainbow-button");
var sendRGB = document.getElementById("send-RGB");

redButton.addEventListener("click", function () {
  // make a GET request to turn on the red light
  fetch("/red");
});

orangeButton.addEventListener("click", function () {
  // make a GET request to turn on the orange light
  fetch("/orange");
});

yellowButton.addEventListener("click", function () {
  // make a GET request to turn on the yellow light
  fetch("/yellow");
});

greenYellowButton.addEventListener("click", function () {
  // make a GET request to turn on the green-yellow light
  fetch("/green-yellow");
});

greenButton.addEventListener("click", function () {
  // make a GET request to turn on the green light
  fetch("/green");
});

greenCyanButton.addEventListener("click", function () {
  // make a GET request to turn on the green-cyan light
  fetch("/green-cyan");
});

cyanButton.addEventListener("click", function () {
  // make a GET request to turn on the cyan light
  fetch("/cyan");
});

blueCyanButton.addEventListener("click", function () {
  // make a GET request to turn on the blue-cyan light
  fetch("/blue-cyan");
});

blueButton.addEventListener("click", function () {
  // make a GET request to turn on the blue light
  fetch("/blue");
});

blueMagentaButton.addEventListener("click", function () {
  // make a GET request to turn on the blue-magenta light
  fetch("/blue-magenta");
});

magentaButton.addEventListener("click", function () {
  // make a GET request to turn on the magenta light
  fetch("/magenta");
});

redMagentaButton.addEventListener("click", function () {
  // make a GET request to turn on the red-magenta light
  fetch("/red-magenta");
});

whiteButton.addEventListener("click", function () {
  // make a GET request to turn on the white light
  fetch("/white");
});

warmWhiteButton.addEventListener("click", function () {
  // make a GET request to turn on the warm white light
  fetch("/warm-white");
});

coolWhiteButton.addEventListener("click", function () {
  // make a GET request to turn on the cool white light
  fetch("/cool-white");
});

offButton.addEventListener("click", function () {
  // make a GET request to turn off the light
  fetch("/black");
});

rainbowButton.addEventListener("click", function () {
  // make a GET request to turn on the rainbow light
  fetch("/rainbow");
});

const redSlider = document.getElementById("red");
const greenSlider = document.getElementById("green");
const blueSlider = document.getElementById("blue");

const redValue = document.getElementById("red-value");
const greenValue = document.getElementById("green-value");
const blueValue = document.getElementById("blue-value");

function updateColor() {
  const red = redSlider.value;
  const green = greenSlider.value;
  const blue = blueSlider.value;

  redValue.value = red;
  greenValue.value = green;
  blueValue.value = blue;

  fetch("/rgb", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: `red=${red}&green=${green}&blue=${blue}`,
  });
}

redSlider.addEventListener("input", updateColor);
greenSlider.addEventListener("input", updateColor);
blueSlider.addEventListener("input", updateColor);
