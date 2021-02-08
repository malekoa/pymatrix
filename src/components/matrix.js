class Matrix extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `<div>
                            asdf
                          </div>`
    }
}
customElements.define('pymatrix-matrix', Matrix)