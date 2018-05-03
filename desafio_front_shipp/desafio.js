(function (window, undefined) {
    "use strict";
    
    function getRandomColor() {
        const hexa = "0123456789ABCDEF";
        let cor = "#";
        for (let i = 0; i < 3; i++) {
            cor += hexa[Math.floor(Math.random()*16)];
        }
        return cor;
    }

    function createThing() {
        let node = document.createElement("div");
        node.className = "thing";
        node.style.background = getRandomColor();
        
        let button = document.createElement("button");
        button.appendChild(document.createTextNode("color"));
        button.className = "action-change-color";
        button.onclick = () => {
            button.parentElement.style.background = getRandomColor();
        };
        
        let a = document.createElement("a");
        a.href = "#";
        a.className = "action-remove";
        a.appendChild(document.createTextNode("remover"));
        a.onclick = (e) => {
            e.preventDefault();
            node.remove();
        };
        
        node.appendChild(button);
        node.appendChild(document.createTextNode(" "));
        node.appendChild(a);

        return node;
    }

    // ponteiros para os elementos
    let info = document.getElementById("info");
    let addButton = document.getElementsByClassName("action-add")[0];
    let removeAllButton = document.getElementsByClassName("action-remove")[0];
    let pool = document.getElementById("pool");

    pool.firstChild.remove(); // remover texto residual contado como nó
    pool.lastChild.remove();
    pool.replaceChild(createThing(),pool.firstChild); // replace no thing que já existe
    
    // -- LISTENERS -- //
    let update = new Event("update"); // evento custom usado para atualizar a info
    
    // info
    SEA.addEventListener(info, "update", () => {
        let text = document.createTextNode(`A piscina contém ${pool.childElementCount} coisas.`);
        info.replaceChild(text, info.firstChild);
    });
    info.dispatchEvent(update);

    // adicionar
    SEA.addEventListener(addButton, "click", () => {
        let newChild = createThing();
        pool.appendChild(newChild);
        info.dispatchEvent(update);
    });

    // remover todos
    SEA.addEventListener(removeAllButton, "click", () => {
        while(pool.childNodes.length > 0) {
            pool.lastChild.remove();
        }
    });     
    
}(window));