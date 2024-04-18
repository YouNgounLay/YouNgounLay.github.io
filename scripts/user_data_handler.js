function sendPostRequest() {
  // Create an XMLHttpRequest object
  var xhr = new XMLHttpRequest();

  // Define the request parameters
  var url = "http://127.0.0.1:8000/request_handler/follow_user/";
  var data = JSON.stringify({
    username: "test subject 01",
    socialUrl: "test@subject.01",
    note: "asdklfjasdlkfj",
  }); // Replace 'key' and 'value' with your data
  var method = "POST";

  // Configure the request
  xhr.open(method, url, true);
  xhr.setRequestHeader("Content-Type", "application/json");

  // Handle the response
  xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        console.log("POST request successful");
        console.log("Response:", xhr.responseText);
      } else {
        console.error("Error:", xhr.statusText);
      }
    }
  };

  // Send the request
  xhr.send(data);
}
