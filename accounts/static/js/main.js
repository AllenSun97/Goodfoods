var slideshow = document.getElementById('slideshow');
var slides = slideshow.getElementsByTagName('img');
var overlaies = document.querySelectorAll('.overlay');
var i = 0;

function nextslide(){
  slides[i].classList.remove('active');
  overlaies[i].classList.remove('active');
  i = (i+1) % slides.length;
  slides[i].classList.add('active');
  overlaies[i].classList.add('active');
}

function prevslide(){
  slides[i].classList.remove('active');
  overlaies[i].classList.remove('active');
  i -= 1;         //index = (index - 1 + slides.length % slides.length)
  if(i < 0) i = 2;
  slides[i].classList.add('active');
  overlaies[i].classList.add('active');
}

var slideshowText = document.getElementById('slideshowText');
var slidesText = slideshowText.getElementsByTagName('div');
var k = 0;

function prevslideText(){
  slidesText[k].classList.remove('active');
  k = (k + 1) % slidesText.length;
  slidesText[k].classList.add('active');
}

function nextslideText(){
  slidesText[k].classList.remove('active');
  k -= 1;         //index = (index - 1 + slides.length % slides.length)
  if(k < 0) k = 2;
  slidesText[k].classList.add('active');
}

const leaves =document.querySelectorAll('.leaf')
leaves.forEach(item => 
  item.addEventListener("click",putleaf));

function putleaf(){
  leaves.forEach((item)=>
  item.classList.remove('leaf-on'));
  this.classList.add('leaf-on');
}
function menuToggle(){
  const togglemenu = document.querySelector('#navbar')

  togglemenu.classList.toggle('active')
}

//Get the button:
mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
// this shit is broken
window.addEventListener('scroll', ()=>{
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";} 
  else {
    mybutton.style.display = "none";
  }
})
// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
