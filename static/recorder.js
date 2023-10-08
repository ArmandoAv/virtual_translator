let blobs = [];
let stream;
let rec;
let recordUrl;
let audioResponseHandler;

// Only record the URL to call (for example, /audio) and the 'handler'
// or 'callback' when the recording ends
function recorder(url, handler) {
    recordUrl = url;
    if (typeof handler !== "undefined") {
        audioResponseHandler = handler;
    }
}

async function record() {
    try {
        document.getElementById("text").innerHTML = "<i>Recording...</i>";
        document.getElementById("record").style.display="none";
        document.getElementById("stop").style.display="";
        document.getElementById("record-stop-label").style.display="block"
        document.getElementById("record-stop-loading").style.display="none"
        document.getElementById("stop").disabled=false

        blobs = [];

        // Recording audio
        stream = await navigator.mediaDevices.getUserMedia({audio:true, video:false})
        rec = new MediaRecorder(stream);
        rec.ondataavailable = e => {
            if (e.data) {
                blobs.push(e.data);
            }
        }
        
        rec.onstop = doPreview;
        
        rec.start();
    } catch (e) {
        alert("Could not start audio recorder! Please verify that you have the appropriate permission, are on HTTPS, etc...");
    }
}

function doPreview() {
    if (!blobs.length) {
        console.log("There aren't blobs!");
    } else {
        console.log("We have blobs!");
        const blob = new Blob(blobs);

        // Use fetch to send recorded audio to Python
        var fd = new FormData();
        fd.append("audio", blob, "audio");

        fetch(recordUrl, {
            method: "POST",
            body: fd,
        })
        .then((response) => response.json())
        .then(audioResponseHandler)
        .catch(err => {
            // Catch the error
            console.log("An error occurred: ", err);
        });
    }
}

function stop() {
    document.getElementById("record-stop-label").style.display="none";
    document.getElementById("record-stop-loading").style.display="block";
    document.getElementById("stop").disabled=true;
    
    rec.stop();
}

// Call the handler if there is one
function handleAudioResponse(response){
    if (!response || response == null) {
        console.log("Doesn't respond");
        return;
    }

    document.getElementById("record").style.display="";
    document.getElementById("stop").style.display="none";
    
    if (audioResponseHandler != null) {
        audioResponseHandler(response);
    }
}