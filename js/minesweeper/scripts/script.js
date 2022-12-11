let width = 12;
let height = 12;
let bombs = 20;
let flags = 20;
let bomb_activated = false;
let field = [];
let cell_numbers = ["", "cell_one", "cell_two", "cell_three", "cell_four", "cell_five",
"cell_six", "cell_seven", "cell_eight"];
let cells = [];
let hover = -1;
let active = true;
let reset_btn;
let set_btn;
let set_box = false;

function setFlags(){
  let fl = document.getElementsByClassName('flags')[0];
  fl.textContent = flags;
}

function insert(width, height){
  let wrapper = document.getElementsByClassName('wrapper')[0];
  wrapper.innerHTML = '';
  for (let i = 0; i < width*height; i++){
    let newCell = document.createElement('div');
    newCell.classList.add('cell');
    newCell.classList.add('cell_closed');
    newCell.coord = i;
    cells.push(newCell);
    wrapper.append(newCell);
    newCell.addEventListener("mousedown", cell_pressed, false);
    newCell.addEventListener("contextmenu", function(e){e.preventDefault();}, false);
  }
}

function bomb_opened(){
  off_timer();
  let reset_btn = document.getElementsByClassName('reset_btn')[0];
  reset_btn.classList.remove('reset_btn_alive');
  reset_btn.classList.add('reset_btn_lost');
  active = false;
  for (let i = 0; i < width * height; i++){
    let cell = cells[i];
    let row = Math.floor(i / width);
    let column = Math.floor(i % width);
    if (field[row][column] >= 100000){
      cell.classList.remove('cell_closed');
      cell.classList.add('cell_opened');
      cell.classList.add('cell_bomb');
      if (field[row][column] == 100000 + 10){
        cell.classList.add('cell_bomb_disarmed');
      }
    }
    if (field[row][column] >= 10 && field[row][column] <= 18){
      cell.classList.remove('cell_flag');
      cell.classList.add('cell_no_flag');
    }
  }
}

function check_flag(){
  let all_disarmed = true;
  for (let i = 0; i < width * height; i++){
    let row = Math.floor(i / width);
    let column = Math.floor(i % width);
    if (field[row][column] == 100000){
      all_disarmed = false;
      break;
    }
  }
  if (all_disarmed){
    off_timer();
    active = false;
    let reset_btn = document.getElementsByClassName('reset_btn')[0];
    reset_btn.classList.remove('reset_btn_alive');
    reset_btn.classList.add('reset_btn_win');
  }
}

function cell_pressed(event, num=0, clicked=true, rright=false){
  let right = false;
  if (!active){
    return;
  }
  if (rright){
    right = true;
  }
  if (clicked && event){
    if (event.which == 3){
      right = true;
    }
    num = event.target.coord;
  }
  if (event && hover >= 0){
    cells[hover].classList.remove('cell_hover');
    hover = -1;
  }
  if (!bomb_activated){
    bomb_activated = true;
    createField(num);
    timer();
  }
  let row = Math.floor(num / width);
  let column = Math.floor(num % width);
  let cell = cells[num];
  if (field[row][column] == 100000 && clicked && !right){
    cell.classList.remove('cell_closed');
    cell.classList.add('cell_opened');
    cell.classList.add('cell_bomb');
    cell.classList.add('cell_bomb_first');
    bomb_opened();
  }
  if (field[row][column] == 0 && !right){
    cell.classList.remove('cell_closed');
    cell.classList.add('cell_opened');
    field[row][column] = -2000000;
    if (row-1 >= 0 && column - 1 >= 0){
      cell_pressed(false, (row-1)*width + column - 1, false);
    }
    if (row-1 >= 0){
      cell_pressed(false, (row-1)*width + column, false);
    }
    if (column - 1 >= 0){
      cell_pressed(false, (row)*width + column - 1, false);
    }
    if (row+1 < height && column + 1 < width){
      cell_pressed(false, (row+1)*width + column + 1, false);
    }
    if (row+1 < height){
      cell_pressed(false, (row+1)*width + column, false);
    }
    if (column + 1 < width){
      cell_pressed(false, (row)*width + column + 1, false);
    }
    if (row+1 < height  && column - 1 >= 0){
      cell_pressed(false, (row+1)*width + column - 1, false);
    }
    if (row-1 >= 0 && column + 1 < width){
      cell_pressed(false, (row-1)*width + column + 1, false);
    }
  }
  if (field[row][column] >= 1 && field[row][column] <= 8 && !right){
    cell.classList.remove('cell_closed');
    cell.classList.add('cell_opened');
    cell.classList.add(cell_numbers[field[row][column]]);
  }
  if (right && cell.classList.contains('cell_closed') && !cell.classList.contains('cell_flag')){
    if (flags > 0){
      cell.classList.add('cell_flag');
      field[row][column] += 10;
      flags--;
      setFlags();
      check_flag();
    }
    return;
  }
  if (right && cell.classList.contains('cell_flag')){
    cell.classList.remove('cell_flag');
    field[row][column] -= 10;
    flags++;
    setFlags();
  }
}

function createField(save){
  field_line = [];
  for (let i = 0; i < width; i++){
    field_line.push(0);
  }
  for (let i = 0; i < height; i++){
    field.push(field_line.slice());
  }
  bombs_array = [];
  let save_row = Math.floor(save / width);
  let save_column = Math.floor(save % width);
  for (let i = 0; i < width*height; i++){
    let row = Math.floor(i / width);
    let column = Math.floor(i % width);
    if (Math.abs(row - save_row) <= 1 && Math.abs(column - save_column) <= 1){
      continue;
    }
    bombs_array.push(i);
  }
  for (let i = 0; i < bombs; i++){
    let rnd = Math.floor(Math.random()*bombs_array.length);
    field[Math.floor(bombs_array[rnd]/width)][bombs_array[rnd]%width] = 100000;

    bombs_array.splice(rnd, 1);
  }
  for (let i = 0; i < width*height; i++){
    let row = Math.floor(i / width);
    let column = Math.floor(i % width);
    if (field[row][column] != 100000){
      let sum = 0;
      if (row - 1 >= 0 && column - 1 >= 0){
        if (field[row - 1][column - 1] == 100000){
          sum++;
        }
      }
      if (row - 1 >= 0){
        if (field[row - 1][column] == 100000){
          sum++;
        }
      }
      if (column - 1 >= 0){
        if (field[row][column-1] == 100000){
          sum++;
        }
      }
      if (row + 1 < height && column < width){
        if (field[row + 1][column + 1] == 100000){
          sum++;
        }
      }
      if (row + 1 < height){
        if (field[row + 1][column] == 100000){
          sum++;
        }
      }
      if (column + 1 < width){
        if (field[row][column + 1] == 100000){
          sum++;
        }
      }
      if (row - 1 >= 0 && column + 1 < width){
        if (field[row - 1][column + 1] == 100000){
          sum++;
        }
      }
      if (row + 1 < height && column - 1 >=  0){
        if (field[row + 1][column - 1] == 100000){
          sum++;
        }
      }
      field[row][column] = sum;
    }
  }
}

function seetingProcess(){
  let set_window = document.getElementsByClassName('params')[0];
  let inputs = set_window.getElementsByTagName('input');
  inputs[0].value = width;
  inputs[1].value = height;
  inputs[2].value = bombs;
  set_window.style.display = "block";
  active = false;
  set_box = true;
}

function okProcess(){
  let set_window = document.getElementsByClassName('params')[0];
  let inputs = set_window.getElementsByTagName('input');
  let ok = true;
  let changed = false;
  if ( inputs[0].value  >= 8 && inputs[0].value  <= 99){
    if (width != inputs[0].value){
      changed = true;
    }
    width = parseInt(inputs[0].value);
  }
  else{
    inputs[0].value = width;
    ok = false;
  }
  if (inputs[1].value  >= 3 && inputs[1].value  <= 99){
    if (height != inputs[1].value){
      changed = true;
    }
    height = parseInt(inputs[1].value);
  }
  else{
    inputs[1].value = height;
    ok = false
  }
  if (width*height - 9 >= inputs[2].value){
    if (bombs != inputs[2].value){
      changed = true;
    }
    bombs = parseInt(inputs[2].value);
  }
  else{
    inputs[2].value = width*height - 9;
    ok = false
  }
  if (!changed){
    active = true;
    set_window.style.display = "none";
    set_box = false;
  }
  if (ok && changed){
    set_window.style.display = "none";
    set_box = false;
    init();
  }
}

function keyProcess(e){
    let code = e.keyCode;
    if (code == '37' || code == '38' || code == '39' || code == '40'){
      if (hover == -1){
        hover = 0;
        cells[hover].classList.add('cell_hover');
        return;
      }
    }
    if (code == '13' || code == '32'){
      if (e.ctrlKey){
        cell_pressed(false, hover, true, true);
      }
      else{
        if (set_box){
          okProcess();
          return;
        }
        if (hover == -3){
          init();
          hover = -1;
          reset_btn.classList.remove('cell_hover');
          return;
        }
        if (hover == -2){
          seetingProcess();
          hover = -1;
          set_btn.classList.remove('cell_hover');
          return;
        }
        cell_pressed(false, hover, true);
      }
    }
    if (code == '38') {
      if (hover - width >= 0){
        cells[hover].classList.remove('cell_hover');
        hover -= width;
        cells[hover].classList.add('cell_hover');
      }
      else if (hover >= 0) {
        cells[hover].classList.remove('cell_hover');
        hover = -2;
        set_btn.classList.add('cell_hover');
      }
    }
    else if (code == '40') {
      if (hover < 0){
        set_btn.classList.remove('cell_hover');
        reset_btn.classList.remove('cell_hover');
        hover = 0;
        cells[hover].classList.add('cell_hover');
      }
      else if (hover + width < width * height && hover >= 0){
        cells[hover].classList.remove('cell_hover');
        hover += width;
        cells[hover].classList.add('cell_hover');
      }
    }
    else if (code == '37') {
      if (hover == -3){
        reset_btn.classList.remove('cell_hover');
        hover = -2;
        set_btn.classList.add('cell_hover');
      }
      if (hover % width != 0  && hover >= 0){
        cells[hover].classList.remove('cell_hover');
        hover -= 1;
        cells[hover].classList.add('cell_hover');
      }
    }
    else if (code == '39') {
      if (hover == -2){
        set_btn.classList.remove('cell_hover');
        hover = -3;
        reset_btn.classList.add('cell_hover');
      }
      if (hover % width != width - 1  && hover >= 0){
        cells[hover].classList.remove('cell_hover');
        hover += 1;
        cells[hover].classList.add('cell_hover');
      }
    }

}

function init(){
  flags = bombs;
  bomb_activated = false;
  field = [];
  cells = [];
  hover = -1;
  setFlags();
  insert(width, height);
  on_timer();
  let wrapper = document.getElementsByClassName('wrapper')[0];
  wrapper.style.gridTemplateColumns = "repeat(" + width + ", 50px)";
  wrapper.style.gridTemplateRows = "repeat(" + height + ", 50px)";

  let area = document.getElementsByClassName('area')[0];
  area.style.gridTemplateColumns = "auto " + (50*width+10) + "px auto";
  area.style.gridTemplateRows = "auto " + (50*width+10) + "px auto";

  set_btn = document.getElementsByClassName('set_btn')[0];
  set_btn.addEventListener("click", seetingProcess);

  let ok_btn = document.getElementsByClassName('ok_btn')[0];
  ok_btn.addEventListener("click", okProcess);

  reset_btn = document.getElementsByClassName('reset_btn')[0];
  reset_btn.addEventListener("click", init);
  reset_btn.classList.remove('reset_btn_lost');
  reset_btn.classList.remove('reset_btn_win');
  reset_btn.classList.add('reset_btn_alive');

  document.addEventListener('keydown', keyProcess);

  active = true;
}

document.addEventListener("DOMContentLoaded", init);



