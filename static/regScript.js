setTimeout(() => {
  const flash = document.querySelector(".flash-message");
  if (flash) {
    flash.style.transition = "opacity 1s ease";
    flash.style.opacity = "0";
    setTimeout(() => flash.remove(), 1000);
  }
}, 3000); // fades out after 3 seconds
