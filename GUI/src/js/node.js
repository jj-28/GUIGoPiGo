//first make a function that adds and removes waypoint names from the map
var brakes;
var cmdqueue = [];

function addWaypoint(id) {

    var table = document.getElementById("waypointtable");
    if (cmdqueue.length == 0) {
        cmdqueue.push(id);
        window.alert(cmdqueue.toString());
		console.log(cmdqueue.indexOf(id));
        var row = table.insertRow(0);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        cell1.innerHTML = document.getElementById(id).name; + document.getElementById(id).name;
        cell2.innerHTML = '<input type="button" id="cell1.id" class="deleteDep" value="Delete" onclick = "deleteButton(this); deleteFromArray(cmdqueue.indexOf(this.id));" document.getElementById(id).name >';
    } else {
        if (cmdqueue[cmdqueue.length - 1] != id) {
            cmdqueue.push(id);
            window.alert(cmdqueue.toString());
			console.log(cmdqueue.indexOf(id));
            var rowCount = table.rows.length;
            var row = table.insertRow(rowCount);
            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);
            cell1.innerHTML = document.getElementById(id).name;
            cell2.innerHTML = '<input type="button" id="document.getElementById(id)" class="deleteDep" value="Delete" onclick = "deleteButton(this); deleteFromArray(cmdqueue.indexOf(this.id));">';
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
    window.alert(this.rowIndex)
}

function deleteFromArray(i) {
    window.alert()
    cmdqueue.splice(i, 1);
}

//function deleteRow(btn) {
	//var i = r.parentNode.parentNode.rowIndex;
//	var row = btn.parentNode.parentNode;
//	row.parentNode.removeChild(row);
    //document.getElementById("waypointtable").deleteRow(row);
//}

function clearWaypoints() {
    window.alert("Clearing waypoints...")
    while (cmdqueue.length > 0 ) {
       cmdqueue.pop();
       $('#waypointtable tbody').html('');
   }

   window.alert("All waypoints cleared.");
}


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


//function that takes in an array from pathfinding and shows the calculated path
function showPath(input) {
    var currentPath;
    for (var i = 0; i <= input.length - 1; i++) {
        currentPath = input[i]
        switch (currentPath) {
            case "n1-n2":
            case "n2-n1":
            $(document).ready(function(){
                $('#b-n1-n2').show()
            });
            break
            case "n2-n3":
            case "n3-n2":
            $(document).ready(function(){
                $('#b-n2-n3').show()
            });
            break
            case "n2-n4":
            case "n4-n2":
            $(document).ready(function(){
                $('#b-n2-n4').show()
            });
            break
            case "n4-n5":
            case "n5-n4":
            $(document).ready(function(){
                $('#b-n4-n5').show()
            });
            break
            case "n4-n6":
            case "n6-n4":
            $(document).ready(function(){
                $('#b-n4-n6').show()
            });
            break
            case "n4-n7":
            case "n7-n4":
            $(document).ready(function(){
                $('#b-n4-n7').show()
            });
            break
            case "n7-n8":
            case "n8-n7":
            $(document).ready(function(){
                $('#b-n7-n8').show()
            });
            break
            case "n7-n9":
            case "n9-n7":
            $(document).ready(function(){
                $('#b-n7-n9').show()
            });
            break
            case "n9-n10":
            case "n10-n9":
            $(document).ready(function(){
                $('#b-n9-n10').show()
            });
            break
            case "n9-n11":
            case "n11-n9":
            $(document).ready(function(){
                $('#b-n9-n11').show()
            });
            break
            case "n11-n12":
            case "n12-n11":
            $(document).ready(function(){
                $('#b-n11-n12').show()
            });
            break
            case "n11-n13":
            case "n13-n11":
            $(document).ready(function(){
                $('#b-n11-n13').show()
            });
            break
            case "n13-n14":
            case "n14-n13":
            $(document).ready(function(){
                $('#b-n13-n14').show()
            });
            break
            case "n13-n17":
            case "n17-n13":
            $(document).ready(function(){
                $('#b-n13-n17').show()
            });
            break
            case "n14-n15":
            case "n15-n14":
            $(document).ready(function(){
                $('#b-n14-n15').show()
            });
            break
            case "n14-n16":
            case "n16-n14":
            $(document).ready(function(){
                $('#b-n14-n16').show()
            });
            break
            case "n14-n17":
            case "n17-n14":
            $(document).ready(function(){
                $('#b-n14-n17').show()
            });
            break
            case "n17-n18":
            case "n18-n17":
            $(document).ready(function(){
                $('#b-n17-n18').show()
            });
            break
            default:
            window.alert("you done fucked up a a ron")
            alert(currentPath)
        }
    }
}

//for testing purposes un-comment code//
 // var array = ["n1-n2","n2-n4","n4-n7","n7-n9","n9-n11","n11-n12"];
 // showPath(array)

function doSomething(){
    window.alert("YES")
}