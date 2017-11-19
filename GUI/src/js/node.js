//first make a function that adds and removes waypoint names from the map
var brakes;
var cmdqueue = [];
var edgeQueue = [];

function addWaypoint(id) {
	
    var table = document.getElementById("waypointtable");
    if (cmdqueue.length == 0) {
        cmdqueue.push(id);
        // window.alert(cmdqueue.toString());
		console.log(cmdqueue.indexOf(id));
        var row = table.insertRow(0);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        cell1.innerHTML = document.getElementById(id).name;
        cell2.innerHTML = '<input type="button" id="cell1.id" name="document.getElementById(id).name" class="deleteDep" value="Delete" onclick = "deleteButton(this); deleteFromArray(this); deleteFromArray(cmdqueue.indexOf(this.id));">';
    } else {
        if (cmdqueue[cmdqueue.length - 1] != id) {
            cmdqueue.push(id);
            // window.alert(cmdqueue.toString());
			console.log(cmdqueue.indexOf(id));
            var rowCount = table.rows.length;
            var row = table.insertRow(rowCount);
            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);
            cell1.innerHTML = document.getElementById(id).name;
            cell2.innerHTML = '<input type="button" id="document.getElementById(id)" name="document.getElementById(id).name" class="deleteDep" value="Delete" onclick = "deleteButton(this); deleteFromArray(cmdqueue.indexOf(this.id));">';
        } else {
            window.alert("You can't add the same waypoint 2 times in a row. Ex:No N1-N1-N@");
        }
    }
}

function deleteButton(button){
    button.addEventListener("click", function(){
        var i = cmdqueue.indexOf(this.id);
      cmdqueue.splice(cmdqueue.indexOf(this.id),1);
        this.parentNode.parentNode.remove(); //"this" refer to the "button" object

    }, false);
}

function deleteFromArray(i) {
    // window.alert()
    cmdqueue.splice(i, 1);
	// var $row = $(this).closest("tr");    // Find the row
 //    var $text = $row.find("td").text; // Find the text
    
 //    // Let's test it out
 //    alert($row);
 //    alert($text);
}

//function deleteRow(btn) {
	//var i = r.parentNode.parentNode.rowIndex;
//	var row = btn.parentNode.parentNode;
//	row.parentNode.removeChild(row);
    //document.getElementById("waypointtable").deleteRow(row);
//}

function clearWaypoints() {
    // window.alert("Clearing waypoints...")
    while (cmdqueue.length > 0 ) {
       cmdqueue.pop();
       $('#waypointtable tbody').html('');
   }

   // window.alert("All waypoints cleared.");
}

function addEdgeQueue(id) {
    for (var i =0; i <edgeQueue.length; i++) {
        if (edgeQueue[i]== 0) {
            edgeQueue[i] = id;
            window.alert(cmdqueue.toString());
        }else {
            console.log("something at " + i);
        git }
    }
}
function deleteEdge(id) {
    for (var i=0; i<edgeQueue.length; i++) {
        if (edgeQueue[i] == id) {
            edgeQueue[i] = 0;
            window.alert("edge deleted")
        }
    }
}

// Creates the websockets connection
function setup2()
{
    // window.alert("Initiating robot")
    var $txt = $("#data");      			// assigns the data(hostname/ip address) entered in the text box
    name = $txt.val();          			// Variable name contains the string(hostname/ip address) entered in the text box
    var host =  "ws://"+name+":9093/ws"; 	// combines the three string and creates a new string
    var socket = new WebSocket(host);
    var $txt = $("data");
    var $btnSend = $("#sendtext");
    $txt.focus();

    // event handlers for UI
    $btnSend.on('click',function()
    {
        var text = $txt.val();
        if(text == "")
        {
            return;
        }
        $txt.val("");
    });

    //might adapt for sending mock edges over
    // $txt
    //     .keypress(function(evt)
    //     {
    //         if(evt.which == 13)
    //         {
    //             $btnSend.click();
    //         }
    //     });
    //
    // // event handlers for websocket
    if(socket)
    {
        // window.alert("Establishing connection wirh the robot");
      var count =1;
      socket.onopen = function()
      {
        count = 0;
            // arrows();     // function for detecting keyboard presses
         // socket.send("waiting");
            buttons();    // function for detecting the button press on webpage
        }
        //Send the button pressed backed to the Raspberry Pi
        function buttons()
        {
        socket.send(cmdqueue.toString());
    }
    socket.onmessage = function(msg)
    {

        // showServerResponse(msg.data);
    }
    socket.onclose = function()
    {
            window.alert("connection closed....");
            showServerResponse("The connection has been closed.");
        }
    }
    else
    {
        console.log("invalid socket");
    }
    function showServerResponse(txt)
    {
        var p = document.createElement('p');
        p.innerHTML = txt;
        document.getElementById('output').appendChild(p);
    }
}

jQuery(function($)
{
    if (!("WebSocket" in window))
    {
        alert("Your browser does not support web sockets");
    }
});

