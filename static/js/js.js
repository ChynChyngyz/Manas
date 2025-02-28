document.addEventListener("DOMContentLoaded", () => {
    const timelineContainers = document.querySelectorAll(".timeline-container");
    const timelines = document.querySelectorAll(".timeline"); // Родители для псевдоэлемента

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("animate");

                const timeline = entry.target.closest('.timeline');
                if (timeline) {
                    timeline.classList.add("animate");
                }

                observer.unobserve(entry.target);
            }
        });
    });

    timelineContainers.forEach(container => {
        observer.observe(container);
    });
});


var tablinks = document.getElementsByClassName('tab-links');
var tabcontents = document.getElementsByClassName('tab-contents');

function opentab(tabname) {
    for (tablink of tablinks) {
        tablink.classList.remove("active-link");
    }
    for (tabcontent of tabcontents) {
        tabcontent.classList.remove("active-tab")
    }
    event.currentTarget.classList.add("active-link");
    document.getElementById(tabname).classList.add("active-tab");

}


const swiper = new Swiper('.swiper', {
    loop: true,

    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },

    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
      },

});