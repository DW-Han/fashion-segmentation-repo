chrome.downloads.onChanged.addListener(function(downloadDelta) {
    if (downloadDelta.state && downloadDelta.state.current === 'complete') {

      // getting last download and checking if its a power point
      chrome.downloads.search({id: downloadDelta.id}, function(downloadItems) {
        //most recent download
        console.log(downloadItems[0].url);
        
        //if pptx then create window and send info
        if (downloadItems[0].filename.endsWith('.jpg') || downloadItems[0].filename.endsWith('.png')) {
          console.log(downloadItems[0].filename + ' is a PowerPoint presentation.');
          window.postMessage({greeting: "hello from background"}, "*");
          var fileName = "filepath.txt";
          var contentType = "text/plain";
          download(downloadItems[0].filename, fileName, contentType);

          chrome.windows.create({
            url: "popup.html",
            type: "popup",
            width: 340,
            height: 200
          });
        
        // if not pptx do nothing
        } else {
          console.log(downloadItems[0].filename + ' is not a PowerPoint presentation.');
        }
      });
      
    }
  });
  

  function callFunction()
  {
    alert(1)
    $.ajax({
      url: "/translate/",
      type:"POST",
      lang: { "link": value },
      link: { "link": "your data" },
      success: function(response){
          alert(response);
      }
  });
  }

  chrome.downloads.onChanged.addListener(function(downloadDelta) {
    if (downloadDelta.state) {
      console.log(downloadDelta.state.current);
    }
  });

  function download(content, fileName, contentType) {
    var a = document.createElement("a");
    var file = new Blob([content], {type: contentType});
    a.href = URL.createObjectURL(file);
    a.download = fileName;
    a.click();
  }
