function move(input) {
    var currentNode;
    currentNode = input[0]
    switch (currentNode) {
        case "n1":
        $(document).ready(function(){
            $('#robot').css({ top: 380, left: 85 })
        });
        break
        case "n2":
        $(document).ready(function(){
            $('#robot').css({ top: 380, left: 185 })
        });
        case "n3":
        break
        $(document).ready(function(){
            $('#robot').css({ top: 480, left: 185 })
        });
        break
        case "n4":
        $(document).ready(function(){
            $('#robot').css({ top: 380, left: 435 })
        });
        break
        case "n5":
        $(document).ready(function(){
            $('#robot').css({ top: 480, left: 435 })
        });
        break
        case "n6":
        $(document).ready(function(){
            $('#robot').css({ top: 380, left: 710 })
        });
        break
        case "n7":
        $(document).ready(function(){
            $('#robot').css({ top: 318, left: 435 })
        });
        break
        case "n8":
        $(document).ready(function(){
            $('#robot').css({ top: 705, left: 325 })
        });
        break
        case "n9":
        $(document).ready(function(){
            $('#robot').css({ top: 225, left: 625 })
        });
        break
        case "n10":
        $(document).ready(function(){
            $('#robot').css({ top: 285, left: 710 })
        });
        break
        case "n11":
        $(document).ready(function(){
            $('#robot').css({ top: 182, left: 621 })
        });
        break
        case "n12":
        $(document).ready(function(){
            $('#robot').css({ top: 182, left: 621 })
        });
        break
        case "n13":
        $(document).ready(function(){
            $('#robot').css({ top: 188, left: 385 })
        });
        break
        case "n14":
        $(document).ready(function(){
            $('#robot').css({ top: 162, left: 230 })
        });
        break
        case "n15":
        $(document).ready(function(){
            $('#robot').css({ top: 100, left: 230 })
        });
        break
        case "n16":
        $(document).ready(function(){
            $('#robot').css({ top: 162, left: 85 })
        });
        break
        case "n17":
        $(document).ready(function(){
            $('#robot').css({ top: 254, left: 385 })
        });
        break
        case "n18":
        $(document).ready(function(){
            $('#robot').css({ top: 318, left: 385 })
        });
        break
        case "n19":
        $(document).ready(function(){
            $('#robot').css({ top: 325, left: 85 })
        });
        break
        default:
        $(document).ready(function(){
            $('#robot').css({ top: 380, left: 85 })
        });
    }

}


// function showCoords(event) {
//     var x = event.clientX;
//     var y = event.clientY;
//     var coords = "X coords: " + x + ", Y coords: " + y;
//     document.getElementById("demo").innerHTML = coords;
// }

//use this for testing move function
// var array = ["n2","n3"]
// move(array)