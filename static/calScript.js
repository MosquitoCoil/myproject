function appendValue(value) {
  const resultField = document.getElementById("result");
  if (resultField.value === "0" && value !== ".") {
    resultField.value = value;
  } else {
    resultField.value += value;
  }
}

function clearResult() {
  document.getElementById("result").value = "0";
}

function calculateResult() {
  const resultField = document.getElementById("result");
  try {
    resultField.value = eval(resultField.value.replace(/x/g, "*"));
  } catch (e) {
    resultField.value = "Error";
  }
}
