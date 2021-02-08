class Navbar extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `<div>
                            <p>${this.dataset.interior}</p>
                          </div>`
    }
}
customElements.define('pymatrix-navbar', Navbar)