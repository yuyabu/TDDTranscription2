chrome.webNavigation.onCommitted.addListener(function(data) {
  console.log('onCommitted', data.tabId, data.url,data.timeStamp);
});
chrome.webNavigation.onBeforeNavigate.addListener(function(data) {
  console.log('onBeforeNavigate', data.tabId, data.url,data.timeStamp);
});
chrome.webNavigation.onDOMContentLoaded.addListener(function(data) {
  console.log('onDOMContentLoaded', data.tabId, data.url,data.timeStamp);
});
chrome.webNavigation.onCompleted.addListener(function(data) {
  console.log('onCompleted', data.tabId, data.url,data.timeStamp);
});
