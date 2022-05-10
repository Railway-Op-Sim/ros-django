// You should import the CSS file.
//import 'viewerjs/dist/viewer.css';
//import Viewer from 'viewerjs';

console.log($('#image')[0]);

const viewer = new Viewer($('#image')[0], {
  inline: false,
  zoomRatio: 0.5,
  viewed() {
    viewer.zoomTo(1);
  },
});