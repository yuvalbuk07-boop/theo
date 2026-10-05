if('serviceWorker' in navigator){
  // Reload once when a new version takes over, so updates show up without closing the app.
  let reloaded=false;
  navigator.serviceWorker.addEventListener('controllerchange',()=>{if(!reloaded&&navigator.serviceWorker.controller){reloaded=true;location.reload()}});
  window.addEventListener('load',()=>navigator.serviceWorker.register('sw.js',{updateViaCache:'none'}).then(r=>{r.update();document.addEventListener('visibilitychange',()=>{if(document.visibilityState==='visible')r.update()})}).catch(()=>{}));
}
