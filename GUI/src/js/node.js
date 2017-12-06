var brakes;
var cmdqueue = [];
var edgeQueue = [];
var progressNodes;
var progressEdges;
var progressRobot;
var path;

var linebreak = document.createElement("br");

function addWaypoint(id) {
    var table = document.getElementById("waypointtable");
    var waypointId = document.getElementById(id).id;
    var console = document.getElementById("console");


    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);

    var consoleCount = console.rows.length;

    if (cmdqueue.length == 0) {
        cmdqueue.push(id);
        window.alert(id);
        console.insertRow(consoleCount).innerHTML = ("Waypoint Queue: " + cmdqueue.toString());
        console.insertRow(consoleCount).innerHTML = ("Added Waypoint: " + id + " at Index: " + cmdqueue.indexOf(id));


        row.insertCell(0).innerHTML = "Waypoint: " + waypointId;
        row.insertCell(1).innerHTML =
            '<input type="button" id="delete" class="deleteDep" value="Delete" onclick = "deleteButton(this);" >';
    } else {
        if (cmdqueue[cmdqueue.length - 1] != id) {
            cmdqueue.push(id);
            console.insertRow(consoleCount).innerHTML = ("Waypoint Queue: " + cmdqueue.toString());
            console.insertRow(consoleCount).innerHTML = ("Added Waypoint: " + id + " at Index: " + cmdqueue.indexOf(id));

            row.insertCell(0).innerHTML = "Waypoint: " + waypointId;
            row.insertCell(1).innerHTML =
                '<input type="button" id="delete" class="deleteDep" value="Delete" onclick = "deleteButton(this);" >';
        } else {
            console.insertRow(consoleCount).innerHTML = ("You can't add the same waypoint 2 times in a row. Ex:No N1-N1-N@");
        }
    }
}

function deleteButton(obj) {
    var console = document.getElementById("console");
    var consoleCount = console.rows.length;
    var index = obj.parentNode.parentNode.rowIndex;
    var table = document.getElementById("waypointtable");

    var waypoint = table.rows[index].cells[0].innerHTML;
    cmdqueue.splice(index, 1)

    console.insertRow(consoleCount).innerHTML = ("Waypoint Queue: " + cmdqueue.toString());
    console.insertRow(consoleCount).innerHTML = ("Deleting: " + waypoint + " at Index: " + index);

}

// clears waypoints and edges
function clearWaypoints() {
    var console = document.getElementById("console");
    var consoleCount = console.rows.length;
    while (cmdqueue.length > 0) {
        cmdqueue.pop();
        $('#waypointtable tbody').html('');
    }
    console.insertRow(consoleCount).innerHTML = ("Waypoint Queue: " + cmdqueue.toString());
    console.insertRow(consoleCount).innerHTML = "Waypoints Cleared";
}

function stop() {
    var console = document.getElementById("console");
    var consoleCount = console.rows.length;
    console.insertRow(consoleCount).innerHTML = "Process Stopped";
}

//adds and removes edges from array onClick
function maintainQueue(id) {
    var console = document.getElementById("console");
    var consoleCount = console.rows.length;
    if (edgeQueue.indexOf(id) == -1) {
        edgeQueue.push(id);
        console.insertRow(consoleCount).innerHTML = ("Obstacle Queue: " + edgeQueue.toString());
        console.insertRow(consoleCount).innerHTML = ("Added Obstacle " + id);
    } else {
        edgeQueue.splice(edgeQueue.indexOf(id), 1);
        edgeIndex = edgeQueue.indexOf(id);
        console.insertRow(consoleCount).innerHTML = ("Obstacle Queue: " + edgeQueue.toString());
        console.insertRow(consoleCount).innerHTML = ("Removing " + id);
    }
}


// Creates the websockets connection
function setup2() {
    var console = document.getElementById("console");
    var consoleCount = console.rows.length;
    console.insertRow(consoleCount).innerHTML = ("Initiating robot")
    var $txt = $("#data");      			// assigns the data(hostname/ip address) entered in the text box
    name = $txt.val();          			// Variable name contains the string(hostname/ip address) entered in the text box
    var host = "ws://" + name + ":9093/ws"; 	// combines the three string and creates a new string
    var socket = new WebSocket(host);
    var $txt = $("data");
    var $btnSend = $("#sendtext");
    $txt.focus();

    // event handlers for UI
    $btnSend.on('click', function () {
        var text = $txt.val();
        if (text == "") {
            return;
        }
        $txt.val("");
    });

    if (socket) {
        var count = 1;
        //sends initial client message
        socket.onopen = function () {
            // socket.send("client ready");
            buttons();
        }

        //Sends JSON object containing node and edges
        function buttons() {
            var g;
            // var g = {'node': cmdqueue.toString(), 'edges': edgeQueue.toString()};
            // socket.send(JSON.stringify(g));
            if (edgeQueue.length == 1) {
                g = cmdqueue[0].toString() + "/" + edgeQueue.toString();

            } else {
                g = cmdqueue[0].toString();
            }
            window.alert(g.toString());
            socket.send(g.toString());
        }

        //clears previous update information
        function clearUpdate() {
            // progressEdges = [];
            progressNodes = [];
            progressRobot = "";
        }


        socket.onmessage = function (msg) {
            // if (typeof msg == 'string') {
            //     if (msg == "request nodes and edges") {
            //         buttons();
            //     } else {
            //         console.insertRow(consoleCount).innerHTML = ("unexpected string received: " + msg);
            //     }
            // } else {
            //     clearUpdate();
            //     var response =[] ;
            //         response = JSON.parse(msg);
            //     // tokenize array elements and put into seperate arrays
            //     // progressNodes = response.[0].split(" ");
            //     // progressEdges = response.[1].split(" ");
            //     // progressRobot = response.[2];
            // }
            var response = msg;
            //more nodes needed
            if (msg == "request nodes and edges") {
                buttons();
                //update data being sent, with request for nodes
            } else if (response.indexOf("/") > -1) {
                //split nodes by hashses
                var q = response.split("/");
                //clear any previously added edges and robot positions
                clearUpdate();
                //split nodes into array by spaces
                progressNodes = q[0].split(" ");
                //iterately concatenate nodes into edges and push to list
                for (var i = 0; i < progressNodes.length - 1; i++) {
                    path = progressNodes[i] + progressNodes[i + 1];
                    progressNodes.push();
                }
                //get robot's current position
                progressRobot = q[1].split(" ");
                //show the path
                showPath();
                //delete first item in cmd queue
                console.log("waypoint" + cmdqueue.shift() + "was deleted");
                //send down next iitem in queue
                buttons();
            } else {
                console.insertRow(consoleCount).innerHTML = ("unexpected string received: " + msg);
            }
        }

        socket.onclose = function () {
            console.insertRow(consoleCount).innerHTML = ("connection closed....");
            showServerResponse("The connection has been closed.");
        }
    } else {
        console.insertRow(consoleCount).innerHTML = ("invalid socket");
    }

    function showServerResponse(txt) {
        // var p = document.createElement('p');
        // p.innerHTML = txt;
        // document.getElementById('output').appendChild(p);
    }
}


//function that takes in an array from pathfinding and shows the calculated path
function showPath() {
    //INPUT IS NOW PROGRESSEDGE ARRAY
    var currentPath;
    for (var i = 0; i <= progressNodes.length - 1; i++) {
        currentPath = progressNodes[i];
        switch (currentPath) {
            case "n1-n2":
            case "n2-n1":
                $(document).ready(function () {
                    $('#b-n1-n2').show()
                });
                break
            case "n2-n3":
            case "n3-n2":
                $(document).ready(function () {
                    $('#b-n2-n3').show()
                });
                break
            case "n2-n4":
            case "n4-n2":
                $(document).ready(function () {
                    $('#b-n2-n4').show()
                });
                break
            case "n4-n5":
            case "n5-n4":
                $(document).ready(function () {
                    $('#b-n4-n5').show()
                });
                break
            case "n4-n6":
            case "n6-n4":
                $(document).ready(function () {
                    $('#b-n4-n6').show()
                });
                break
            case "n4-n7":
            case "n7-n4":
                $(document).ready(function () {
                    $('#b-n4-n7').show()
                });
                break
            case "n7-n8":
            case "n8-n7":
                $(document).ready(function () {
                    $('#b-n7-n8').show()
                });
                break
            case "n7-n9":
            case "n9-n7":
                $(document).ready(function () {
                    $('#b-n7-n9').show()
                });
                break
            case "n9-n10":
            case "n10-n9":
                $(document).ready(function () {
                    $('#b-n9-n10').show()
                });
                break
            case "n9-n11":
            case "n11-n9":
                $(document).ready(function () {
                    $('#b-n9-n11').show()
                });
                break
            case "n11-n12":
            case "n12-n11":
                $(document).ready(function () {
                    $('#b-n11-n12').show()
                });
                break
            case "n11-n13":
            case "n13-n11":
                $(document).ready(function () {
                    $('#b-n11-n13').show()
                });
                break
            case "n13-n14":
            case "n14-n13":
                $(document).ready(function () {
                    $('#b-n13-n14').show()
                });
                break
            case "n13-n17":
            case "n17-n13":
                $(document).ready(function () {
                    $('#b-n13-n17').show()
                });
                break
            case "n14-n15":
            case "n15-n14":
                $(document).ready(function () {
                    $('#b-n14-n15').show()
                });
                break
            case "n14-n16":
            case "n16-n14":
                $(document).ready(function () {
                    $('#b-n14-n16').show()
                });
                break
            case "n14-n17":
            case "n17-n14":
                $(document).ready(function () {
                    $('#b-n14-n17').show()
                });
                break
            case "n17-n18":
            case "n18-n17":
                $(document).ready(function () {
                    $('#b-n17-n18').show()
                });
                break
            default:
                console.insertRow(consoleCount).innerHTML = ("No path found");
                stop()
        }
    }
}

//for testing purposes un-comment code//
//  var array = ["n1-n2","n2-n4","n4-n7","n7-n9","n9-n11","n11-n12"];
//  showPath(array)

function move(input) {
    var currentNode;
    currentNode = input[0];
    switch (currentNode) {
        case "n1":
            $(document).ready(function () {
                $('#robot').css({top: 380, left: 85})
            });
            break
        case "n2":
            $(document).ready(function () {
                $('#robot').css({top: 380, left: 185})
            });
        case "n3":
            break
            $(document).ready(function () {
                $('#robot').css({top: 480, left: 185})
            });
            break
        case "n4":
            $(document).ready(function () {
                $('#robot').css({top: 380, left: 435})
            });
            break
        case "n5":
            $(document).ready(function () {
                $('#robot').css({top: 480, left: 435})
            });
            break
        case "n6":
            $(document).ready(function () {
                $('#robot').css({top: 380, left: 710})
            });
            break
        case "n7":
            $(document).ready(function () {
                $('#robot').css({top: 318, left: 435})
            });
            break
        case "n8":
            $(document).ready(function () {
                $('#robot').css({top: 705, left: 325})
            });
            break
        case "n9":
            $(document).ready(function () {
                $('#robot').css({top: 225, left: 625})
            });
            break
        case "n10":
            $(document).ready(function () {
                $('#robot').css({top: 285, left: 710})
            });
            break
        case "n11":
            $(document).ready(function () {
                $('#robot').css({top: 182, left: 621})
            });
            break
        case "n12":
            $(document).ready(function () {
                $('#robot').css({top: 182, left: 621})
            });
            break
        case "n13":
            $(document).ready(function () {
                $('#robot').css({top: 188, left: 385})
            });
            break
        case "n14":
            $(document).ready(function () {
                $('#robot').css({top: 162, left: 230})
            });
            break
        case "n15":
            $(document).ready(function () {
                $('#robot').css({top: 100, left: 230})
            });
            break
        case "n16":
            $(document).ready(function () {
                $('#robot').css({top: 162, left: 85})
            });
            break
        case "n17":
            $(document).ready(function () {
                $('#robot').css({top: 254, left: 385})
            });
            break
        case "n18":
            $(document).ready(function () {
                $('#robot').css({top: 318, left: 385})
            });
            break
        case "n19":
            $(document).ready(function () {
                $('#robot').css({top: 325, left: 85})
            });
            break
        default:
            $(document).ready(function () {
                $('#robot').css({top: 380, left: 85})
            });
    }

}

var defaultArray = [];
move(defaultArray);