function startDictation() {
                document.getElementById('transcript').value = '';
                document.getElementById('output').value = '';
                if (window.hasOwnProperty('webkitSpeechRecognition')) {
                    var recognition = new webkitSpeechRecognition();
                    recognition.continuous = false;
                    recognition.interimResults = false;
                    recognition.lang = "en-US";
                    recognition.start();
                    recognition.onresult = function (e) {
                        document.getElementById('loader').hidden = false;
                        document.getElementById('transcript').value = e.results[0][0].transcript;
                        recognition.stop();
                        var data = e.results[0][0].transcript;
                        $.post("http://localhost:5000/news_urls", { "data": data },
                        function (response) {
                        document.getElementById('loader').hidden = true;
                            data = response;
                            document.getElementById("output").value = data["urls"];
                        }).error(function (response) {
                        document.getElementById('loader').hidden = true;
                            if (response.status == 400)
                                text = jQuery.parseJSON(response.responseText)["original_exception"];
                            else
                                text = "I'm sorry. I did not get that.";
                            document.getElementById("output").value = text;
                        });
                    };
                    recognition.onerror = function (e) {
                        recognition.stop();
                        console.log("Recognition had an error");
                    }
                }
            }

            function btnClick() {
	                synth.cancel();
                    var utterThis = new SpeechSynthesisUtterance(document.getElementById("output").value);
                    utterThis.voice = synth.getVoices()[0];
                    utterThis.pitch = 1.0;
                    utterThis.rate = 0.8;
                    utterThis.onerror = function(e) { console.log("Something went wrong with utterance."); };
                    synth.speak(utterThis);
            }