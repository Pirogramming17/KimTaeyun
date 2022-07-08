const duration = 60;
let lapse = 0;
let intervalID;

const lapseEl = document.querySelector(".lapse .seconds");

function fillZero(num) {
  return String(num).padStart(2, "0");
}

lapseEl.innerText = fillZero(0);

const startBtn = document.querySelector(".start-btn");
const stopBtn = document.querySelector(".stop-btn");
const resetBtn = document.querySelector(".reset-btn");

startBtn.addEventListener("click", function () {
  if (!lapse) {
    lapseEl.innerText = fillZero(0);
  }

  intervalID = setInterval(
    function () {
      lapseEl.innerText = String(lapse).padStart(2, "0");

      if (lapse === duration) {
        clearInterval(intervalID);
        lapse = 0;
      }
    },

    1000
  );
});

stopBtn.addEventListener("click", function () {
  clearInterval(intervalID);
});

resetBtn.addEventListener("click", function () {
  clearInterval(intervalID);
  lapse = 0;
  lapseEl.innerText = fillZero(0);
});

// // checking all checkboxes
// document.getElementById("select-all").onclick = function () {
//   var checkboxes = document.getElementsByName("lapse-num");
//   for (var checkbox of checkboxes) {
//     checkbox.checked = this.checked;
//   }
// };
