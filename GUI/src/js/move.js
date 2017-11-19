function move(input) {
    var currentNode;
    currentNode = input[0]
    switch (currentNode) {
        case "n1":
        $(document).ready(function(){
            $('#robot').css({ top: 400, left: 100 })
        });
        break
        case "n2":
        $(document).ready(function(){
            $('#robot').css({ top: 400, left: 200 })
        });
        case "n3":
        break
        $(document).ready(function(){
            $('#robot').css({ top: 500, left: 200 })
        });
        break
        case "n4":
        $(document).ready(function(){
            $('#robot').css({ top: 400, left: 450 })
        });
        break
        case "n5":
        $(document).ready(function(){
            $('#robot').css({ top: 500, left: 450 })
        });
        break
        case "n6":
        $(document).ready(function(){
            $('#robot').css({ top: 400, left: 725 })
        });
        break
        case "n7":
        $(document).ready(function(){
            $('#robot').css({ top: 338, left: 450 })
        });
        break
        case "n8":
        $(document).ready(function(){
            $('#robot').css({ top: 725, left: 340 })
        });
        break
        case "n9":
        $(document).ready(function(){
            $('#robot').css({ top: 245, left: 640 })
        });
        break
        case "n10":
        $(document).ready(function(){
            $('#robot').css({ top: 305, left: 725 })
        });
        break
        case "n11":
        $(document).ready(function(){
            $('#robot').css({ top: 202, left: 636 })
        });
        break
        case "n12":
        $(document).ready(function(){
            $('#robot').css({ top: 102, left: 636 })
        });
        break
        case "n13":
        $(document).ready(function(){
            $('#robot').css({ top: 208, left: 400 })
        });
        break
        case "n14":
        $(document).ready(function(){
            $('#robot').css({ top: 182, left: 245 })
        });
        break
        case "n15":
        $(document).ready(function(){
            $('#robot').css({ top: 120, left: 245 })
        });
        break
        case "n16":
        $(document).ready(function(){
            $('#robot').css({ top: 182, left: 100 })
        });
        break
        case "n17":
        $(document).ready(function(){
            $('#robot').css({ top: 274, left: 400 })
        });
        break
        case "n18":
        $(document).ready(function(){
            $('#robot').css({ top: 338, left: 400 })
        });
        break
        case "n19":
        $(document).ready(function(){
            $('#robot').css({ top: 345, left: 100 })
        });
        break
        default:
        $(document).ready(function(){
            $('#robot').css({ top: 400, left: 100 })
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
var array = ["n11","n3"]
move(array)