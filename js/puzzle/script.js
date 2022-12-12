let cells = [];
let holders = [];


function isOk(holderId) {
  return !holders[holderId];
}

function end() {
  document.getElementById('win').style.display = "block";
  let parts = document.getElementsByClassName('pic');
  for (let i = 0; i < parts.length; i++) {
    parts[i].classList.remove('drag');
  }
}

function checkAll() {
  let area = document.getElementsByClassName('area')[0];
  let arealocale = getlocale(area);
  let areaWidth = area.getBoundingClientRect().width;
  let areaHeight = area.getBoundingClientRect().height;
  let parts = document.getElementsByClassName('pic');
  for (let i = 0; i < 54; i++) {
    holders[i] = false;
  }
  for (let i = 0; i < parts.length; i++) {
    let insideTop = parseInt(parts[i].style.top, 10) - arealocale.top;
    let insideLeft = parseInt(parts[i].style.left, 10) - arealocale.left;
    if (insideTop >= 0 && insideLeft >= 0 && insideTop < areaHeight && insideLeft < areaWidth) {
      if (insideTop % 50 == 0 || insideLeft % 50 == 0) {
        let holderId = parseInt(insideTop / 50) * 9 + parseInt(insideLeft / 50);
        holders[holderId] = parts[i].num;
      }
    }
  }
  for (let i = 0; i < parts.length; i++) {
    if (holders[i] != i) {
      break;
    }
    if (i + 1 == parts.length) {
      end();
    }
  }
}

function insert() {
  for (let i = 0; i < cells.length; i++) {
    document.body.append(cells[i]);
    cells[i].style.top = parseInt(Math.random() * 450, 10) + "px";
    cells[i].style.left = parseInt(Math.random() * 420, 10) + "px";
    cells[i].num = i;
  }
}

function finput_handler(evt) {
  if (event.target.files.length < 0) {
    return;
  }
  let img = document.getElementById('donwload_img');
  let reader = new FileReader();
  let data = URL.createObjectURL(event.target.files[0]);
  img.src = data;
  img.onload = function () {
    let img = document.getElementById('donwload_img');
    let width = img.naturalWidth;
    let height = img.naturalHeight;
    img.style.display = "none";
    let startWidth = 0;
    let startHeight = 0;
    if (width / height > 3 / 2) {
      startWidth = Math.abs(width - (height / 2 * 3)) / 2;
    }
    else {
      startHeight = Math.abs(height - (width / 3 * 2)) / 2;
    }
    let size = (height - startHeight * 2) / 6;

    for (let j = startHeight; j < height - startHeight; j += size) {
      for (let i = startWidth; i < width - startWidth; i += size) {
        let pic = document.createElement('div');
        pic.classList.add('pic');
        pic.style.backgroundImage = "url(" + data + ")";
        pic.style.backgroundPosition = "right " + (i + size) * (50 / size) + "px bottom " + (j + size) * (50 / size) + "px";
        pic.width = "50px";
        pic.height = "50px";

        pic.style.backgroundSize = 900 + "%";

        pic.classList.add('drag');
        cells.push(pic);
      }
    }
    insert();
    document.getElementsByClassName('lauch')[0].style.display = "none";

  }

}

function init() {
  let finput = document.getElementById('uploaded_image');
  finput.addEventListener('change', finput_handler);
  let area = document.getElementsByClassName('area')[0];
  for (let i = 0; i < 54; i++) {
    let newDiv = document.createElement('div');
    newDiv.classList.add('puzzleCell');
    area.append(newDiv);
    holders.push(false);
  }


}

document.addEventListener("DOMContentLoaded", init);


let wrapper = document.querySelector('.image_wrapper')
function donwload(input) {
  let file = input.files[0];
  let rd = new FileReader();
  rd.readAsDataURL(file);

  rd.onload = function () {
    let img = document.createElement('img');
    wrapper.appendChild(img);
    img.src = rd.result;
  }
}




let DragManager = new function () {
  let drag = false;
  let self = this;

  function onMouseDown(e) {

    if (e.which != 1) return;


    let elem = e.target.closest('.drag');
    if (!elem) return;
    drag = elem;
    drag.started = false;
    drag.downX = e.pageX;
    drag.downY = e.pageY;
    drag.style.zIndex = 999;
    return false;
  }

  function onMouseMove(e) {
    if (!drag) return;
    if (!drag.started) {

      let moveX = e.pageX - drag.downX;
      let moveY = e.pageY - drag.downY;


      if (Math.abs(moveX) < 3 && Math.abs(moveY) < 3) {
        return;
      }
      drag.started = true;
      if (!drag) {
        drag = false;
        return;
      }

      let coords = getlocale(drag);

      drag.shiftX = drag.downX - coords.left;
      drag.shiftY = drag.downY - coords.top;
      drag.old = {};
      drag.old.left = drag.style.left;
      drag.old.top = drag.style.top;

    }


    drag.style.left = e.pageX - drag.shiftX + 'px';
    drag.style.top = e.pageY - drag.shiftY + 'px';

    return false;
  }

  function onMouseUp(e) {
    if (drag) {

      let area = document.getElementsByClassName('area')[0];
      let arealocale = getlocale(area);
      let areaWidth = area.getBoundingClientRect().width;
      let areaHeight = area.getBoundingClientRect().height;
      let insideTop = e.pageY - arealocale.top;
      let insideLeft = e.pageX - arealocale.left;
      if (insideTop >= 0 && insideLeft >= 0 && insideTop < areaHeight && insideLeft < areaWidth) {
        drag.style.top = arealocale.top + insideTop - insideTop % 50 + "px";
        drag.style.left = arealocale.left + insideLeft - insideLeft % 50 + "px";
        let holderId = parseInt(insideTop / 50) * 9 + parseInt(insideLeft / 50);


      }
      drag.style.zIndex = 1;
      checkAll();
    }
    drag = false;
    drag.started = false;
  }

  document.onmousemove = onMouseMove;
  document.onmouseup = onMouseUp;
  document.onmousedown = onMouseDown;
};


function getlocale(elem) {
  let box = elem.getBoundingClientRect();

  return {
    top: box.top + pageYOffset,
    left: box.left + pageXOffset
  };

}
