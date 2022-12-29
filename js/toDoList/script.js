window.addEventListener('load', () => {
	const form = document.querySelector("#new-task-form");
	const input = document.querySelector("#new-task-input");
	const list_el = document.querySelector("#tasks");

	form.addEventListener('submit', (e) => {
		e.preventDefault();

		const task = input.value;
    if (input.value == null || input.value == ""){
      alert("Заполните поле");
      return;
    }

		const task_el = document.createElement('div');
		task_el.classList.add('task');

		const task_content_el = document.createElement('div');
		task_content_el.classList.add('content');

    const do_check = document.createElement('input');
    do_check.type = 'checkbox';
    do_check.classList.add('do-check');
    task_el.appendChild(do_check);

		task_el.appendChild(task_content_el);



    const check = document.getElementById('new_task_priority');
    if (check.checked){
      const task_priority_el = document.createElement('span');
      task_priority_el.classList.add('check_priority');
      task_priority_el.innerText = '💥'
      task_content_el.appendChild(task_priority_el);
    }

		const task_input_el = document.createElement('input');
		task_input_el.classList.add('text');
		task_input_el.type = 'text';
		task_input_el.value = task;
		task_input_el.setAttribute('readonly', 'readonly');

		task_content_el.appendChild(task_input_el);

		const task_actions_el = document.createElement('div');
		task_actions_el.classList.add('actions');
		
		const task_edit_el = document.createElement('button');
		task_edit_el.classList.add('edit');
		task_edit_el.innerText = 'Изменить';

		const task_delete_el = document.createElement('button');
		task_delete_el.classList.add('delete');
		task_delete_el.innerText = 'Удалить';

		task_actions_el.appendChild(task_edit_el);
		task_actions_el.appendChild(task_delete_el);

		task_el.appendChild(task_actions_el);

		list_el.appendChild(task_el);

		input.value = '';


/*     if(do_check.checked){
      task_content_el.classList.add('end_list');
    } */

    do_check.addEventListener('click', (e) =>{
      task_input_el.classList.toggle('end_list');
      task_el.classList.toggle('end_task');
    })

		task_edit_el.addEventListener('click', (e) => {
			if (task_edit_el.innerText.toLowerCase() == "изменить") {
				task_edit_el.innerText = "Сохранить";
				task_input_el.removeAttribute("readonly");
				task_input_el.focus();
			} else {
				task_edit_el.innerText = "Изменить";
				task_input_el.setAttribute("readonly", "readonly");
			}
		});

		task_delete_el.addEventListener('click', (e) => {
			list_el.removeChild(task_el);
		});
	});
});