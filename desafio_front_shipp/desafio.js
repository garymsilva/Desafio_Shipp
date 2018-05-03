(function (window, undefined) {
    "use strict";
    
    let update = new Event("update"); // evento custom usado para atualizar a info
    let THINGS_COUNTER = 1;

    var getRandomColor = () => {
        const hexa = "0123456789ABCDEF";
        let cor = "#";
        for (let i = 0; i < 3; i++) {
            cor += hexa[Math.floor(Math.random()*16)];
        }
        return cor;
    }

    var createThing = () => {
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

    var updateInfo = () => {
        let text = document.createTextNode(`A piscina contém ${THINGS_COUNTER} coisas.`);
        info.replaceChild(text, info.firstChild);
    }

    // ponteiros para os elementos
    let info = document.getElementById("info");
    let addButton = document.getElementsByClassName("action-add")[0];
    let removeAllButton = document.getElementsByClassName("action-remove")[0];
    let pool = document.getElementById("pool");

    // remover texto residual contado como nó
    pool.firstChild.remove();
    pool.lastChild.remove();

    // replace no thing que já existe
    pool.replaceChild(createThing(),pool.firstChild);

    // start no texto da info
    updateInfo(info);
    
    SEA.addEventListener(info, "update", () => updateInfo(info));

    SEA.addEventListener(addButton, "click", () => {
        let newChild = createThing();
        pool.appendChild(newChild);
        THINGS_COUNTER++;
        info.dispatchEvent(update);
    });

    SEA.addEventListener(removeAllButton, "click", () => {
        while(pool.childNodes.length > 0) {
            pool.lastChild.remove();
        }
    });
    
}(window));