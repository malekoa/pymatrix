class Matrix extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `<div>
                            asdf
                          </div>`
    }
}
customElements.define('pymatrix-matrix', Matrix)
/* ------------------------------------------------------------------------------ */
class Navbar extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `<div>
                            <p>${this.dataset.interior}</p>
                          </div>`
    }
}
customElements.define('pymatrix-navbar', Navbar)
/* ------------------------------------------------------------------------------ */
