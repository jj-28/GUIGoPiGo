function move(event) {
    var k = event.keyCode,
        chrId = document.getElementById('robot'),
        chr = {
            updown: function() {
                var y = parseInt(getComputedStyle(chrId).top);
                if (k == 38) {
                    --y;
                } else if (k == 40) {
                    ++y;
                }
                return y;
            },
            leftright: function() {
                var x = parseInt(getComputedStyle(chrId).left);
                if (k == 37) {
                    --x;
                } else if (k == 39) {
                    ++x;
                }
                return x;
            }
        };
    chrId.style.top = (chr.updown()) + "px";
    chrId.style.left = (chr.leftright()) + "px";

}

document.addEventListener('keydown', move);

// function showCoords(event) {
//     var x = event.clientX;
//     var y = event.clientY;
//     var coords = "X coords: " + x + ", Y coords: " + y;
//     document.getElementById("demo").innerHTML = coords;
// }

function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
}