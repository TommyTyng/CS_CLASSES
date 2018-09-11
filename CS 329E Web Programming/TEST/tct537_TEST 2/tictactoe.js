
var count = 0;

var markButton = function (id) {
  var button = document.getElementById(id);
  if (button.innerHTML === "X" || button.innerHTML === "O") {
    return
  }
  else {
    if (count % 2 === 0) {
      button.innerHTML = "X";
    }
    else {
      button.innerHTML = "O";
    }
    count += 1;
  }
  if (count >= 4){
    checkGame();
  }
};


var checkGame = function () {
  matrix = [["", "", ""], ["", "", ""], ["", "", ""]];
  for (var row = 0; row <= 2; row++) {
    for (var col = 0; col <= 2; col++) {
      matrix[row][col] = document.getElementById("b" + row.toString() + col.toString()).innerHTML;
    }
  }
  // Check for Row win
  for (var i = 0; i <= 2; i++) {
    if ((matrix[i][0] === matrix[i][1]) && (matrix[i][1] === matrix[i][2]) && (matrix[i][0] === "X" || matrix[i][0] === "O")) {
      window.alert(matrix[i][0] + " WON!");
      return;
    }
  }
  // Check for Column win
  for (var j = 0; j <= 2; j++) {
    if ((matrix[0][j] === matrix[1][j]) && (matrix[1][j] === matrix[2][j]) && (matrix[0][j] === "X" || matrix[0][j] === "O")) {
      window.alert(matrix[0][j] + " WON!");
      return
    }
  }
  // Check for Diagonal win
  if ((matrix[0][0] === matrix[1][1]) && (matrix[1][1] === matrix[2][2]) && (matrix[0][0] === "X" || matrix[0][0] === "O")) {
    window.alert(matrix[0][0] + " WON!");
    return
  }
  if ((matrix[0][2] === matrix[1][1]) && (matrix[1][1] === matrix[2][0]) && (matrix[0][2] === "X" || matrix[0][2] === "O")) {
    window.alert(matrix[0][2] + " WON!");
    return
  }
};