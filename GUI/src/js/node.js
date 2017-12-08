var brakes;
var cmdqueue = [];
var edgeQueue = [];
var progressNodes = [];
var progressEdges = [];
var progressRobot = "";
var path;
var sleep;

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
        // window.alert(id);
        // console.insertRow(consoleCount).innerHTML = ("Waypoint Queue: " + cmdqueue.toString());
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
// console.log(cmdqueue.toString());
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
        // console.insertRow(consoleCount).innerHTML = ("Obstacle Queue: " + edgeQueue.toString());
        // console.insertRow(consoleCount).innerHTML = ("Added Obstacle " + id);
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
        function send() {
            socket.send("request path");
        }

        socket.onopen = function () {
            // socket.send("client ready");
            sleep = setInterval(send, 10000);
            buttons();
        }
        //Sends JSON object containing node and edges
        function buttons() {

            var g;
            // var g = {'node': cmdqueue.toString(), 'edges': edgeQueue.toString()};
            // socket.send(JSON.stringify(g));
            if (cmdqueue.length > 0) {
                move("n1");
                if (edgeQueue.length > 0) {
                    g = cmdqueue[0].toString() + "/" + edgeQueue.toString();
                    //window.alert(g.toString());
                    socket.send(g.toString());
                } else {
                    g = cmdqueue[0].toString();
                    //window.alert(g.toString());
                    socket.send(g.toString());
                }
            }else {
                window.alert("You need to add a node before highlighting edges.");
            }


        }

        function clearUpdate() {
            progressEdges = [];
            progressNodes = [];
            progressRobot = "";
        }
        function reset () {
            socket.send("RESET");
            clearUpdate();
            move();
            clearWaypoints();
        }
        socket.onmessage = function (event) {
            var response = event.data;
            // console.insertRow(consoleCount).innerHTML = ("received from server " + response);
            if (response == "ERROR") {
                window.alert("An error has been detected. Valid path not found.");
            }
            else if (response == "PATH COMPLETE") {
                window.alert(cmdqueue.shift());
                move();
                if (cmdqueue.length > 0) {
                    buttons();
                } else {
                    window.alert("The robot has completed navigation. Please hit the reset button.");
                }
            }
            else if (response.indexOf("/") > -1) {

                if (response.split("/").length > 1) {
                    var q = response.split("/");
                    progressNodes = q[0].split(" ");
                    progressRobot = q[1];
                    window.alert(progressRobot);
                    move();
                    progressNodes.unshift(progressRobot);
                    for (var i = 0; i < progressNodes.length - 1; i++) {
                        path = progressNodes[i] + progressNodes[i + 1];
                        progressEdges.push(path);
                    }
                    window.alert(progressEdges);
                    showPath();
                    move();
                } else {
                    // move(progressRobot);
                }
            } else {
                // console.insertRow(consoleCount).innerHTML = ("unexpected string received: " + response);
                if (progressEdges.length > 0) {
                    // window.alert("removing first node and calling show path.. " + progressEdges.shift());
                    progressEdges.shift();
                    showPath();
                    move();
                }
            }
        }

        socket.onclose = function () {
            console.insertRow(consoleCount).innerHTML = ("connection closed....");
            showServerResponse("The connection has been closed.");
        }
        socket.onerror= function(error) {
            window.alert("An unexpected error has occured. Please check the Robot Addresses and try again.");
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
    $(document).ready(function () {
        $('#b-n1-n2').hide()
    });

    $(document).ready(function () {
        $('#b-n2-n3').hide()
    });

    $(document).ready(function () {
        $('#b-n2-n4').hide()
    });

    $(document).ready(function () {
        $('#b-n4-n5').hide()
    });

    $(document).ready(function () {
        $('#b-n4-n6').hide()
    });

    $(document).ready(function () {
        $('#b-n4-n7').hide()
    });

    $(document).ready(function () {
        $('#b-n7-n8').hide()
    });

    $(document).ready(function () {
        $('#b-n7-n9').hide()
    });

    $(document).ready(function () {
        $('#b-n9-n10').hide()
    });

    $(document).ready(function () {
        $('#b-n9-n11').hide()
    });

    $(document).ready(function () {
        $('#b-n11-n12').hide()
    });

    $(document).ready(function () {
        $('#b-n11-n13').hide()
    });

    $(document).ready(function () {
        $('#b-n13-n14').hide()
    });

    $(document).ready(function () {
        $('#b-n13-n17').hide()
    });

    $(document).ready(function () {
        $('#b-n14-n15').hide()
    });

    $(document).ready(function () {
        $('#b-n14-n16').hide()
    });

    $(document).ready(function () {
        $('#b-n14-n17').hide()
    });

    $(document).ready(function () {
        $('#b-n17-n18').hide()
    });

    for (var i = 0; i <= progressEdges.length - 1; i++) {
        currentPath = progressEdges[i];
        // var currentPath;
        // for (var i = 0; i <= input.length - 1; i++) {
        //     currentPath = input[i];
        switch (currentPath) {
            case "n1n2":
            case "n2n1":
            $(document).ready(function () {
                $('#b-n1-n2').show()
            });
            break
            case "n2n3":
            case "n3n2":
            $(document).ready(function () {
                $('#b-n2-n3').show()
            });
            break
            case "n2n4":
            case "n4n2":
            $(document).ready(function () {
                $('#b-n2-n4').show()
            });
            break
            case "n4n5":
            case "n5n4":
            $(document).ready(function () {
                $('#b-n4-n5').show()
            });
            break
            case "n4n6":
            case "n6n4":
            $(document).ready(function () {
                $('#b-n4-n6').show()
            });
            break
            case "n4n7":
            case "n7n4":
            $(document).ready(function () {
                $('#b-n4-n7').show()
            });
            break
            case "n7n8":
            case "n8n7":
            $(document).ready(function () {
                $('#b-n7-n8').show()
            });
            break
            case "n7n9":
            case "n9n7":
            $(document).ready(function () {
                $('#b-n7-n9').show()
            });
            break
            case "n9n10":
            case "n10n9":
            $(document).ready(function () {
                $('#b-n9-n10').show()
            });
            break
            case "n9n11":
            case "n11n9":
            $(document).ready(function () {
                $('#b-n9-n11').show()
            });
            break
            case "n11n12":
            case "n12n11":
            $(document).ready(function () {
                $('#b-n11-n12').show()
            });
            break
            case "n11n13":
            case "n13n11":
            $(document).ready(function () {
                $('#b-n11-n13').show()
            });
            break
            case "n13n14":
            case "n14n13":
            $(document).ready(function () {
                $('#b-n13-n14').show()
            });
            break
            case "n13n17":
            case "n17n13":
            $(document).ready(function () {
                $('#b-n13-n17').show()
            });
            break
            case "n14n15":
            case "n15n14":
            $(document).ready(function () {
                $('#b-n14-n15').show()
            });
            break
            case "n14n16":
            case "n16n14":
            $(document).ready(function () {
                $('#b-n14-n16').show()
            });
            break
            case "n14n17":
            case "n17n14":
            $(document).ready(function () {
                $('#b-n14-n17').show()
            });
            break
            case "n17n18":
            case "n18n17":
            $(document).ready(function () {
                $('#b-n17-n18').show()
            });
            break
            default:
            // console.insertRow(consoleCount).innerHTML = ("No path found");
            // stop()
        }
    }
}

// //for testing purposes un-comment code//
//  var array = ["n1n2","n2n4","n4n7","n7n9","n9n11","n11n12"];
//  showPath(array);

function move() {
    var currentNode;
    currentNode = progressRobot;
    //currentNode = input[0];
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