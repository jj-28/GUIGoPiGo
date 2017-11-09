//first make a function that adds and removes waypoint names from the map
var brakes;
var cmdqueue= Array();
function addWaypoint(id) {
    var table = document.getElementById("waypointtable");
//        for (var i = 0; i < cmdqueue.length; i++) {
    if (cmdqueue.length == 0) {
        cmdqueue.push(id);
        // document.getElementById("print").innerHTML = cmdqueue.length;
        window.alert(cmdqueue.toString());
        // cmdqueue[x] = document.getElementById(id).value;
        // alert("Element: " + cmdqueue[x] + " Added at index " + x);
        // x++;
        var row = table.insertRow(0);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        cell1.innerHTML = '<input type="button" class="deleteDep" value="Delete" onclick = "deleteRow()">';
        cell2.innerHTML = document.getElementById(id).name;
        //setup2();
    } else {
        if (cmdqueue[cmdqueue.length - 1] != id) {
            // cmdqueue[x] = document.getElementById(id).value;
            // alert("Element: " + cmdqueue[x] + " Added at index " + x);
            // x++;
            cmdqueue.push(id);
            // document.getElementById("print").innerHTML = cmdqueue.length;
            window.alert(cmdqueue.toString());
            var rowCount = table.rows.length;
            var row = table.insertRow(rowCount);
            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);
            cell1.innerHTML = '<input type="button" class="deleteDep" value="Delete" onclick = "deleteRow()">';
            cell2.innerHTML = document.getElementById(id).name;
            //setup2();
        } else {
            window.alert("You can't add the same waypoint 2 times in a row. Ex:No N1-N1-N@");
            //setup2();
        }
    }
}

function clearWaypoints() {
    window.alert("Clearing waypoints...")
   while (cmdqueue.length > 0 ) {
       cmdqueue.pop();
       $('#waypointtable tbody').html('');
   }

    window.alert("All waypoints cleared.");
}

// function stop()
// {
// brakes = "b";
//     setup2();
// }

// Creates the websockets connection
function setup2()
{
    window.alert("Initiating robot")
    var $txt = $("#ip");      			// assigns the data(hostname/ip address) entered in the text box
    name = $txt.val();          			// Variable name contains the string(hostname/ip address) entered in the text box
    var host =  "ws://"+name+":9093/ws"; 	// combines the three string and creates a new string
    var socket = new WebSocket(host);
    var $txt = $("#ip");
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
      //  window.alert("Establishing connection wirh the robot");
        var count =1;
        socket.onopen = function()

        {
            count = 0;
            // arrows();     // function for detecting keyboard presses
            buttons();    // function for detecting the button press on webpage
        }
        //Send the button pressed backed to the Raspberry Pi
        function buttons()
        {
            // if(brakes == "b")
            // {
            //     socket.send("b");
            // }
        // window.alert("sending waypoints...");
            socket.send(cmdqueue.toString());
        }
        socket.onmessage = function(msg)
        {
            showServerResponse(msg.data);
        }
        socket.onclose = function()
        {
            //alert("connection closed....");
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

