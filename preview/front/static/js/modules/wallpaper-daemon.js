export class WallpaperDaemon {
  constructor(options = {}) {
    this.wallpaperEl = document.getElementById("background");

    this.wallpaperDir = "/static/wallpapers/";
    this.currentWallpaper = "wallpaper1.jpg";

    this.init();
  }

  init() {
    this.setWallpaper();
  }

  setWallpaper() {
    const wallpaperPath = this.wallpaperDir + this.currentWallpaper;

    const img = new Image();
    img.onload = () => {
      this.wallpaperEl.style.backgroundImage = `url('${wallpaperPath}')`;
    }

    img.src = wallpaperPath;

    return true;
  }
}

