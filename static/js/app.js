// ========== Retractable Header ==========
// Store navbar classes
const navHeader = document.querySelector(".site-header");
const navClasses = navHeader.classList;

function homeAction() {
  return
}

function downAction() {
  navClasses.remove("nav-open");
  navClasses.add("nav-collapse");
}

function upAction() {
  navClasses.remove("nav-collapse");
  navClasses.add("nav-open");
}

// returns current scroll position
var scrollTop = function () {
  return window.scrollY;
};

// Initial scroll position
var scrollState = 0;

// Primary scroll event function
var scrollDetect = function (home, down, up) {
  // Current scroll position
  var currentScroll = scrollTop();
  if (scrollTop() === 0) {
    home();
  } else if (currentScroll > scrollState) {
    down();
  } else {
    up();
  }
  // Set previous scroll position
  scrollState = scrollTop();
};

window.addEventListener("scroll", function () {
  scrollDetect(homeAction, downAction, upAction);
});
// ========== end Retractable Header ==========

// ========== add space to make up for the header size ==========
const navSpacer = document.querySelector('[js-header-spacer]');

function setSpacer(navElement) {
  navSpacer.style.height = navElement.offsetHeight + 'px';
}

setSpacer(navHeader);
// ========== add space to make up for the header size ==========

// set year for copyright
const copyright = document.getElementById('copyright');
const year = new Date().getFullYear();
copyright.textContent = year;