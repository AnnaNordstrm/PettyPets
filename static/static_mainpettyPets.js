

var a_joke = ["I wondered why the frisbee was getting bigger...", "then it hit me."]; 

    function tell_buildup() {
        // assumes that the joke consists of a list.
        document.getElementById("buildup").innerHTML = a_joke[0];
    }

    function tell_punchline() {
        // assumes that the joke consists of a list.
        document.getElementById("punchline").innerHTML = a_joke[1];
    }

    function clear_joke() {
        // removes the joke from the screen. 
        
        document.getElementById("joke").innerHTML = "";
        document.getElementById("buildup").innerHTML = "";
        document.getElementById("punchline").innerHTML = "";

    }

    function tell_joke() {
        //get a joke from joke dictionary. Yet to be implemented.

        //tell a joke.
        document.getElementById("joke").innerHTML = "Here's a little joke for you...";
        window.setTimeout(tell_buildup, 4000); // wait 4 seconds
        window.setTimeout(tell_punchline, 8000); // wait another 4 seconds

        // clear it.
        window.setTimeout(clear_joke, 12000); // wait yet another 4 seconds before removing the joke from screen.
    }

    function timer(time) {
        // will be called upon when feeding the lemur, or any other interaction.
        // will count to to the provided time (an int representings seconds), then it returns "stop" to whatever called it, in order to make an animation stop.
        startTime = new Date();
        var counting = true;
        while (counting == true){
            endTime = new Date();
            var timeDiff = endTime - startTime; //in ms 
            // strip the ms 
            timeDiff /= 1000; 

            // get seconds 
            var seconds = Math.round(timeDiff);
            if (seconds > time) {
                counting = false;
            }
        }
        return "stop"
    }
// TODO: Byt namn på eating, eller dela helt enkelt upp det
    eating = (val) => {
        // change level of fullnes by calling for tryFeed in food_level.py. Has now been implemented.
        var text1 = val

        $.ajax(
            {
                url: "/home",
                type: "POST",
                data: {  
                    text1: text1
                }
            }).done((response) => {
            var html = "<p> Result : </p>";
            response = response.esult;
            $.each(response, (key, val) => {
                html += "<p>" + key + ": " + val + "</p>"
                console.log(html)
                if (val == "dead") {
                document.getElementById("x").src = "https://giphy.com/embed/krMpiV41eo264"
                
            } else {
            
            document.getElementById("x").src="https://giphy.com/embed/bWFSMCn6BzM3fyRCCg"; // can you have ; here?
            var animate_eating = timer(4);
            if (animate_eating == "stop") {
            // go back to normal gif
                document.getElementById("x").src="https://giphy.com/embed/KZMWLuOepc88Q6a4jU";
                }
            tell_joke();
            }
        $(".results").append(html);
        })
    })

    check = (val) => {
        // Updates the user on how hungry their pet is, without changing anything
        var text1 = val
        $.ajax(
            {
                url: "/join",
                type: "POST",
                data: {  
                    text1: text1
                }
            }).done((response) => {
            var html = "<p> Result : </p>";
            response = response.esult;
            $.each(response, (key, val) => {
                html += "<p>" + key + ": " + val + "</p>"
        $(".results").append(html);
        //document.getElementById("x").src="https://giphy.com/embed/qozauafWRlIxG";
        //var animate_sleeping = timer(4);
        //if (animate_sleeping == "stop") {
            // go back to normal gif
            //document.getElementById("x").src="https://giphy.com/embed/KZMWLuOepc88Q6a4jU";
        //}

            
        })    
    })
    }
    }
window.onload=function(){
    document.getElementById('food_button').addEventListener("click", eating("2"));
    }
    
