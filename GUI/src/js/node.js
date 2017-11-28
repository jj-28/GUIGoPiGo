var brakes;
var cmdqueue = [];
var edgeQueue = [];
var progressNodes;
var progressEdges;
var progressRobot;

function addWaypoint(id) {
    var table = document.getElementById("waypointtable");
    if (cmdqueue.length == 0) {
        cmdqueue.push(id);
        console.log(cmdqueue.indexOf(id));
        var row = table.insertRow(0);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        cell1.innerHTML = document.getElementById(id).name;
        cell2.innerHTML = '<input type="button" name="document.getElementById(id).name" class="deleteDep" value="Delete" onclick = "deleteButton(this); deleteFromArray(this); deleteFromArray(cmdqueue.indexOf(this.id));">';
    } else {
        if (cmdqueue[cmdqueue.length - 1] != id) {
            cmdqueue.push(id);
            console.log(cmdqueue.indexOf(id));
            var rowCount = table.rows.length;
            var row = table.insertRow(rowCount);
            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);
            cell1.innerHTML = document.getElementById(id).name;
            cell2.innerHTML = '<input type="button" name="document.getElementById(id).name" class="deleteDep" value="Delete" onclick = "deleteButton(this); deleteFromArray(cmdqueue.indexOf(this.id));">';
        } else {
            window.alert("You can't add the same waypoint 2 times in a row. Ex:No N1-N1-N@");
        }
    }
}

// function deleteRow(cell2) {
//     var row = btn.parentNode.parentNode;
//     row.parentNode.removeChild(row);
// }

// function deleteButton(button) {
//     button.addEventListener("click", function () {
//         var i = cmdqueue.indexOf(this.id);
//         cmdqueue.splice(cmdqueue.indexOf(this.id), 1);
//         this.parentNode.parentNode.remove(); //"this" refer to the "button" object
//
//     }, false);
// }
//
// function deleteFromArray(i) {
//     // window.alert()
//     cmdqueue.splice(i, 1);
//     var $row = $(this).closest("tr");    // Find the row
//        var $text = $row.find("td").text; // Find the text
//
//     //    // Let's test it out
//     //    alert($row);
//     //    alert($text);
// }
//
// function deleteRow(btn) {
// var i = r.parentNode.parentNode.rowIndex;
// 	var row = btn.parentNode.parentNode;
// 	row.parentNode.removeChild(row);
// document.getElementById("waypointtable").deleteRow(row);
// }

// clears waypoints and edges
function clearWaypoints() {
    while (cmdqueue.length > 0) {
        cmdqueue.pop();
        $('#waypointtable tbody').html('');
    }
}
//adds and removes edges from array onClick
function maintainQueue(id) {
    if (edgeQueue.indexOf(id) == -1) {
        edgeQueue.push(id);
        window.alert(edgeQueue.toString());
    } else {
        edgeQueue.splice(edgeQueue.indexOf(id), 1);
        window.alert("removed, array looks like " + edgeQueue.toString());
    }
}

// Creates the websockets connection
function setup2() {
    // window.alert("Initiating robot")
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
            socket.send("client ready");
        }

        //Sends JSON object containing node and edges
        function buttons() {

            var g = {'node': cmdqueue.toString(), 'edges': edgeQueue.toString()};
            socket.send(JSON.stringify(g));
        }
        //clears previous update information
        function clearUpdate() {
            progressEdges = [];
            progressNodes = [];
            progressRobot = "";
        }


        socket.onmessage = function (msg) {
            // if (typeof msg == 'string') {
            //     if (msg == "request nodes and edges") {
            //         buttons();
            //     } else {
            //         window.alert("unexpected string received: " + msg);
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
            var response =  msg;
            if (response.indexOf("/") > -1 ) {
                var q = response.split("/");
                clearUpdate();
                progressNodes = q[0].split(" ");
                progressEdges = q[2].split(" ");
                progressRobot = q[1].split(" ");
            } else {
                    if (msg == "request nodes and edges") {
                        buttons();
                    } else {
                        window.alert("unexpected string received: " + msg);
                    }
            }
        }

        socket.onclose = function () {
            window.alert("connection closed....");
            showServerResponse("The connection has been closed.");
        }
    } else {
        console.log("invalid socket");
    }

    function showServerResponse(txt) {
        // var p = document.createElement('p');
        // p.innerHTML = txt;
        // document.getElementById('output').appendChild(p);
    }

    jQuery(function ($) {
        if (!("WebSocket" in window)) {
            alert("Your browser does not support web sockets");
        }
    });

}
