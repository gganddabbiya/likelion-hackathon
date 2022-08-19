var closeArray = document.querySelector(".exhibitionNavBar-1");
var ganadaArray = document.querySelector(".exhibitionNavBar-2")
var newArray = document.querySelector(".exhibitionNavBar-3")

closeArray.addEventListener("click", function(){
    ganadaArray.style.color="gray";
    newArray.style.color="gray";
    closeArray.style.color="black";

    closeArray.style.fontWeight="bold"
    ganadaArray.style.fontWeight="500"
    newArray.style.fontWeight="500"
});
ganadaArray.addEventListener("click", function(){
    closeArray.style.color="gray";
    newArray.style.color="gray";
    ganadaArray.style.color="black"

    ganadaArray.style.fontWeight="bold"
    closeArray.style.fontWeight="500"
    newArray.style.fontWeight="500"
});
newArray.addEventListener("click", function(){
    ganadaArray.style.color="gray";
    closeArray.style.color="gray";
    newArray.style.color="black"

    newArray.style.fontWeight="bold"
    closeArray.style.fontWeight="500"
    ganadaArray.style.fontWeight="500"
});