
const HIDING_CLASS = "d-sm-none"

const NAV_BUTTON_CLASS = "nav-toggle-button"
const NAV_LIST_CLASS = "nav-list"


class NavHandler{

	constructor(button, list){
		this.button = button
		this.list = list
		this.isVisible = !list.classList.contains(HIDING_CLASS)
		this.button.onclick = () => { this.handleClick() }	
	}

	hideList(){
		this.list.classList.add(HIDING_CLASS)
		this.isVisible = false
	}

	showList(){
		this.list.classList.remove(HIDING_CLASS)
		this.isVisible = true
	}

	handleClick(){
		if(this.isVisible){
			this.hideList()
		}
		else{
			this.showList()
		}
	}

}


handler = new NavHandler(
	document.getElementsByClassName(NAV_BUTTON_CLASS)[0],
	document.getElementsByClassName(NAV_LIST_CLASS)[0]
)
