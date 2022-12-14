// Home Banner Slide Show
// Aidan Daley
const homeImages = ["Media/home/home1.JPG","Media/home/home2.JPG","Media/home/home3.JPG", "Media/home/home4.JPG", "Media/home/home5.JPG", "Media/home/home6.JPG"]


// Event Listener
let n = 0;

setInterval(function() {
    n = (n + 1) % homeImages.length;
    console.log(n);

    $(document).ready(function() {
        $("#homeImage").fadeOut(500, () => {
            $("#homeImage").attr('src', homeImages[n]);
            $("#homeImage").fadeIn(500);
        });
    });
}, 5000);



