const parentElement = document.querySelector(".two");

parentElement.addEventListener("mousemove", (e) => { // Use parentElement instead of document
  rotateElement(e, parentElement);
})

window.addEventListener("scroll", () => { // Add scroll event listener
  resetRotation(parentElement);
});

function rotateElement(event, element) {
  // get mouse position
  const x = event.clientX;
  const y = event.clientY;
  // console.log(x, y)

  // find the middle
  const middleX = window.innerWidth / 2;
  const middleY = window.innerHeight / 2;
  // console.log(middleX, middleY)

  // get offset from middle as a percentage
  // and tone it down a little
  const offsetX = ((x - middleX) / middleX) * 45;
  const offsetY = ((y - middleY) / middleY) * 45;
  // console.log(offsetX, offsetY);

  // set rotation
  element.style.setProperty("--rotateX", offsetX + "deg");
  element.style.setProperty("--rotateY", -1 * offsetY + "deg");
}

function resetRotation(element) {
  element.style.setProperty("--rotateX", "0");
  element.style.setProperty("--rotateY", "0");
}

/* Courasel */

const carouselItems = document.querySelectorAll('.benefit');
const totalItems = carouselItems.length;
let currentIndex = 0;

function moveToNextItem(){
  if (window.innerWidth < 650){
    for (let i = 0; i < totalItems ; i++){
      carouselItems[i].style.setProperty("display","none")
    }
    if (currentIndex == 2){
      currentIndex = -1;
    }
    currentIndex ++;
  
    carouselItems[currentIndex].style.setProperty("display","flex");
     // Adjust the interval as needed
  } 
}
setInterval(moveToNextItem, 2000);




/* Card script  */

const card = document.querySelector('.card');
const card_content = document.querySelector(".card__content");
const computedStyle = window.getComputedStyle(card_content);

function returncard(){
  card_content.style.setProperty("transform", "rotateY(0)")

}

card.addEventListener("click", ()=>{

  if (window.innerWidth < 650){
    card_content.style.setProperty("transform", "rotateY(.5turn)")
    setInterval(returncard, 7000)
  }
  
})

function backcard(){
      if(card_content.style.transform == ""){
        card_content.style.setProperty("transform", "rotateY(.5turn)");
      }
      else{
        card_content.style.setProperty("transform", "");
      }
      

      console.log(typeof(card_content.style.transform));
    
  

}

setInterval(backcard, 8000);


$(document).ready(function(){
  $("#")
})